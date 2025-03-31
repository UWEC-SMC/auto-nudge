import os
from pathlib import Path

import backoff
import requests

from datetime import datetime, timedelta
from dotenv import load_dotenv

from models.auto_nudge_cache import AutoNudgeCache
from models.nudge_config import NudgeConfig
from models.macos_sofa_feed import MacSofaFeed
from num2words import num2words
from pydantic import ValidationError
from requests.exceptions import Timeout, ConnectionError
from typing import Optional, Tuple

load_dotenv()

MACOS_SOFA_FEED_URL = os.getenv("MACOS_SOFA_FEED_URL", "https://sofafeed.macadmins.io/v1/macos_data_feed.json")
NUDGE_CONFIG_PATH = os.getenv("NUDGE_CONFIG_PATH", "./v1/nudge_config.json")
FORCE_UPDATE = True if os.getenv("NUDGE_FORCE_UPDATE", "false").lower() == "true" else False
CACHE_PATH = os.getenv("AUTO_NUDGE_CACHE_PATH", ".auto_nudge_cache.json")


@backoff.on_exception(backoff.expo, (Timeout, ConnectionError), max_tries=3)
def get_feed(feed_url: str) -> MacSofaFeed:
    """Retrieves and validates the SOFA feed from the provided url.

    Args:
        feed_url (str): The url from which to retrieve the SOFA feed.

    Returns:
        MacSofaFeed: Validated SOFA Feed object
    """
    print(f"Retrieving SOFA feed from {feed_url}")
    res = requests.get(feed_url)
    res.raise_for_status()

    return MacSofaFeed.model_validate_json(res.text)


def get_nudge_config(config_path: str) -> NudgeConfig:
    """Retrieves and validates the Nudge configuration from the provided path.

    Args:
        config_path (str): The path from which to retrieve the Nudge configuration.

    Returns:
        NudgeConfig: Validate Nudge Configu object
    """
    print(f"Retrieving Nudge configuration from {config_path}")
    with open(config_path, "r", encoding="utf-8") as json:
        return NudgeConfig.model_validate_json(json.read(), strict=True)


def is_within_blackout(config: NudgeConfig) -> Tuple[bool, Optional[str]]:
    """Checks if we're currently in a blackout period as defined by a provided Nudge configuration.

    Args:
        config (NudgeConfig): The Nudge configuration used to evaluate if we're within a blackout period.

    Returns:
        Tuple[bool, Optional[str]]: A tuple containing a bool for if we're within a blackout of not, and if so, a string containing it's associated comment.
    """
    print("Checking if we're within a blackout period")
    for period in config.metadata.blackout_periods:
        if period.is_in_blackout(datetime.now()):
            return True, period.comment

    return False, None


def get_cache(path: str) -> AutoNudgeCache:
    """
    Retrieves the current cache from the provided file path. If the cache isn't present, a new one will be created.

    Args:
        path (str): The file path to retrieve the cache from.

    Returns:
        AutoNudgeCache: The current cache. If none is present, a newly initialized cache will be returned.
    """
    cache_path = Path(path)
    cache: AutoNudgeCache

    print(f"Checking for existing cache at {cache_path}")
    if cache_path.is_file():
        print("Cache hit")
    else:
        print("No cache present - creating one")
        open(cache_path, 'w').close() # Create empty file

    with open(cache_path) as file:
        try:
            cache = AutoNudgeCache.model_validate_json(file.read())
        except ValidationError as e:
            cache = AutoNudgeCache()

    return cache

def should_update_config(feed: MacSofaFeed, config: NudgeConfig) -> bool:
    """Checks if the Nudge configuration requires updating. This is done by checking if the latest version
    contained within the SOFA Feed is different from what the Nudge config is currently targeting.

    Args:
        feed (MacSofaFeed): SOFA Feed object containing a list of macOS versions.
        config (NudgeConfig): The current Nudge configuration object.

    Returns:
        bool: True if the config should be updated, False otherwise.
    """
    print("Determining if Nudge config needs to be updated")
    return config.os_version_requirements[0].required_minimum_os_version != feed.os_versions[0].latest.product_version


def update_config(feed: MacSofaFeed, config: NudgeConfig) -> None:
    """Updates the provided Nudge configuration using values from the provided SOFA feed. Will update the required_minimum_os_version and the mainContentNote body text.

    Args:
        feed (MacSofaFeed): SOFA Feed object used to update the Nudge config.
        config (NudgeConfig): Nudge config object to be updated.

    Returns:
        None
    """
    print("Updating Nudge configuration")
    # Actionable changes detected. Update our config as necessary.
    # Update target version
    config.os_version_requirements[0].required_minimum_os_version = feed.os_versions[0].latest.product_version

    # Update install deadline
    # Set our offset to 2 weeks by default, or 1 week if the new version resolves an actively exploited CVE
    deadline_offset = (
        timedelta(weeks=2)
        if len(feed.os_versions[0].security_releases[0].actively_exploited_cves) == 0
        else timedelta(weeks=1)
    )
    install_deadline = datetime.now() + deadline_offset
    config.os_version_requirements[0].required_installation_date = install_deadline.strftime("%Y-%m-%dT00:00:00Z")

    # Update body text
    date_string = install_deadline.strftime("%A, %B {day}, %Y").format(
        day=num2words(install_deadline.day, to="ordinal_num")
    )
    config.user_interface.update_elements[0].main_content_note = config.metadata.note_template.format(date_string)


def main():
    sofa_feed: MacSofaFeed
    nudge_config: NudgeConfig
    config_updated = False
    cache = get_cache(CACHE_PATH)

    # Retrieve macOS SOFA feed
    try:
        sofa_feed = get_feed(MACOS_SOFA_FEED_URL)
    except ValidationError as e:
        print(f"Error occurred while validating SOFA feed: {e}")
        exit(1)
    except (Timeout, ConnectionError) as e:
        print(f"Network error occurred while attempting to pull the SOFA feed from {MACOS_SOFA_FEED_URL}: {e}")
        exit(1)
    except Exception as e:
        print(f"Error occurred while attempting to pull the SOFA feed: {e}")
        exit(1)

    # Check if we need to update our nudge configuration.
    if cache.last_update_hash == sofa_feed.update_hash and not FORCE_UPDATE:
        print(f"Nudge config already targeting current SOFA feed release {cache.last_update_hash}. Exiting.")
        exit(0)
    else:
        print(f"New SOFA feed release detected, hash {sofa_feed.update_hash}")

    # Retrieve nudge config
    try:
        nudge_config = get_nudge_config(NUDGE_CONFIG_PATH)
    except Exception as e:
        print(f"Error occurred while attempting to retrieve nudge config from {NUDGE_CONFIG_PATH}: {e}")
        exit(1)

    in_blackout, reason = is_within_blackout(nudge_config)

    if in_blackout and not FORCE_UPDATE:
        print(f"Currently within blackout period: {reason}. Exiting.")
        exit(0)

    print("Outside blackout period - safe to proceed")

    # Update our metadata and update the nudge configuration if necessary.
    cache.last_update_hash = sofa_feed.update_hash

    if should_update_config(sofa_feed, nudge_config) or FORCE_UPDATE:
        print("Nudge configuration requires updating")
        update_config(sofa_feed, nudge_config)
        config_updated = True

    # Write changes and update workflow variables
    print(f"Writing changes to {NUDGE_CONFIG_PATH}")
    with open(NUDGE_CONFIG_PATH, "w") as file:
        file.write(nudge_config.model_dump_json(indent=4, exclude_none=True, by_alias=True))

    # Update cache
    print(f"Updating cache")
    with open(CACHE_PATH, "w") as file:
        file.write(cache.model_dump_json())

    print("Determining runtime environment")
    if os.getenv("GITHUB_ACTIONS"):
        print(f"Github environment detected. Setting environment variables.")
        with open(os.environ["GITHUB_ENV"], "a") as env:
            commit_msg: str

            if config_updated:
                commit_msg = f"Update required_minimum_os_version to {nudge_config.os_version_requirements[0].required_minimum_os_version}"

            env_var = f"COMMIT_MSG='{commit_msg}'"
            print(env_var)
            env.write(f"{env_var}\n")

            env_var = f"CONFIG_CHANGED={config_updated}"
            print(env_var)
            env.write(f"{env_var}\n")
    else:
        print(f"Local environment detected. Printing results.")
        print("")
        print(f"SOFA Feed Hash: {cache.last_update_hash}")
        print(f"Config updated: {config_updated}")
        print(f"Targeted version: {nudge_config.os_version_requirements[0].required_minimum_os_version}")
        print(f"Deadline: {nudge_config.os_version_requirements[0].required_installation_date}")

    # Done
    exit(0)


if __name__ == "__main__":
    main()

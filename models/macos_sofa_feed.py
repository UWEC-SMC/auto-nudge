from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class Latest(BaseModel):
    product_version: str = Field(
        ...,
        alias="ProductVersion",
        description="Just the numerical customer-facing version, for example '14.4.1'",
    )
    build: str = Field(
        ...,
        alias="Build",
        description="More-stringent coded version, which can be parsed based on internal release 'train' and major darwin version, etc.",
    )
    release_date: str = Field(
        ...,
        alias="ReleaseDate",
        description="Same UTC timestamp format as above for when this release was considered published",
    )
    expiration_date: str = Field(
        ...,
        alias="ExpirationDate",
        description="Misnomer as not applicable to macOS, but for other OSes marks when 'personalization'/OTA activation process by Apple would no longer be allowed",
    )
    supported_devices: List[str] = Field(
        ...,
        alias="SupportedDevices",
        description="BoardIDs (which are a more-stingent identifier of devices) this release supports",
        min_length=1,
    )
    cves: Dict[str, bool] = Field(
        ...,
        alias="CVEs",
        description="BeautifulSoup extraction of listed CVE's on SecurityInfo page",
    )
    actively_exploited_cves: List[str] = Field(
        ...,
        alias="ActivelyExploitedCVEs",
        description="Convenience listing/array of boolean 'true's from CVEs object above",
    )
    unique_cves_count: int = Field(..., alias="UniqueCVEsCount", description="Count of the above")


class SecurityRelease(BaseModel):
    update_name: str = Field(
        ...,
        alias="UpdateName",
        description="'Full' name of release, for example 'macOS Sonoma 14.4.1'",
    )
    product_version: str = Field(..., alias="ProductVersion", description="Matches above")
    release_date: str = Field(..., alias="ReleaseDate", description="Matches above")
    release_type: str = Field(..., alias="ReleaseType", description="Indicates if an OS update or RSR")
    security_info: str = Field(
        ...,
        alias="SecurityInfo",
        description="Link to 'About the security content of' said release, for example HT214084",
    )
    supported_devices: Optional[List[str]] = Field(
        None,
        alias="SupportedDevices",
        description="Could be missing (min 0) BoardIDs (which are a more-stingent identifier of devices) this release supports",
        min_length=0,
    )
    cves: Dict[str, bool] = Field(
        ...,
        alias="CVEs",
        description="BeautifulSoup extraction of listed CVE's on SecurityInfo page",
    )
    actively_exploited_cves: List[str] = Field(
        ...,
        alias="ActivelyExploitedCVEs",
        description="Convenience listing/array of boolean 'true's from CVEs object above",
    )
    unique_cves_count: int = Field(..., alias="UniqueCVEsCount", description="Count of the above")
    days_since_previous_release: int = Field(
        ...,
        alias="DaysSincePreviousRelease",
        description="timedelta of this release to previous in days",
    )


class SupportedModel(BaseModel):
    model: str = Field(..., alias="Model", description="'Family' name, for example 'MacBook Air'")
    url: str = Field(
        ...,
        alias="URL",
        description="URL considered canonical per model 'family' for parsing OS compatibilty",
    )
    identifiers: Dict[str, str] = Field(..., alias="Identifiers")


class OsVersion(BaseModel):
    os_version: str = Field(..., alias="OSVersion", description="Instance of a macOS Version")
    latest: Latest = Field(
        ...,
        alias="Latest",
        description="Latest release for this OS version, made distinct/'cherry-picked' for convenience",
    )
    security_releases: List[SecurityRelease] = Field(
        ...,
        alias="SecurityReleases",
        description="All OS releases tracked in Apple security releases page, including latest",
        min_length=1,
    )
    supported_models: List[SupportedModel] = Field(
        ...,
        alias="SupportedModels",
        description="Models from a scrape-able KB that confirms OS support, for example HT201862",
    )


class XProtectPayloads(BaseModel):
    com_apple_x_protect_framework_x_protect: str = Field(..., alias="com.apple.XProtectFramework.XProtect")
    com_apple_xprotect_framework_plugin_service: str = Field(..., alias="com.apple.XprotectFramework.PluginService")
    release_date: str = Field(..., alias="ReleaseDate")


class XProtectPlistConfigData(BaseModel):
    com_apple_x_protect: str = Field(..., alias="com.apple.XProtect")
    release_date: str = Field(..., alias="ReleaseDate")


class Model(BaseModel):
    marketing_name: str = Field(..., alias="MarketingName", description="For example 'Mac Pro (Late 2013)'")
    supported_os: List[str] = Field(
        ...,
        alias="SupportedOS",
        description="List of major OS versions supported, in the format name + major version 'macOS Sonoma 14'",
    )
    os_versions: List[int] = Field(..., alias="OSVersions", description="Just major OS numbers in a list")


class Uma(BaseModel):
    title: str = Field(..., description="Name of OS, for example macOS Sonoma")
    version: str = Field(..., description="'Full' numeric version, ")
    build: str = Field(..., description="Matches above")
    apple_slug: str = Field(
        ...,
        description="3 digit, hyphen and ~5 digit way artifacts are ID'd by Apple internally",
    )
    url: str = Field(..., description="URL on Apple's (or Akamai's still?) CDN")


class InstallationApps(BaseModel):
    latest_uma: Uma = Field(
        ...,
        alias="LatestUMA",
        description="Convenience entry for most recent UMA app info",
    )
    all_previous_uma: List[Uma] = Field(
        ...,
        alias="AllPreviousUMA",
        description="List of all older versions, matching the schema described above",
    )


class MacSofaFeed(BaseModel):
    update_hash: str = Field(
        ...,
        alias="UpdateHash",
        description="SHA-256 of the last time the data in the feed was updated",
    )
    os_versions: List[OsVersion] = Field(
        ...,
        alias="OSVersions",
        description="All macOS versions published to date that Apple has included in their security releases page (formerly known as HT201222)",
    )
    x_protect_payloads: XProtectPayloads = Field(
        ...,
        alias="XProtectPayloads",
        description="Entries for each XProtect-relevant version, with most recent release date",
    )
    x_protect_plist_config_data: XProtectPlistConfigData = Field(
        ...,
        alias="XProtectPlistConfigData",
        description="As per support.apple.com/101591, 'Prevents known malware from running'",
    )
    models: Dict[str, Model] = Field(
        ...,
        alias="Models",
        description="Re-presentation of info to help map devices and OS compatibility, with one entry per device",
    )
    installation_apps: InstallationApps = Field(
        ...,
        alias="InstallationApps",
        description="'Universal Mac Assistant' installer info, which put for example 'Install macOS Sonoma.app' in the Applications folder",
    )

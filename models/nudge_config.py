from __future__ import annotations

from datetime import datetime
from typing import List, Optional, Tuple

from pydantic import BaseModel, Field


class OptionalFeatures(BaseModel):
    acceptable_application_bundle_ids: Optional[List[str]] = Field(
        None,
        alias="acceptableApplicationBundleIDs",
        description="The application Bundle ID which Nudge allows without taking focus. (You can specify one or more Bundle ID.)",
    )
    acceptable_assertion_application_names: Optional[List[str]] = Field(
        None,
        alias="acceptableAssertionApplicationNames",
        description="The application names using assertions which Nudge allows without taking focus. (You can specify one or more applications. To find the names please run /usr/bin/pmset -g assertions in terminal while the application is open and running)",
    )
    acceptable_assertion_usage: Optional[bool] = Field(
        None,
        alias="acceptableAssertionUsage",
        description="When enabled, Nudge will not activate or re-activate when assertions are currently set.",
    )
    acceptable_camera_usage: Optional[bool] = Field(
        None,
        alias="acceptableCameraUsage",
        description="When enabled, Nudge will not activate or re-activate when the camera is on.",
    )
    acceptable_update_preparing_usage: Optional[bool] = Field(
        None,
        alias="acceptableUpdatePreparingUsage",
        description="When enabled, Nudge will not activate or re-activate when an update is being downloaded, prepared or staged. (Note: This key is only used with Nudge v2.0 and higher)",
    )
    acceptable_screen_sharing_usage: Optional[bool] = Field(
        None,
        alias="acceptableScreenSharingUsage",
        description="When enabled, Nudge will not activate or re-activate when screen sharing is active.",
    )
    aggressive_user_experience: Optional[bool] = Field(
        None,
        alias="aggressiveUserExperience",
        description="When disabled, Nudge will not hide all non-acceptableApplicationBundleIDs after the requiredInstallationDate or allowedDeferrals.",
    )
    aggressive_user_full_screen_experience: Optional[bool] = Field(
        None,
        alias="aggressiveUserFullScreenExperience",
        description="When disabled, Nudge will not create a blurred background when the user is past the deferral window.",
    )
    asynchronous_software_update: Optional[bool] = Field(
        None,
        alias="asynchronousSoftwareUpdate",
        description="When disabled, Nudge will wait for Software Update to finish downloading (if any) updates before showing the UI.",
    )
    attempt_to_block_application_launches: Optional[bool] = Field(
        None,
        alias="attemptToBlockApplicationLaunches",
        description="When enabled, Nudge will attempt to block application launches after the required installation date. This key must be used in conjunction with blockedApplicationBundleIDs (Note: This key is only used with Nudge v1.1.7 and higher)",
    )
    attempt_to_check_for_supported_device: Optional[bool] = Field(
        None,
        alias="attemptToCheckForSupportedDevice",
        description="When disabled, Nudge will no longer compare the current device against the SOFA feed for the required update. If the device cannot install this update, Nudge will not present the Unsupported UI (Note: This key is only used with Nudge v2.0 and higher)",
    )
    attempt_to_fetch_major_upgrade: Optional[bool] = Field(
        None,
        alias="attemptToFetchMajorUpgrade",
        description="When a major upgrade is required, Nudge will attempt to download it through the softwareupdate binary. (Note: This key is only used with Nudge v1.1 and will not be honored in v1.0.)",
    )
    blocked_application_bundle_ids: Optional[List[str]] = Field(
        None,
        alias="blockedApplicationBundleIDs",
        description="The application Bundle ID which Nudge disallows from launching after the required installation date. (You can specify one or more Bundle ID.)",
    )
    custom_sofa_feed_url: Optional[str] = Field(
        None,
        alias="customSOFAFeedURL",
        description="A url path to use a custom SOFA feed. (Note: This key is only used with Nudge v2.0 and higher)",
    )
    disable_nudge_for_standard_installs: Optional[bool] = Field(
        None,
        alias="disableNudgeForStandardInstalls",
        description="When utilizing a SOFA feed and disableNudgeForStandardInstalls is true, Nudge will only enforce updates with published CVEs. Defaults to false. (Note: This key is only used with Nudge v2.0 and higher)",
    )
    disable_software_update_workflow: Optional[bool] = Field(
        None,
        alias="disableSoftwareUpdateWorkflow",
        description="When disableSoftwareUpdateWorkflow is true, Nudge will not attempt to run the softwareupdate process. Defaults to false.",
    )
    enforce_minor_updates: Optional[bool] = Field(
        None,
        alias="enforceMinorUpdates",
        description="When enabled, Nudge will enforce minor updates. This should likely never be disabled.",
    )
    honor_focus_modes: Optional[bool] = Field(
        None,
        alias="honorFocusModes",
        description="When enabled, Nudge will not activate or re-activate when a user is in DoNotDisturb/Focus status. This feature is expiremental and may not work in all user settings. (Note: This key is only used with Nudge v2.0 and higher)",
    )
    honor_cycle_timers_on_exit: Optional[bool] = Field(
        None,
        alias="honorCycleTimersOnExit",
        description="When enabled, Nudge will honor the current cycle timers when user's press the `Quit` button. (Note: This key is only used with Nudge v2.0 and higher)",
    )
    refresh_sofa_feed_time: Optional[int] = Field(
        None,
        alias="refreshSOFAFeedTime",
        description="The maximum age the cached SOFA feed file can be on disk. When this file age expires, Nudge will re-assess the SOFA feed for updates. Please be mindful of changing this value as there is an associated cost for maintaining the SOFA service. (Note: This key is only used with Nudge v2.0 and higher)",
    )
    terminate_applications_on_launch: Optional[bool] = Field(
        None,
        alias="terminateApplicationsOnLaunch",
        description="When enabled, Nudge will terminate the applications listed in blockedApplicationBundleIDs upon initial launch.",
    )
    utilize_sofa_feed: Optional[bool] = Field(
        None,
        alias="utilizeSOFAFeed",
        description="When enabled, Nudge will utilize the SOFA feed url for update data. (Note: This key is only used with Nudge v2.0 and higher)",
    )


class AboutUpdateUrl(BaseModel):
    field_language: Optional[str] = Field(
        None,
        alias="_language",
        description="The targeted language locale for the user interface. Note: For a list of locales, please run the following command in Terminal: /usr/bin/locale -a",
    )
    about_update_url: Optional[str] = Field(
        None,
        alias="aboutUpdateURL",
        description="The URL for the More Info button. While this accepts a string, it must be a valid URL (http://, https://, file://).",
    )


class UnsupportedUrl(BaseModel):
    field_language: Optional[str] = Field(
        None,
        alias="_language",
        description="The targeted language locale for the user interface. Note: For a list of locales, please run the following command in Terminal: /usr/bin/locale -a",
    )
    unsupported_url: Optional[str] = Field(
        None,
        alias="unsupportedURL",
        description="A single URL, enabling the More Info button URL path when using the unsupported UI. While this accepts a string, it must be a valid URL (http://, https://, file://). Note: If this value is passed with aboutUpdateURLs, the aboutUpdateURLs key will be ignored. (Note: This key is only used with Nudge v2.0 and higher)",
    )


class OsVersionRequirement(BaseModel):
    about_update_url: Optional[str] = Field(
        None,
        alias="aboutUpdateURL",
        description="A single URL, enabling the More Info button URL path. While this accepts a string, it must be a valid URL (http://, https://, file://). Note: If this value is passed with aboutUpdateURLs, the aboutUpdateURLs key will be ignored.",
    )
    about_update_urls: Optional[List[AboutUpdateUrl]] = Field(
        None,
        alias="aboutUpdateURLs",
        description="The aboutUpdateURL - per country localization.",
        title="aboutUpdateURLs",
    )
    action_button_path: Optional[str] = Field(
        None,
        alias="actionButtonPath",
        description="A path to a URI for opening alternative actions, like Jamf self service items.",
    )
    actively_exploited_cves_major_upgrade_sla: Optional[int] = Field(
        None,
        alias="activelyExploitedCVEsMajorUpgradeSLA",
        description="When a major upgrade is under active exploit, this is the amount of days a user has to install the update. (Note: This key is only used with Nudge v2.0 and higher)",
    )
    actively_exploited_cves_minor_update_sla: Optional[int] = Field(
        None,
        alias="activelyExploitedCVEsMinorUpdateSLA",
        description="When a minor update is under active exploit, this is the amount of days a user has to install the update. (Note: This key is only used with Nudge v2.0 and higher)",
    )
    major_upgrade_app_path: Optional[str] = Field(
        None,
        alias="majorUpgradeAppPath",
        description="The app path for a major upgrade. (Note: Requires Nudge v1.0.1 or higher.)",
    )
    minor_version_recalculation_threshold: Optional[int] = Field(
        None,
        alias="minorVersionRecalculationThreshold",
        description="The amount of minor versions a device can be behind before the requiredInstallationDate is recalculated against a previous update. (Note: This key is only used with Nudge v2.0.5 and higher)",
    )
    non_actively_exploited_cves_major_upgrade_sla: Optional[int] = Field(
        None,
        alias="nonActivelyExploitedCVEsMajorUpgradeSLA",
        description="When a major upgrade is not under active exploit but contains CVEs, this is the amount of days a user has to install the update. (Note: This key is only used with Nudge v2.0 and higher)",
    )
    non_actively_exploited_cves_minor_update_sla: Optional[int] = Field(
        None,
        alias="nonActivelyExploitedCVEsMinorUpdateSLA",
        description="When a minor update is not under active exploit but contains CVEs, this is the amount of days a user has to install the update. (Note: This key is only used with Nudge v2.0 and higher)",
    )
    required_installation_date: Optional[str] = Field(
        None,
        alias="requiredInstallationDate",
        description="The required installation date for Nudge to enforce the required operating system version. You must follow a standard date string as YYYY-MM-DDTHH:MM:SSZ - Example: 2021-09-15T00:00:00Z",
    )
    required_minimum_os_version: Optional[str] = Field(
        None,
        alias="requiredMinimumOSVersion",
        description="The required minimum operating system version. Note: When passing versions such as `11.2.0`, it will be normalized to `11.2`. It is recommended to remove the trailing zero from the version number.",
    )
    standard_major_upgrade_sla: Optional[int] = Field(
        None,
        alias="standardMajorUpgradeSLA",
        description="When a major upgrade has no known CVEs, this is the amount of days a user has to install the update. (Note: This key is only used with Nudge v2.0 and higher)",
    )
    standard_minor_update_sla: Optional[int] = Field(
        None,
        alias="standardMinorUpdateSLA",
        description="When a minor update has no known CVEs, this is the amount of days a user has to install the update. (Note: This key is only used with Nudge v2.0 and higher)",
    )
    targeted_os_versions_rule: Optional[str] = Field(
        None,
        alias="targetedOSVersionsRule",
        description='The OS string rule for targeting Nudge events. You can target with "default", the full OS version (example: "11.5.1"). or the major OS version (example: "11"). (Note: This key is only used with Nudge v1.1 and higher)',
    )
    unsupported_url: Optional[str] = Field(
        None,
        alias="unsupportedURL",
        description="A single URL, enabling the More Info button URL path when using the unsupported UI. While this accepts a string, it must be a valid URL (http://, https://, file://). Note: If this value is passed with aboutUpdateURLs, the aboutUpdateURLs key will be ignored. (Note: This key is only used with Nudge v2.0 and higher)",
    )
    unsupported_urls: Optional[List[UnsupportedUrl]] = Field(
        None,
        alias="unsupportedURLs",
        description="The unsupportedURL - per country localization.",
        title="unsupportedURLs",
    )


class UserExperience(BaseModel):
    allow_grace_periods: Optional[bool] = Field(
        None,
        alias="allowGracePeriods",
        description="Allows a device to modify the requiredInstallationDate logic and launch behavior. Useful for new device provisioning.",
    )
    allow_later_deferral_button: Optional[bool] = Field(
        None,
        alias="allowLaterDeferralButton",
        description="Allows the user to press the `Later` button through the custom deferrals UI",
    )
    allow_movable_window: Optional[bool] = Field(
        None,
        alias="allowMovableWindow",
        description="Allows the user to move the Nudge window. (Note: This key is only used with Nudge v2.0 and higher)",
    )
    allow_user_quit_deferrals: Optional[bool] = Field(
        None,
        alias="allowUserQuitDeferrals",
        description="Allows the user to specify when they will next be prompted by Nudge. (Set to `False` to maintain v1.0.0 behavior.) When using this feature, Nudge will no longer adhere to your LaunchAgent logic as the user is specifying their own execution time for the next Nudge event.(See: `~/Library/Preferences/com.github.macadmins.Nudge.plist`.)",
    )
    allowed_deferrals: Optional[int] = Field(
        None,
        alias="allowedDeferrals",
        description='The number of times a user can defer Nudge (change it from the currently active window) before the "aggressive user experience" is enabled.',
    )
    allowed_deferrals_until_forced_secondary_quit_button: Optional[int] = Field(
        None,
        alias="allowedDeferralsUntilForcedSecondaryQuitButton",
        description="The number of times a user can defer Nudge (change it from the currently active window) before both quit buttons need to be actioned.",
    )
    approaching_refresh_cycle: Optional[int] = Field(
        None,
        alias="approachingRefreshCycle",
        description="The amount of time in seconds Nudge will use as a timer to refresh the user interface if it is not the currently active window. This key is directly tied to its partner key `approachingWindowTime` to know when to trigger this timer.",
    )
    approaching_window_time: Optional[int] = Field(
        None,
        alias="approachingWindowTime",
        description='The amount of time in hours Nudge will use to determine that the `requiredInstallationDate` is "approaching".',
    )
    calendar_deferral_unit: Optional[str] = Field(
        None,
        alias="calendarDeferralUnit",
        description="Utilize the approachingWindowTime or imminentWindowTime for calendar deferrals.",
    )
    elapsed_refresh_cycle: Optional[int] = Field(
        None,
        alias="elapsedRefreshCycle",
        description="The amount of time in seconds Nudge will use as a timer to refresh the user interface if it is not the currently active window. This key is triggered once the `requiredInstallationDate` has expired.",
    )
    grace_period_install_delay: Optional[int] = Field(
        None,
        alias="gracePeriodInstallDelay",
        description="The amount of time in hours Nudge will extend the requiredInstallationDate for newly provisioned devices.",
    )
    grace_period_launch_delay: Optional[int] = Field(
        None,
        alias="gracePeriodLaunchDelay",
        description="The amount of time in hours Nudge will bypass launching for newly provided devices.",
    )
    grace_period_path: Optional[str] = Field(
        None,
        alias="gracePeriodPath",
        description="The path of the file Nudge will read and assess for allowGracePeriods.",
    )
    imminent_refresh_cycle: Optional[int] = Field(
        None,
        alias="imminentRefreshCycle",
        description="The amount of time in seconds Nudge will use as a timer to refresh the user interface if it is not the currently active window. This key is directly tied to its partner key `imminentWindowTime` to know when to trigger this timer.",
    )
    imminent_window_time: Optional[int] = Field(
        None,
        alias="imminentWindowTime",
        description='The amount of time in hours Nudge will use to determine that the `requiredInstallationDate` is "imminent".',
    )
    initial_refresh_cycle: Optional[int] = Field(
        None,
        alias="initialRefreshCycle",
        description="The amount of time in seconds Nudge will use as a timer to refresh the user interface if it is not the currently active window. This key is triggered for all Nudge launches until the `approachingWindowTime` has been passed.",
    )
    launch_agent_identifier: Optional[str] = Field(
        None,
        alias="launchAgentIdentifier",
        description="The identifier of the Nudge LaunchAgent. Only set this if you use a custom identifier",
    )
    load_launch_agent: Optional[bool] = Field(
        None,
        alias="loadLaunchAgent",
        description="Loads the Nudge LaunchAgent using macOS Ventura's SMAppService API (macOS 13+ required).",
    )
    max_random_delay_in_seconds: Optional[int] = Field(
        None,
        alias="maxRandomDelayInSeconds",
        description="The maximum amount of delay Nudge will utilize before launching the UI. This is useful if you do not want your users to all receive the Nudge prompt at the exact time of the LaunchAgent. Note: This functionality only applies when also enabling `randomDelay`.",
    )
    no_timers: Optional[bool] = Field(
        None,
        alias="noTimers",
        description="This will disable all functionality related to the `userExperience` preference domain.",
    )
    nudge_major_upgrade_event_launch_delay: Optional[int] = Field(
        None,
        alias="nudgeMajorUpgradeEventLaunchDelay",
        description="When a new major upgrade is posted to the SOFA feed, this can artificially delay the SOFA nudge events by x amount of days. (Note: This key is only used with Nudge v2.0 and higher)",
    )
    nudge_minor_update_event_launch_delay: Optional[int] = Field(
        None,
        alias="nudgeMinorUpdateEventLaunchDelay",
        description="When a new minor update is posted to the SOFA feed, this can artificially delay the SOFA nudge events by x amount of days. (Note: This key is only used with Nudge v2.0 and higher)",
    )
    nudge_refresh_cycle: Optional[int] = Field(
        None,
        alias="nudgeRefreshCycle",
        description="The amount of time in seconds Nudge will use as its core timer to refresh all the core code paths. Note: While you can lower this setting, it could make Nudge too aggressive. Be mindful of decreasing this value.",
    )
    random_delay: Optional[bool] = Field(
        None,
        alias="randomDelay",
        description="Enables an initial delay Nudge before launching the UI. This is useful if you do not want your users to all receive the Nudge prompt at the exact time of the LaunchAgent.",
    )


class UpdateElement(BaseModel):
    field_language: Optional[str] = Field(
        None,
        alias="_language",
        description="The targeted language locale for the user interface. Note: For a list of locales, please run the following command in Terminal: /usr/bin/locale -a",
    )
    action_button_text: Optional[str] = Field(
        None,
        alias="actionButtonText",
        description='Modifies the actionButton, also known as the "Update Device" button.',
    )
    action_button_text_unsupported: Optional[str] = Field(
        None,
        alias="actionButtonTextUnsupported",
        description='Modifies the primaryQuitButton, also known as the "Update Device" button when using the Unsupported UI. (Note: This key is only used with Nudge v2.0 and higher)',
    )
    application_terminated_title_text: Optional[str] = Field(
        None,
        alias="applicationTerminatedTitleText",
        description="Modifies the terminated application notification title. (Note: This key is only used with Nudge v2.0 and higher)",
    )
    application_terminated_body_text: Optional[str] = Field(
        None,
        alias="applicationTerminatedBodyText",
        description="Modifies the terminated application notification body. (Note: This key is only used with Nudge v2.0 and higher)",
    )
    custom_deferral_button_text: Optional[str] = Field(
        None,
        alias="customDeferralButtonText",
        description='Modifies the customDeferralButtonText, also known as the "Custom" button.',
    )
    custom_deferral_dropdown_text: Optional[str] = Field(
        None,
        alias="customDeferralDropdownText",
        description='customDeferralDropdownText, also known as the "Defer" button.',
    )
    information_button_text: Optional[str] = Field(
        None,
        alias="informationButtonText",
        description='Modifies the informationButton, also known as the "More Info" button.',
    )
    main_content_header: Optional[str] = Field(
        None,
        alias="mainContentHeader",
        description='Modifies the mainContentHeader. This is the "Your device will restart during this update" text.',
    )
    main_content_header_unsupported: Optional[str] = Field(
        None,
        alias="mainContentHeaderUnsupported",
        description='Modifies the mainContentHeader. This is the "Your device is no longer capable of receiving critical security updates" text when using the Unsupported UI. (Note: This key is only used with Nudge v2.0 and higher)',
    )
    main_content_note: Optional[str] = Field(
        None,
        alias="mainContentNote",
        description='Modifies the mainContentNote. This is the "Important Notes" text.',
    )
    main_content_note_unsupported: Optional[str] = Field(
        None,
        alias="mainContentNoteUnsupported",
        description='Modifies the mainContentNote. This is the "Important Notes" text when using the Unsupported UI. (Note: This key is only used with Nudge v2.0 and higher)',
    )
    main_content_sub_header: Optional[str] = Field(
        None,
        alias="mainContentSubHeader",
        description='Modifies the mainContentSubHeader. This is the "Updates can take around 30 minutes to complete" text.',
    )
    main_content_sub_header_unsupported: Optional[str] = Field(
        None,
        alias="mainContentSubHeaderUnsupported",
        description='Modifies the mainContentSubHeader. This is the "Please work with your local IT team to obtain a replacement device" text when using the Unsupported UI. (Note: This key is only used with Nudge v2.0 and higher)',
    )
    main_content_text: Optional[str] = Field(
        None,
        alias="mainContentText",
        description='Modifies the `mainContentText`. This is the "A fully up-to-date device is required to ensure that IT can your accurately protect your device." text. (See the Wiki for information on adding line breaks.)',
    )
    main_content_text_unsupported: Optional[str] = Field(
        None,
        alias="mainContentTextUnsupported",
        description='Modifies the `mainContentText`. This is the "A fully up-to-date device is required to ensure that IT can your accurately protect your device." text when using the Unsupported UI. See the Wiki for information on adding line breaks. (Note: This key is only used with Nudge v2.0 and higher)',
    )
    main_header: Optional[str] = Field(
        None,
        alias="mainHeader",
        description='Modifies the `mainHeader`. This is the "Your device requires a security update" text.',
    )
    main_header_unsupported: Optional[str] = Field(
        None,
        alias="mainHeaderUnsupported",
        description='Modifies the `mainHeader`. This is the "Your device requires a security update" text when using the Unsupported UI. (Note: This key is only used with Nudge v2.0 and higher)',
    )
    one_day_deferral_button_text: Optional[str] = Field(
        None,
        alias="oneDayDeferralButtonText",
        description='Modifies the oneDayDeferralButtonText, also known as the "One Day" button.',
    )
    one_hour_deferral_button_text: Optional[str] = Field(
        None,
        alias="oneHourDeferralButtonText",
        description='Modifies the oneHourDeferralButtonText, also known as the "One Hour" button.',
    )
    primary_quit_button_text: Optional[str] = Field(
        None,
        alias="primaryQuitButtonText",
        description='Modifies the `primaryQuitButton`, also known as the "Later" button.',
    )
    screen_shot_alt_text: Optional[str] = Field(
        None,
        alias="screenShotAltText",
        description="Modifies the accessible hover over on screen shots.",
    )
    secondary_quit_button_text: Optional[str] = Field(
        None,
        alias="secondaryQuitButtonText",
        description='Modifies the `secondaryQuitButton`, also known as the "I understand" button.',
    )
    sub_header: Optional[str] = Field(
        None,
        alias="subHeader",
        description='Modifies the `subHeader`. This is the "A friendly reminder from your local IT team" text.',
    )
    sub_header_unsupported: Optional[str] = Field(
        None,
        alias="subHeaderUnsupported",
        description='Modifies the `subHeader`. This is the "A friendly reminder from your local IT team" text when using the Unsupported UI. (Note: This key is only used with Nudge v2.0 and higher)',
    )


class UserInterface(BaseModel):
    action_button_path: Optional[str] = Field(
        None,
        alias="actionButtonPath",
        description="A path to a URI for opening alternative actions, like Jamf self service items.",
    )
    application_terminated_notification_image_path: Optional[str] = Field(
        None,
        alias="applicationTerminatedNotificationImagePath",
        description="A local image path for the notification event when Nudge terminates and application. (Note: This key is only used with Nudge v2.0 and higher)",
    )
    fallback_language: Optional[str] = Field(
        None,
        alias="fallbackLanguage",
        description="The language to revert to if no localizations are available for the device's current language.",
    )
    force_fallback_language: Optional[bool] = Field(
        None,
        alias="forceFallbackLanguage",
        description="Force the custom localizations to the value of `fallbackLanguage`.",
    )
    force_screen_shot_icon: Optional[bool] = Field(
        None,
        alias="forceScreenShotIcon",
        description="Force the built-in ScreenShot icon to render in the UI if a ScreenShot path is not passed.",
    )
    icon_dark_path: Optional[str] = Field(
        None,
        alias="iconDarkPath",
        description="A path to a local jpg, png, icns that contains the icon for dark mode. This will replace the Apple logo on the left side of Nudge.",
    )
    icon_light_path: Optional[str] = Field(
        None,
        alias="iconLightPath",
        description="A path to a local jpg, png, icns that contains the icon for light mode. This will replace the Apple logo on the left side of Nudge.",
    )
    required_installation_display_format: Optional[str] = Field(
        None,
        alias="requiredInstallationDisplayFormat",
        description="When utilizing showRequiredDate, set a custom display format. Be aware that the format you desire may not look good on the UI. (Note: This key is only used with Nudge v2.0 and higher)",
    )
    screen_shot_dark_path: Optional[str] = Field(
        None,
        alias="screenShotDarkPath",
        description="A path to a local jpg, png, icns that contains the screen shot for dark mode. This will replace the Big Sur logo on the lower right side of Nudge.",
    )
    screen_shot_light_path: Optional[str] = Field(
        None,
        alias="screenShotLightPath",
        description="A path to a local jpg, png, icns that contains the screen shot for light mode. This will replace the Big Sur logo on the lower right side of Nudge.",
    )
    show_actively_exploited_cves: Optional[bool] = Field(
        None,
        alias="showActivelyExploitedCVEs",
        description="When disabled, Nudge will not show the Actively Exploited CVEs in the left sidebar. (Note: This key is only used with Nudge v2.0 and higher)",
    )
    show_deferral_count: Optional[bool] = Field(
        None,
        alias="showDeferralCount",
        description="Enables or disables the deferral count of the current Nudge event.",
    )
    show_days_remaining_to_update: Optional[bool] = Field(
        None,
        alias="showDaysRemainingToUpdate",
        description="When disabled, Nudge will not show the `Days Remaining To Update:` item on the left side of the UI. (Note: This key is only used with Nudge v2.0 and higher)",
    )
    show_required_date: Optional[bool] = Field(
        None,
        alias="showRequiredDate",
        description="When enabled, Nudge will also show the requiredInstallationDate as string formatted date. (Note: This key is only used with Nudge v2.0 and higher)",
    )
    simple_mode: Optional[bool] = Field(
        None,
        alias="simpleMode",
        description="Enables Nudge to launch in the simplified user experience.",
    )
    single_quit_button: Optional[bool] = Field(
        None,
        alias="singleQuitButton",
        description="Only display one quit button regardless of proximity to the due date.",
    )
    update_elements: Optional[List[UpdateElement]] = Field(
        None,
        alias="updateElements",
        description="The individual buttons and text elements that can be customized for your employer's needs. This includes per country localization.",
        title="updateElements",
    )


class BlackoutPeriod(BaseModel):
    start: str = Field(..., description="The first day of the blackout, in MM/DD format.")
    end: str = Field(..., description="The last day of the blackout, in MM/DD format.")
    comment: str = Field(..., description="The reason for the blackout.")

    def is_in_blackout(self, date: datetime) -> bool:
        """
        Check if today falls between two month-day pairs, regardless of the year.

        Args:
            date (datetime): Date to check if is within the given blackout period.

        Returns:
            bool: True if within the range, False otherwise.
        """
        compare_date = (date.month, date.day)
        start_month_day = tuple(map(int, self.start.split("/")))
        end_month_day = tuple(map(int, self.end.split("/")))

        # Handle ranges that wrap around the new year (e.g., Dec 15 - Jan 10)
        if start_month_day <= end_month_day:
            return start_month_day <= compare_date <= end_month_day
        else:
            return compare_date >= start_month_day or compare_date <= end_month_day


class NudgeMetadata(BaseModel):
    last_update_hash: str = Field(
        None,
        description="The update hash of the last processed SOFA feed update.",
    )
    blackout_periods: List[BlackoutPeriod] = Field(
        None, description="A collection start & end dates for when the nudge config should NOT be updated."
    )
    note_template: str = Field(
        None,
        description="Text template to be used when updating mainContentNote. Placeholders should be in {} format.",
        examples=["⚠️  Updates must be installed prior to {install_deadline}  ⚠️"],
    )


class NudgeConfig(BaseModel):
    optional_features: Optional[OptionalFeatures] = Field(
        None,
        alias="optionalFeatures",
        description="All optional features to enhance and customize the Nudge experience for your employer's needs.",
        title="optionalFeatures",
    )
    os_version_requirements: Optional[List[OsVersionRequirement]] = Field(
        None,
        alias="osVersionRequirements",
        description="The required components necessary to enforce an Operating System version through Nudge. Specify one array to enforce a single Operating System version across all machines or specify multiple arrays for specific enforcements.",
        title="osVersionRequirements",
    )
    user_experience: Optional[UserExperience] = Field(
        None,
        alias="userExperience",
        description="All features related to how Nudge refreshes and defines the user experience",
        title="userExperience",
    )
    user_interface: Optional[UserInterface] = Field(
        None,
        alias="userInterface",
        description="All features related to how Nudge defines the user interface.",
        title="userInterface",
    )
    metadata: Optional[NudgeMetadata] = Field(None, description="Metadata for automated nudge config generation.")

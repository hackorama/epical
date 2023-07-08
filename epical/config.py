# 
# See configuration file details in ../docs/config.md
#
PROJECT_NAME: str = "ePiCal"
PROJECT_VERSION: str = "0.1.0"

DEBUG: bool = False
LOG_FILE: str = "~/.epical/epical.log"

GRID_LIB_DIR: str = "../grid/lib"
EPD_LIB_DIR: str = "../epd/lib"

DATA_RETRY_MAX_COUNT: int = 3
DATA_RETRY_DELAY_SECS: int = 5

WEATHER_CITY: str = "SanJose"
SCORE_TEAM_ID: str = "SF"
EVENTS_FILE: str = "resources/events.json"

# External server for control checks (check_run_and_halt.sh) and data (image, battery) updates
# Control check url protocol ../web/server/static/README.md
CONTROL_SERVER_URL: str = "http://home.local.net:8888"

# Daily rotation and event day specific photos, details in ../docs/photos.md
PHOTO_FILE_OR_FOLDER: str = "resources/photos"
EVENT_PHOTO_FILE_OR_FOLDER: str = "resources/event_photos"
PHOTO_BOUNDING_BOX_WIDTH: int = 680
PHOTO_BOUNDING_BOX_HEIGHT: int = 500

SCREEN_W: int = 1304
SCREEN_H: int = 984
SCREEN_BORDER: int = 20
SCREEN_ROTATE: bool = True
SCREEN_STATUS_MARGIN: int = 30

FONT_TTF: str = "resources/fonts/font.ttf"
FONT_BOLD_TTF: str = "resources/fonts/bold.ttf"
FONT_LIGHT_TTF: str = "resources/fonts/light.ttf"
FONT_THIN_TTF: str = "resources/fonts/thin.ttf"
FONT_EMOJI_TTF: str = "resources/fonts/emoji.ttf"
FONT_SIZE: int = 40

API_TIMEOUT_SECS: int = 10

# Optional Pi Zero uptimed urecords data file for testing
POWER_OPTIONAL_UP_RECORDS_FILE: str = "~/.epical/uprecords.txt"
# Required track last battery full charge date
POWER_REQD_BATTERY_FILE: str = "~/.epical/battery"
# Battery full charge capacity and self discharge factor
POWER_BATTERY_MILLI_AMP_HOUR: int = 5000
POWER_BATTERY_VOLTS: int = 5
POWER_BATTERY_EFFICIENCY_PERCENT: int = 85
POWER_BATTERY_MONTHLY_SELF_DISCHARGE_PERCENT: int = 10
# Pi Zero average power usage
POWER_DEVICE_VOLTS: int = 5
POWER_DEVICE_MILLI_AMP_HOUR: int = 180
# Screen refresh additional power usage on top of Pi Zero average
POWER_DISPLAY_REFRESH_MILLI_WATT: int = 83
POWER_DISPLAY_REFRESH_VOLTS: int = 3
POWER_DISPLAY_REFRESH_TIME_SECS: int = 120

# Prefer faster mono image gen over more accurate image gen
IMAGE_GEN_PREFER_SPEED_OVER_ACCURACY: bool = True

# Do not clear screen for every screen refresh
# Use uprecords to count each boot as a refresh
# or estimate one refresh per day using the day of month
# Set to 1 to clear for every refresh
# Set to x to clear after x screen refresh
# Set to 0 to never clear
CLEAR_SCREEN_AFTER_REFRESH_COUNT: int = 0

# Export screen image and logs to an external server
UPLOAD_ENABLED: bool = False
UPLOAD_LOGS_URL: str = "http://home.local.net:8888/upload/logs"
UPLOAD_SCREEN_URL: str = "http://home.local.net:8888/upload/screen"

# This is an example of a custom widget for indian malayalam calendar
MAL_DATE_ENABLED: bool = False
MAL_DATE_API_URL: str = "http://home.local.net/kollavarsham"
MAL_FONT_TTF: str = "resources/fonts/malayalam.ttf"

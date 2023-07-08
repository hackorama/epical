import calendar
import datetime
import json
import os
import random
import time
from calendar import Calendar
from typing import Any, Dict, List, Optional, Tuple

import config
import pytz
import requests
from util import abs_relative_path, log

from .score_data import ScoreData
from .weather_data import WeatherData


class CalData:
    def __init__(self):
        self.weather = None
        self.scores = []
        self.retry_update()

    def retry_update(self):
        retries = 0
        while (
            retries < config.DATA_RETRY_MAX_COUNT
            and not self.weather
            or not self.scores
        ):
            if retries:
                log.warning(
                    f"Data fetch failed, retrying after {config.DATA_RETRY_DELAY_SECS} seconds ..."
                )
                time.sleep(config.DATA_RETRY_DELAY_SECS)
            retries += 1
            log.info(f"Data fetch {retries}/{config.DATA_RETRY_MAX_COUNT}")
            self.update()

    def update(self):
        try:
            if not self.scores:
                self.scores = ScoreData.get_scores()
        except Exception as error:
            log.error(f"Score data fetch failed: {error}")
        try:
            if not self.weather:
                self.weather = WeatherData(config.WEATHER_CITY).get_data()
        except Exception as error:
            log.error(f"Weather data fetch failed: {error}")

    @staticmethod
    def check_remote_photo(extension) -> Optional[bytes]:
        try:
            response = requests.get(
                f"{config.CONTROL_SERVER_URL}/photo.{extension}", stream=True, timeout=5
            )
            if response.ok:
                return response.raw
        except Exception as expected_error:
            log.debug(f"Image check for {extension}: {expected_error}")
        return None

    @staticmethod
    def get_remote_photo() -> Tuple[Optional[bytes], Optional[str]]:
        image_raw_bytes = CalData.check_remote_photo("png")
        if image_raw_bytes:
            return image_raw_bytes, "photo.png"
        image_raw_bytes = CalData.check_remote_photo("bmp")
        if image_raw_bytes:
            return image_raw_bytes, "photo.bmp"
        image_raw_bytes = CalData.check_remote_photo("jpg")
        if image_raw_bytes:
            return image_raw_bytes, "photo.jpg"
        image_raw_bytes = CalData.check_remote_photo("jpeg")
        if image_raw_bytes:
            return image_raw_bytes, "photo.jpeg"
        return None, None

    @staticmethod
    def check_event_photo(extension) -> Optional[str]:
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day
        file_name = os.path.join(f"{month}_{day}.{extension}")
        event_photo_path = os.path.join(
            abs_relative_path(config.EVENT_PHOTO_FILE_OR_FOLDER), file_name
        )
        if os.path.exists(event_photo_path):
            return event_photo_path
        return None

    @staticmethod
    def get_event_photo() -> Optional[str]:
        if os.path.isdir(abs_relative_path(config.EVENT_PHOTO_FILE_OR_FOLDER)):
            event_photo = CalData.check_event_photo("png")
            if event_photo:
                return event_photo
            event_photo = CalData.check_event_photo("bmp")
            if event_photo:
                return event_photo
            event_photo = CalData.check_event_photo("jpeg")
            if event_photo:
                return event_photo
            event_photo = CalData.check_event_photo("jpg")
            if event_photo:
                return event_photo
        return None

    @staticmethod
    def check_override_photo(name: str) -> Optional[str]:
        abs_photo_path = abs_relative_path(config.PHOTO_FILE_OR_FOLDER)
        override_name = os.path.join(abs_photo_path, name)
        if os.path.exists(override_name):
            return override_name
        override_name = os.path.join(abs_photo_path, name.lower())
        if os.path.exists(override_name):
            return override_name
        override_name = os.path.join(abs_photo_path, name.upper())
        if os.path.exists(override_name):
            return override_name
        return None

    @staticmethod
    def check_override_photos() -> Optional[str]:
        override_photo_path = CalData.check_override_photo("photo.jpeg")
        if override_photo_path:
            return override_photo_path
        override_photo_path = CalData.check_override_photo("photo.jpg")
        if override_photo_path:
            return override_photo_path
        override_photo_path = CalData.check_override_photo("photo.png")
        if override_photo_path:
            return override_photo_path
        override_photo_path = CalData.check_override_photo("photo.bmp")
        if override_photo_path:
            return override_photo_path
        return None

    @staticmethod
    def select_photo() -> Optional[str]:
        override_photo_path = CalData.check_override_photos()
        if override_photo_path:
            log.info(f"Found override photo {override_photo_path}")
            return override_photo_path

        abs_photo_path = abs_relative_path(config.PHOTO_FILE_OR_FOLDER)
        if os.listdir(abs_photo_path):
            random.seed(os.urandom(10))
            selected = random.choice(os.listdir(abs_photo_path))
            return os.path.join(abs_photo_path, selected)
        log.error(f"No files in photo folder: {abs_photo_path}")
        return None

    @staticmethod
    def get_photo() -> Optional[str]:
        event_photo = CalData.get_event_photo()
        if event_photo:
            return event_photo
        abs_photo_path = abs_relative_path(config.PHOTO_FILE_OR_FOLDER)
        if os.path.isfile(abs_photo_path):
            return abs_photo_path
        if os.path.isdir(abs_photo_path):
            return CalData.select_photo()
        log.error(f"Invalid photos path: {abs_photo_path}")
        return None

    @staticmethod
    def get_events(month: int) -> Dict[Any, Any]:
        try:
            with open(
                abs_relative_path(config.EVENTS_FILE), "r", encoding="UTF-8"
            ) as file:
                events = json.load(file)
            return events.get(str(month), {})
        except Exception as error:
            print(
                f"ERROR: Failed reading events from '{abs_relative_path(config.EVENTS_FILE)}', got error: {error}"
            )
        return {}

    def get_weather(self) -> Optional[List[List[Any]]]:
        return self.weather

    def get_scores(self) -> Optional[List[Any]]:
        return self.scores

    @staticmethod
    def get_score_logo() -> Tuple[str, int, int]:
        return ScoreData.get_score_logo()

    @staticmethod
    def get_month() -> str:
        return datetime.datetime.now().strftime("%B")

    @staticmethod
    def get_year() -> str:
        return datetime.datetime.now().strftime("%Y")

    @staticmethod
    def get_malayalam_date() -> str:
        try:
            if config.MAL_DATE_API_URL:
                r = requests.get(
                    config.MAL_DATE_API_URL, timeout=config.API_TIMEOUT_SECS
                )
                return r.text.strip().strip('"')
            return CalData.build_malayalam_date()
        except Exception as error:
            log.error(f"Failed getting malayalam date: {error}")
        return ""

    @staticmethod
    def build_malayalam_date() -> str:
        # conditional import since jsii requires node binary
        import kollavarsham

        now = pytz.utc.localize(datetime.datetime.utcnow())
        kv = kollavarsham.Kollavarsham(
            latitude=10, longitude=76.2, system="SuryaSiddhanta"
        )
        today = kv.from_gregorian_date(date=now)
        # The malayalam strings returned for ml_masa_name and naksatra.ml_malayalam
        # does not render correctly for complex ligatures.
        # Requires libraqm installed before installing Pillow/PIL, details in pillow.md
        return f"{today.year} {today.ml_masa_name} {today.date} {today.naksatra.ml_malayalam}"

    def get_cal(self) -> List[List[Any]]:
        cal = Calendar()
        cal.setfirstweekday(calendar.SUNDAY)
        month: List[Any] = []
        month_number = int(datetime.datetime.now().strftime("%m"))
        events = self.get_events(month_number)
        year = int(datetime.datetime.now().strftime("%Y"))

        for week in cal.monthdatescalendar(year, month_number):
            month.append([])
            for day in week:
                month[len(month) - 1].append(
                    {
                        "day": day.day,
                        "event": events.get(str(day.day)),
                        "current_month": day.month == month_number,
                    }
                )
        return month

from datetime import datetime
from typing import Any, List, Optional

import config
import requests
from util import log


class WeatherData:
    API_ENDPOINT = "http://wttr.in/{location}?format=j1"

    WEATHER_EMOJI = {
        "NEW_MOON": "🌑",
        "WAXING_CRESCENT": "🌒",
        "FIRST_QUARTER": "🌓",
        "WAXING_GIBBOUS": "🌔",
        "FULL_MOON": "🌕",
        "WANING_GIBBOUS": "🌖",
        "LAST_QUARTER": "🌗",
        "WANING_CRESCENT": "🌘",
        "CLOUDY": "☁️",
        "FOG": "🌫",
        "HEAVY_RAIN": "🌧",
        "HEAVY_SHOWERS": "🌧",
        "HEAVY_SNOW": "❄️",
        "HEAVY_SNOW_SHOWERS": "❄️",
        "LIGHT_RAIN": "🌦",
        "LIGHT_SHOWERS": "🌦",
        "LIGHT_SLEET": "🌧",
        "LIGHT_SLEET_SHOWERS": "🌧",
        "LIGHT_SNOW": "🌨",
        "LIGHT_SNOW_SHOWERS": "🌨",
        "MIST": "🌫",
        "OVERCAST": "🌫",
        "PARTLY_CLOUDY": "⛅️",
        "SUNNY": "☀️",
        "THUNDERY_HEAVY_RAIN": "🌩",
        "THUNDERY_SHOWERS": "⛈",
        "THUNDERY_SNOW_SHOWERS": "⛈",
        "VERY_CLOUDY": "☁️",
        "CLEAR": "✨",
    }

    WEEK_DAY = ["M", "T", "W", "T", "F", "S", "S"]

    def __init__(self, location: str):
        self._location = location
        self._data = self.update()

    def update(self) -> Any:
        try:
            r = requests.get(
                WeatherData.API_ENDPOINT.format(location=self._location),
                timeout=config.API_TIMEOUT_SECS,
            )
            return r.json()
        except Exception as error:
            log.error(f"ERROR: Weather API failed: {error}")
        return None

    def has_data(self) -> bool:
        return self._data

    @staticmethod
    def get_weather_icon(name: str) -> str:
        key = str(name).strip().upper().replace(" ", "_")
        return WeatherData.WEATHER_EMOJI.get(key, " ").strip()

    @staticmethod
    def get_week_day_char(days_after_today: int = 0) -> str:
        today = datetime.now().date()
        today_week_day = int(today.strftime("%w"))
        week_index = today_week_day - 1 + days_after_today
        if week_index > 6:
            week_index = week_index - 7
        return WeatherData.WEEK_DAY[week_index]

    def get_data(self) -> Optional[List]:
        data_ = None
        if not self.has_data():
            return data_
        try:
            data_ = []
            for i, day in enumerate(self._data["weather"]):
                conditions = []
                temperatures = []
                conditions.append(
                    self.get_weather_icon(day["astronomy"][0]["moon_phase"])
                )
                week_day = WeatherData.get_week_day_char(i)
                temperatures.append(week_day)
                for hour in day["hourly"]:
                    conditions.append(
                        self.get_weather_icon(hour["weatherDesc"][0]["value"])
                    )
                    temperatures.append(f"{hour['tempF']}")
                data_.append(conditions)
                data_.append(temperatures)
        except Exception as error:
            log.error(f"Failed in weather data processing: {error}")
        return data_

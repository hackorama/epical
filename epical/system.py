import os
from http import HTTPStatus
from typing import Optional, Tuple

import config
import requests
from data.battery import Battery
from palette import Palette
from PIL import Image, ImageDraw, ImageFont
from util import draw_overlay_text, log


class System:
    battery = Battery()

    def __init__(self, canvas: Image.Image):
        self._canvas = canvas
        self._width, self._height = canvas.size

    def battery_status(self) -> Tuple[str, Optional[int]]:
        battery_up_days = System.battery.get_battery_up_days()
        device_up_time = System.battery.get_device_up_hour_minutes()
        device_up_count = System.battery.get_device_up_count()
        display_up_time = System.battery.get_display_refresh_hour_minutes()
        if (
            battery_up_days is not None
            and device_up_time is not None
            and device_up_count is not None
        ):
            log.info(f"Battery up days   {battery_up_days}")
            log.info(f"Device boot count {device_up_count}")
            log.info(f"Device up time    {device_up_time}")
            if display_up_time:
                log.info(f"Display up time   {display_up_time}")
            system_stat = f"{device_up_count}/{battery_up_days} {device_up_time}"
        else:
            system_stat = f"{config.PROJECT_NAME.upper()} {config.PROJECT_VERSION}"
        battery_per_cent = System.battery.battery_percent()
        if battery_per_cent is not None:
            log.info(f"Battery           {battery_per_cent}%")
        return system_stat, battery_per_cent

    def display_status(self) -> None:  # pylint: disable=too-many-locals
        bold_14_font = ImageFont.truetype(config.FONT_TTF, 14)
        emoji_14_font = ImageFont.truetype(config.FONT_EMOJI_TTF, 14)
        battery_font = bold_14_font
        status_margin = config.SCREEN_STATUS_MARGIN

        system_stat, battery_per_cent = self.battery_status()
        if battery_per_cent is not None:
            battery_stat = f"{battery_per_cent}%"
        else:
            battery_per_cent = 0
            battery_stat = "\U0001F50C"  # unicode for electric plug emoji
            battery_font = emoji_14_font

        draw = ImageDraw.Draw(self._canvas)

        _, _, _, stat_h = draw.textbbox((0, 0), system_stat, bold_14_font)
        x = status_margin
        y = self._height - status_margin - stat_h
        draw_overlay_text(draw, x, y, system_stat, bold_14_font, Palette.FG, Palette.BG)

        _, _, stat_w, stat_h = draw.textbbox((0, 0), battery_stat, battery_font)
        stat_icon_gap = int(stat_h / 4)

        icon_w = int(stat_h * 1.8)
        icon_h = stat_h

        x = self._width - status_margin - icon_w - stat_icon_gap - stat_w
        y = self._height - status_margin - stat_h
        draw.text((x, y), battery_stat, fill=(0, 0, 0), font=battery_font)

        x = self._width - status_margin - icon_w
        self.draw_battery(x, y, icon_w, icon_h, battery_per_cent)

    def draw_battery(  # pylint: disable=too-many-arguments
        self, x: int, y: int, w: int, h: int, percent: int
    ) -> None:
        draw = ImageDraw.Draw(self._canvas)
        terminal_w = int(w / 10) if w > 10 else 1
        terminal_h = int(h / 2)
        battery_w = w - terminal_w
        charge_w = int((battery_w * percent) / 100)
        pc_width = int(percent / 10 * 2) if percent else 0
        if pc_width:
            draw.rectangle(
                (x, y, x + charge_w, y + h),
                fill=Palette.FG if percent > 25 else Palette.HL,
            )
        draw.rectangle((x, y, x + battery_w, y + h), outline=Palette.FG)
        draw.rectangle(
            (
                x + battery_w,
                y + int((h - terminal_h) / 2),
                x + battery_w + terminal_w,
                (y + h) - int((h - terminal_h) / 2),
            ),
            outline=Palette.FG,
        )

    @staticmethod
    def upload_file(url: str, file_path: str) -> None:
        file_name = os.path.basename(file_path)
        with open(file_path, "rb") as file:
            files = {
                "file": (
                    file_name,
                    file,
                )
            }
            response = requests.post(
                url=url, files=files, timeout=config.API_TIMEOUT_SECS
            )
            if response.status_code == HTTPStatus.OK:
                log.info(f"Uploaded {file_name}")
            else:
                log.error(f"Failed uploading {file_name}: {response.reason}")

    @staticmethod
    def upload_screen() -> None:
        try:
            System.upload_file(
                config.UPLOAD_SCREEN_URL, f"{config.PROJECT_NAME.lower()}.png"
            )
        except Exception as error:
            log.error("Error uploading screen image %s", error)

    @staticmethod
    def upload_logs() -> None:
        try:
            System.upload_file(
                config.UPLOAD_LOGS_URL, os.path.expanduser(config.LOG_FILE)
            )
        except Exception as error:
            log.error("Error uploading logs %s", error)

    @staticmethod
    def upload() -> None:
        if config.UPLOAD_ENABLED:
            System.upload_logs()
            System.upload_screen()

    @staticmethod
    def device_boots() -> int:
        return System.battery.get_device_boots()

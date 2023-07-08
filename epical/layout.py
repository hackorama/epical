import datetime
import itertools
import sys
from typing import Any, List, Optional

import config
from cal_grid import CalGrid
from data.cal_data import CalData
from palette import Palette
from PIL import Image, UnidentifiedImageError
from style import GridStyle
from system import System
from util import abs_relative_path, log, report_complex_font_support

from grid import Grid  # pylint: disable=no-name-in-module


class Layout:  # pylint: disable=too-many-instance-attributes
    def __init__(self, data: CalData, width: int, height: int, border: int):
        self._data: CalData = data
        self._width: int = width
        self._height: int = height
        self._border: int = border
        self._grid_origin_x: int = self._border
        self._grid_origin_y: int = self._border
        self._grid_width: int = self._width - 2 * self._border
        self._grid_height: int = self._height - 2 * self._border
        self._image: Image.Image = Image.new(
            "RGBA", (self._width, self._height), Palette.BG
        )

    def __rotate_screen(self) -> None:
        tmp = self._height
        self._height = self._width
        self._width = tmp
        self._grid_width = self._width - 2 * self._border
        self._grid_height = self._height - 2 * self._border
        self._image = Image.new("RGBA", (self._width, self._height), Palette.BG)

    def build_header_grid(self) -> Grid:
        month_title = f"{self._data.get_month()} {self._data.get_year()}"
        mal_date = ""
        if config.MAL_DATE_ENABLED:
            report_complex_font_support()
            mal_date = self._data.get_malayalam_date()
        data = [[month_title, mal_date]]

        grid = Grid(data)
        grid.style().set_elastic_fit(True)
        grid.style(0, 0).set_align(left=True, top=True)
        grid.style(0, 0).set_font(abs_relative_path(config.FONT_TTF)).set_font_size(60)
        grid.style(0, 0).set_margin(0, 0, 0, 10)
        grid.style(0, 1).set_align(right=True, top=True)
        if config.MAL_DATE_ENABLED:
            grid.style(0, 1).set_font(
                abs_relative_path(config.MAL_FONT_TTF)
            ).set_font_size(24)
        grid.style(0, 1).set_font_color(Palette.LL)
        return grid

    def build_weather_grid(self) -> Grid:  # pylint: disable=too-many-locals
        data = self._data.get_weather()

        if not data:
            log.error("Skipping weather display, failed data fetch")
            return Grid([[]])

        grid = Grid(data)

        grid.style().set_margin(5, 5, 10, 10)
        grid.style().set_font(abs_relative_path(config.FONT_EMOJI_TTF)).set_font_size(
            28
        )

        style = GridStyle()
        style.set_font(abs_relative_path(config.FONT_TTF)).set_font_size(24)
        grid.set_odd_row_cell_style(style=style)

        lows = []
        highs = []
        for i, row in enumerate(data):
            if i % 2:  # temperature values are in even rows
                min_ = sys.maxsize
                max_ = 0
                min_cell = None
                max_cell = None
                for j, cell in enumerate(row):
                    if j > 0:  # skip first column which is header
                        if int(cell) < min_:
                            min_ = int(cell)
                            min_cell = (i, j)
                        if int(cell) > max_:
                            max_ = int(cell)
                            max_cell = (i, j)
                if min_cell:
                    lows.append(min_cell)
                if max_cell:
                    highs.append(max_cell)
        for low in lows:
            grid.style(low[0], low[1]).set_font(abs_relative_path(config.FONT_BOLD_TTF))
        for high in highs:
            grid.style(high[0], high[1]).set_font(
                abs_relative_path(config.FONT_BOLD_TTF)
            )
            if int(data[high[0]][high[1]]) >= 90:
                grid.style(high[0], high[1]).set_font_color(Palette.HL)

        return grid

    def get_photo(self) -> Optional[Image.Image]:
        photo_file_str_or_raw_bytes, photo_image_name = self._data.get_remote_photo()
        if not photo_file_str_or_raw_bytes:
            # Image open accepts raw "bytes" or filename "str" ignore type compatibility check
            photo_file_str_or_raw_bytes = self._data.get_photo()  # type: ignore
            photo_image_name = photo_file_str_or_raw_bytes  # type: ignore
            if not photo_file_str_or_raw_bytes:
                return None
            log.info(f"Displaying {photo_image_name}")
        else:
            log.info(f"Displaying remote {photo_image_name}")
        if not photo_image_name:
            return None
        try:
            if photo_image_name.lower().endswith(".bmp"):
                photo = Image.open(
                    photo_file_str_or_raw_bytes
                )  # expect color converted bmp
            else:
                photo = Image.open(photo_file_str_or_raw_bytes).convert(
                    "L"
                )  # convert to grey scale
            return photo
        except UnidentifiedImageError as error:
            log.error(f"Invalid photo file: {error}")
        return None

    def show_photo(self) -> None:
        photo = self.get_photo()
        if not photo:
            log.warning("No photo found to display")
            return
        photo.thumbnail(
            (config.PHOTO_BOUNDING_BOX_WIDTH, config.PHOTO_BOUNDING_BOX_HEIGHT)
        )
        self._image.paste(
            photo,
            (
                self._border,
                self._height
                - photo.height
                - self._border
                - config.SCREEN_STATUS_MARGIN,
            ),
        )  # transparent

    def build_cal_grid(self) -> Grid:
        cal_data = self._data.get_cal()
        grid = CalGrid(cal_data)
        grid.style().set_margin(10, 10, 10, 10)
        grid.style().set_font(abs_relative_path(config.FONT_TTF)).set_font_size(24)
        return grid

    def set_event_grid_size(self, events, style):
        count = len(events)
        event_len = 0
        for v in events.values():
            if len(v) > event_len:
                event_len = len(v)
        if count <= 4:
            style.set_margin(5, 5, 5, 50)
            style.set_font(abs_relative_path(config.FONT_TTF)).set_font_size(36)
        elif count <= 6:
            style.set_margin(5, 5, 5, 10)
            style.set_font(abs_relative_path(config.FONT_TTF)).set_font_size(36)
        elif count <= 8:
            style.set_margin(5, 5, 5, 10)
            style.set_font(abs_relative_path(config.FONT_TTF)).set_font_size(22)
        elif count <= 10:
            style.set_margin(5, 5, 5, 5)
            style.set_font(abs_relative_path(config.FONT_TTF)).set_font_size(18)
        else:
            style.set_margin(5, 5, 5, 5)
            style.set_font(abs_relative_path(config.FONT_TTF)).set_font_size(14)

        if event_len > 40:
            style.set_font(abs_relative_path(config.FONT_TTF)).set_font_size(14)
        elif event_len > 32:
            style.set_font(abs_relative_path(config.FONT_TTF)).set_font_size(22)

    def build_events_grid(self) -> Grid:
        month_number = int(datetime.datetime.now().strftime("%m"))
        events = self._data.get_events(month_number)
        if len(events) > 25:
            log.warning(f"Too many events, showing only 25/{len(events)}")
            events = dict(itertools.islice(events.items(), 25))
        events_data = []
        for day, event in events.items():
            if len(event) > 64:
                log.warning(f"Truncating long event description to 64/{len(event)}")
                event = event[:64] + " ..."
            events_data.append([day, event])  # two-dimensional array
        if events_data:
            events_data.append(["", ""])  # empty valid data
        grid = Grid(events_data)
        self.set_event_grid_size(events, grid.style())
        grid.style().set_align(left=True, top=True)
        today = datetime.datetime.now().day
        for i, event in enumerate(events_data):
            if event[0] and int(event[0]) == today:
                grid.style(i, 0).set_font_color(Palette.HL)
                grid.style(i, 1).set_font_color(Palette.HL)
            if not event[
                1
            ].isascii():  # check for non ascii international chars and change font
                grid.style(i, 1).set_font(abs_relative_path(config.MAL_FONT_TTF))

        return grid

    def build_scores_grid(self) -> Grid:
        logo_image_name, w, h = self._data.get_score_logo()
        logo = Image.open(logo_image_name)
        logo.thumbnail((w, h))

        score_data = []
        for score in self._data.scores:
            if score["score"]:
                score_data.append(
                    [score["name"], score["score"]]
                )  # two-dimensional array
            else:
                score_data.append(
                    [score["name"], score["game_time"]]
                )  # two-dimensional array

        if not score_data:
            score_data = [[""]]
        games_grid = Grid(score_data)
        games_grid.style().set_margin(5, 0, 5, 5)
        games_grid.style().set_font(
            abs_relative_path(config.FONT_BOLD_TTF)
        ).set_font_size(18)
        games_grid.style().set_align(right=True)

        games_data: List[List[Any]] = [[games_grid], [logo]]

        for i, score in enumerate(self._data.scores):
            if not score["score"]:  # upcoming game
                games_grid.style(i, 1).set_font_size(14)
            elif score["won"]:
                games_grid.style(i, 1).set_font_color(Palette.HL)

        score_grid = Grid(
            data=games_data,
        )
        score_grid.style(1, 0).set_margin(0, 0, 0, 0).set_outer_margin(
            0, 0, 0, 0
        ).set_align(
            right=True
        )  # logo
        if not config.SCREEN_ROTATE:
            games_grid.invert()
            score_grid.invert()
        return score_grid

    def display_status(self) -> None:  # pylint: disable=too-many-locals
        system = System(self._image)
        system.display_status()

    def display_portrait(self) -> Image.Image:
        self.__rotate_screen()

        self.show_photo()

        header_grid = self.build_header_grid()
        weather_grid = self.build_weather_grid()
        cal_grid = self.build_cal_grid()
        event_grid = self.build_events_grid()
        score_grid = self.build_scores_grid()

        mid_grid = Grid([[weather_grid, cal_grid]])
        mid_grid.style().set_elastic_fit(True)
        mid_grid.style().set_edge_fit(True)

        lower_grid = Grid([[event_grid, score_grid]])
        lower_grid.style().set_margin(0, 0, 0, 0)
        lower_grid.style().set_elastic_fit(True)
        lower_grid.style().set_edge_fit(True)

        grid = Grid(
            [[header_grid], [mid_grid], [lower_grid]],
            width=self._grid_width,
        )
        grid.style().set_align(left=True, top=True)
        grid.style().set_elastic_fit(True)
        grid.style().set_edge_fit(True)

        grid.draw(
            self._image,
            origin_x=self._grid_origin_x,
            origin_y=self._grid_origin_y,
        )

        self.display_status()

        return self._image

    def display_landscape(self) -> Image.Image:
        header_grid = self.build_header_grid()
        weather_grid = self.build_weather_grid()
        weather_grid.invert()
        cal_grid = self.build_cal_grid()
        event_grid = self.build_events_grid()
        score_grid = self.build_scores_grid()

        right_grid = Grid([[cal_grid], [weather_grid]])
        right_grid.style().set_elastic_fit(True)
        right_grid.style(0, 0).set_align(right=True)
        right_grid.style(1, 0).set_align(right=True).set_margin(0, 0, 0, 0)

        mid_grid = Grid([[event_grid, right_grid]])
        mid_grid.style().set_elastic_fit(True)
        mid_grid.style().set_edge_fit(True)

        lower_grid = Grid([[score_grid]])
        lower_grid.style().set_elastic_fit(True)
        lower_grid.style().set_edge_fit(True)

        grid = Grid(
            data=[[header_grid], [mid_grid], [lower_grid]],
            width=self._grid_width,
            height=self._grid_height,
        )

        grid.draw(
            self._image,
            origin_x=self._grid_origin_x,
            origin_y=self._grid_origin_y,
        )

        self.display_status()

        return self._image

    def display(self) -> Image.Image:
        if config.SCREEN_ROTATE:
            return self.display_portrait()
        return self.display_landscape()

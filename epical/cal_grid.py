import datetime

import config
from palette import Palette

from grid import Grid  # pylint: disable=no-name-in-module


class CalGrid(Grid):  # pylint: disable=too-few-public-methods
    def _get_cell_data(self, row, col):
        # Calendar grid data includes additional data like events
        # which are used during rendering for conditional cell styling
        # But cell size resolving should use the specific data
        # that will be displayed.
        # So override this to return only the specific data
        # that will be used for cell display
        return self._data[row][col]["day"]

    def _draw_cell(  # pylint: disable=too-many-arguments
        self,
        row: int = 0,
        col: int = 0,
        x1: int = 1,
        y1: int = 1,
        x2: int = 1,
        y2: int = 1,
        debug: bool = False,  # pylint: disable=unused-argument
    ) -> None:
        # Override and customize cell drawing for conditional custom styling
        draw = self._get_draw()
        style = self._resolve_style(row, col)
        day = datetime.datetime.now().strftime("%d")
        day_color = Palette.FG

        style.set_font(config.FONT_BOLD_TTF)

        if not self._data[row][col]["current_month"]:
            day_color = Palette.FG
            style.set_font(config.FONT_TTF)
        elif col in (0, 6):  # sunday and saturday
            day_color = Palette.HL

        if self._data[row][col]["current_month"] and self._data[row][col]["event"]:
            draw.ellipse(
                (
                    x1 + 2,
                    y1 + 2,
                    x2 - 2,
                    y2 - 2,
                ),
                outline=Palette.FG,
            )

        if self._data[row][col]["current_month"] and self._data[row][col]["day"] == int(
            day
        ):  # today
            draw.ellipse(
                (
                    x1 + 2,
                    y1 + 2,
                    x2 - 2,
                    y2 - 2,
                ),
                outline=Palette.HL,
                fill=Palette.HL,
            )
            day_color = Palette.BG

        font = style.get_font_object()
        self._draw_cell_text(
            row, col, str(self._data[row][col]["day"]), font=font, fill=day_color
        )

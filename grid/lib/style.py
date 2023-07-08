import os
from typing import Optional, Tuple

from multipledispatch import dispatch
from PIL import ImageFont
from PIL.ImageFont import FreeTypeFont
from typing_extensions import Self


class Align:  # pylint: disable=too-few-public-methods
    def __init__(
        self,
        left: bool = False,
        right: bool = False,
        top: bool = False,
        bottom: bool = False,
    ) -> None:
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    def aligned(self) -> bool:
        return self.left or self.right or self.top or self.bottom


class Margin:  # pylint: disable=too-few-public-methods
    def __init__(
        self, left: int = 2, right: int = 2, top: int = 2, bottom: int = 2
    ) -> None:
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom


class Border:  # pylint: disable=too-few-public-methods, too-many-instance-attributes
    def __init__(  # pylint: disable=too-many-arguments
        self,
        left: int = 0,
        right: int = 0,
        top: int = 0,
        bottom: int = 0,
        left_color: Tuple[int, int, int] = (0, 0, 0),
        right_color: Tuple[int, int, int] = (0, 0, 0),
        top_color: Tuple[int, int, int] = (0, 0, 0),
        bottom_color: Tuple[int, int, int] = (0, 0, 0),
    ) -> None:
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.left_color = left_color
        self.right_color = right_color
        self.top_color = top_color
        self.bottom_color = bottom_color


class GridBorder:  # pylint: disable=too-few-public-methods
    def __init__(
        self,
        row_border_width: int = 0,
        column_border_width: int = 0,
        row_border_color: Tuple[int, int, int] = (255, 255, 255),
        column_border_color: Tuple[int, int, int] = (255, 255, 255),
    ) -> None:
        self.row_border_width = row_border_width
        self.row_border_color = row_border_color
        self.column_border_width = column_border_width
        self.column_border_color = column_border_color
        self.row_border_priority = True


class GridStyle:  # pylint: disable=too-many-instance-attributes
    BLACK: Tuple[int, int, int] = (0, 0, 0)
    WHITE: Tuple[int, int, int] = (255, 255, 255)
    FG: Tuple[int, int, int] = BLACK
    BG: Tuple[int, int, int] = WHITE
    DEFAULT_FONT_FILE = "font.ttf"

    def __init__(  # pylint: disable=too-many-arguments
        self,
        margin: Optional[Margin] = None,
        outer_margin: Optional[Margin] = None,
        align: Optional[Align] = None,
        border: Optional[Border] = None,
        bg_color: Optional[Tuple[int, int, int]] = None,
        elastic_fit: bool = False,
        fixed_fit: bool = False,
        edge_align: bool = False,
        grid_border: Optional[GridBorder] = None,
        font_size: int = 12,
        font_color=None,
    ) -> None:
        self.margin: Margin = margin if margin else Margin()
        self.outer_margin: Margin = outer_margin if outer_margin else Margin()
        self.align = align if align else Align()
        self.border: Border = border if border else Border()
        self.grid_border: GridBorder = grid_border if grid_border else GridBorder()
        self.font: str = GridStyle.__font_abs_path(GridStyle.DEFAULT_FONT_FILE)
        self.font_size: int = font_size
        self.font_color: Tuple[int, int, int] = (
            font_color if font_color else GridStyle.FG
        )
        self.bg_color: Optional[Tuple[int, int, int]] = bg_color
        self.elastic_fit: bool = elastic_fit
        self.fixed_fit: bool = fixed_fit
        self.edge_align: bool = edge_align

    @staticmethod
    def __font_abs_path(font_file_name: str) -> str:
        this_file = os.path.abspath(__file__)
        this_dir = os.path.dirname(this_file)
        return str(os.path.join(this_dir, font_file_name))

    @dispatch(int)
    def set_margin(self, width: int = 0) -> Self:
        self.margin = Margin(width, width, width, width)
        return self

    @dispatch(int, int)  # type: ignore
    def set_margin(  # pylint: disable=function-redefined
        self, horizontal: int = 0, vertical: int = 0
    ) -> Self:
        self.margin = Margin(
            left=horizontal, right=horizontal, top=vertical, bottom=vertical
        )
        return self

    @dispatch(int, int, int, int)  # type: ignore
    def set_margin(  # pylint: disable=function-redefined
        self, left: int = 0, right: int = 0, top: int = 0, bottom: int = 0
    ) -> Self:
        self.margin = Margin(left, right, top, bottom)
        return self

    def set_outer_margin(
        self, left: int = 0, right: int = 0, top: int = 0, bottom: int = 0
    ) -> Self:
        self.outer_margin = Margin(left, right, top, bottom)
        return self

    def set_align(
        self,
        left: bool = False,
        right: bool = False,
        top: bool = False,
        bottom: bool = False,
    ) -> Self:
        self.align = Align(left, right, top, bottom)
        return self

    def set_font(self, font: str) -> Self:
        self.font = font
        return self

    def set_font_size(self, size: int) -> Self:
        self.font_size = size
        return self

    def set_font_color(self, color: Tuple[int, int, int]) -> Self:
        self.font_color = color
        return self

    def set_cell_border(  # pylint: disable=too-many-arguments
        self,
        left: int = 0,
        right: int = 0,
        top: int = 0,
        bottom: int = 0,
        left_color: Tuple[int, int, int] = (0, 0, 0),
        right_color: Tuple[int, int, int] = (0, 0, 0),
        top_color: Tuple[int, int, int] = (0, 0, 0),
        bottom_color: Tuple[int, int, int] = (0, 0, 0),
    ) -> Self:
        self.border = Border(
            left, right, top, bottom, left_color, right_color, top_color, bottom_color
        )
        return self

    def set_bg_color(self, bg_color: Tuple[int, int, int] = (255, 255, 255)) -> Self:
        self.bg_color = bg_color
        return self

    def set_elastic_fit(self, fit: bool = False) -> Self:
        self.elastic_fit = fit
        return self

    def set_fixed_fit(self, fit: bool = False) -> Self:
        self.fixed_fit = fit
        return self

    def set_edge_fit(self, fit: bool = False) -> Self:
        self.edge_align = fit
        return self

    def set_grid_border(self, width: int, color: Tuple[int, int, int]) -> Self:
        self.grid_border = GridBorder(width, width, color, color)
        return self

    def set_grid_column_border(self, width: int, color: Tuple[int, int, int]) -> Self:
        self.grid_border.column_border_width = width
        self.grid_border.column_border_color = color
        return self

    def set_grid_row_border(self, width: int, color: Tuple[int, int, int]) -> Self:
        self.grid_border.row_border_width = width
        self.grid_border.row_border_color = color
        return self

    def set_grid_row_border_priority(self) -> Self:
        self.grid_border.row_border_priority = True
        return self

    def set_grid_column_border_priority(self) -> Self:
        self.grid_border.row_border_priority = False
        return self

    def get_font_object(self) -> FreeTypeFont:
        return ImageFont.truetype(self.font, self.font_size)

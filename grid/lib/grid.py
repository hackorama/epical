import copy
from typing import Any, List, Literal, Optional, Tuple

from draw import draw_rectangle
from PIL import Image, ImageDraw
from PIL.ImageFont import FreeTypeFont
from style import Align, Border, GridStyle, Margin
from typing_extensions import Self


class Grid:  # pylint: disable=too-many-instance-attributes, too-many-public-methods
    DEBUG_COLOR = (200, 200, 200)
    DEFAULT_SIZE = 2
    # Ref: https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
    MULTI_LINE_SPACING = 4

    def __init__(
        self,
        data: List[List[Any]],
        width: int = 0,
        height: int = 0,
    ):
        self._origin_x: int = 0
        self._origin_y: int = 0
        self._width: int = width
        self._height: int = height

        self._canvas: Optional[Image.Image] = None
        self._canvas_width: int = 0
        self._canvas_height: int = 0
        self._style: GridStyle = GridStyle()
        self._data, self._rows, self._cols = self.__sanitized_data(data)
        self._cell_style: List[List[Optional[GridStyle]]] = [
            [None] * self._cols for _ in range(self._rows)
        ]
        self._cell_sizes: List[List[Tuple[int, int]]] = [  # TODO must be int
            [(0, 0)] * self._cols for _ in range(self._rows)
        ]
        self._parent: Optional[Grid] = None
        self._parent_col: Optional[int] = None
        self._parent_row: Optional[int] = None
        self._debug: bool = False
        self.__set_container_parent()

    def __sanitized_data(
        self, data: List[List[Any]]
    ) -> Tuple[List[List[Any]], int, int]:
        if not data:
            return [[None]], 1, 1
        if len(data[0]) == 0:
            return [[None]], 1, 1
        for i, row in enumerate(data):
            if not row:
                data[i] = [None]
            if not isinstance(row, List):
                data[i] = [row]
        cols = max(  # pylint: disable=consider-using-generator
            [len(row) for row in data]
        )
        padded_data = [row + [None] * (cols - len(row)) for row in data]
        return padded_data, len(padded_data), cols

    def __set_container_parent(self) -> None:
        # Save only the parent grid reference and cell location
        # We cannot save the cell sizes until parent grid is rendered
        # So this stored parent position will be used later down
        # in the recursive rendering pipeline when parent cell sizes are resolved
        for row in range(self._rows):
            for col in range(self._cols):
                cell_data = self._get_cell_data(row, col)
                if isinstance(cell_data, Grid):
                    cell_data._parent = self
                    cell_data._parent_row = row
                    cell_data._parent_col = col

    def _get_cell_data(self, row: int, col: int) -> Any:
        return self._data[row][col]

    def __solve_adaptive_sizes(  # pylint: disable=too-many-statements
        self,
    ) -> Tuple[List[int], List[int]]:
        col_width: List[int] = [0] * self._cols
        row_height: List[int] = [0] * self._rows
        gw, gh = self.__grid_size()
        # Start with equal fixed size
        w = int(gw / self._cols)
        h = int(gh / self._rows)
        for row in range(self._rows):
            for col in range(self._cols):
                style = self._resolve_style(row, col)
                cell_data = self._get_cell_data(row, col)
                if isinstance(cell_data, (float, int, str)):
                    w, h = self.__text_size(str(cell_data), style.get_font_object())
                elif isinstance(cell_data, Image.Image):
                    w, h = cell_data.size
                elif isinstance(cell_data, Grid):
                    cell_data.__resolve_cell_sizes()
                    w, h = cell_data.__grid_size()
                    if self._style.grid_border.column_border_width:
                        w += 1
                    if self._style.grid_border.row_border_width:
                        h += 1
                else:
                    w = h = Grid.DEFAULT_SIZE

                w += style.outer_margin.left + style.outer_margin.right
                w += self._style.grid_border.column_border_width
                w += style.border.left + style.border.right
                w += style.margin.left + style.margin.right
                h += style.outer_margin.top + style.outer_margin.bottom
                h += style.border.top + style.border.bottom
                h += self._style.grid_border.row_border_width
                h += style.margin.top + style.margin.bottom

                if w > col_width[col]:
                    col_width[col] = w
                if h > row_height[row]:
                    row_height[row] = h

        return col_width, row_height

    def __resolve_cell_sizes(self) -> None:
        if self._style.fixed_fit:
            self.__resolve_fixed_cell_sizes()
        else:
            self.__resolve_adaptive_cell_sizes()

    def __resolve_adaptive_cell_sizes(self) -> None:
        col_width, row_height = self.__solve_adaptive_sizes()
        for r in range(self._rows):
            for c in range(self._cols):
                self._cell_sizes[r][c] = (col_width[c], row_height[r])
        gw = 0
        gh = 0
        for c in range(self._cols):
            gw += col_width[c]
        for r in range(self._rows):
            gh += row_height[r]

        gw += self._style.grid_border.column_border_width
        gh += self._style.grid_border.row_border_width

        if not self._width:
            self._width = gw
        if not self._height:
            self._height = gh
        self.__cell_elastic_fit(gw, gh)

    def __cell_elastic_fit(self, gw: int, gh: int) -> None:
        # Expand all cells equally to match given grid size
        cw_delta = 0
        ch_delta = 0

        if gw < self._width:
            gw_delta = self._width - gw
            cw_delta = int(gw_delta / self._cols)
        else:
            self._width = gw

        if gh < self._height:
            gh_delta = self._height - gh
            ch_delta = int(gh_delta / self._rows)
        else:
            self._height = gh

        if cw_delta or ch_delta:
            for row in range(self._rows):
                for col in range(self._cols):
                    w, h = self._cell_sizes[row][col]
                    self._cell_sizes[row][col] = (w + cw_delta, h + ch_delta)

    def __resolve_fixed_cell_sizes(self) -> None:
        gw, gh = self.__grid_size()
        # TODO FIXME fixed size without canvas
        if not gw and not gh and not self._canvas:
            self.__resolve_adaptive_cell_sizes()
            return
        if not gw and self._canvas:
            gw = self._canvas.width
        if not gh and self._canvas:
            gh = self._canvas.height
        cw = int(gw / self._cols)
        ch = int(gh / self._rows)
        for r in range(self._rows):
            for c in range(self._cols):
                self._cell_sizes[r][c] = (cw, ch)

    def __grid_size(self) -> Tuple[int, int]:
        return self._width, self._height

    def __resolve_cell_position(
        self, row: int, col: int
    ) -> Tuple[int, int, int, int]:  # pylint: disable=too-many-locals
        x, y, w, h, _, _, _, _ = self.__cell_size(row, col)
        x1, y1, x2, y2 = self.resolve_positions(x, y, w, h)
        # If the cell object is another grid then use that child grid's size
        # when parent grid has no fixed content size
        if not self._style.fixed_fit:
            cell_data = self._get_cell_data(row, col)
            if isinstance(cell_data, Grid) and cell_data._style.elastic_fit:
                # Use stored parent cell location and fit this to parent cell size
                cell_data._parent_cell_fit()
        return x1, y1, x2, y2

    def _resolve_style(self, row: int, col: int) -> GridStyle:
        if not self._cell_style[row][col]:
            self._cell_style[row][col] = copy.deepcopy(self._style)
        # the style will not be none at this point so ignore mypy optional warning
        return self._cell_style[row][col]  # type: ignore

    def _draw_cell(  # pylint: disable=too-many-arguments
        self,
        row: int,
        col: int,
        x1: int,  # pylint: disable=unused-argument
        y1: int,  # pylint: disable=unused-argument
        x2: int,  # pylint: disable=unused-argument
        y2: int,  # pylint: disable=unused-argument
        debug: bool = False,
    ) -> None:
        style = self._resolve_style(row, col)
        cell_data = self._get_cell_data(row, col)
        if isinstance(cell_data, (float, int, str)):
            self._draw_cell_text(
                row,
                col,
                str(cell_data),
                font=style.get_font_object(),
                fill=style.font_color,
                align=style.align,
            )
        elif isinstance(cell_data, Image.Image):
            dw, dh = cell_data.size
            ax, ay = self._cell_content_size_align(
                row,
                col,
                dw,
                dh,
                style.align.left,
                style.align.right,
                style.align.top,
                style.align.bottom,
            )
            # Top left anchor correction
            if not style.align.left:
                ax += 1
            if not style.align.top:
                ay += 1
            self._draw_cell_image(int(ax), int(ay), cell_data)
        elif isinstance(cell_data, Grid):
            self._draw_cell_grid(row, col, cell_data, align=style.align, debug=debug)

    def _draw_cell_text(  # pylint: disable=too-many-arguments
        self,
        row: int,
        col: int,
        text: str,
        font: FreeTypeFont,
        fill: Tuple[int, int, int],
        align: Optional[Align] = None,
    ):
        if not align:
            align = self._resolve_style(row, col).align

        draw = self._get_draw()
        tw, th = self.__text_size(text, font)
        text_align: Literal["left", "right", "center"] = "center"
        if align.left:
            text_align = "left"
        if align.right:
            text_align = "right"
        draw.multiline_text(
            self._cell_content_size_align(
                row, col, tw, th, align.left, align.right, align.top, align.bottom
            ),
            text,
            font=font,
            fill=fill,
            spacing=Grid.MULTI_LINE_SPACING,
            align=text_align,
        )

    def _draw_cell_image(self, x: int, y: int, image: Image.Image):
        # TODO raise exception for canvas none
        if image.mode == "RGBA" and self._canvas:
            self._canvas.paste(image, (x, y), mask=image)
        elif self._canvas:
            self._canvas.paste(image, (x, y))

    def _draw_cell_grid(  # pylint: disable=too-many-arguments
        self, row: int, col: int, grid: Self, align: Align, debug: bool = False
    ) -> Image.Image:
        w, h = grid.get_grid_size()
        ax, ay = self._cell_content_size_align(
            row, col, w, h, align.left, align.right, align.top, align.bottom
        )
        if (
            self._style.grid_border.column_border_width
            and self._style.grid_border.column_border_width % 2 == 0
        ):
            ax += 1
        if (
            self._style.grid_border.row_border_width
            and self._style.grid_border.row_border_width % 2 == 0
        ):
            ay += 1
        return grid.__render(self._canvas, int(ax), int(ay), debug)

    def __grid_border_pixel_correction(self) -> Tuple[int, int, int, int]:
        if (
            not self._style.grid_border.row_border_width
            and not self._style.grid_border.column_border_width
        ):
            return 0, 0, 0, 0
        h_l_o = int(self._style.grid_border.column_border_width / 2)
        v_t_o = int(self._style.grid_border.row_border_width / 2)
        h_r_o = h_l_o
        v_b_o = v_t_o
        # Mid-point correction for odd widths
        if self._style.grid_border.row_border_width % 2 == 0:
            v_t_o -= 1
        if self._style.grid_border.column_border_width % 2 == 0:
            h_l_o -= 1
        if self._style.grid_border.column_border_width < 2:
            h_l_o = h_r_o = 0
        if self._style.grid_border.row_border_width < 2:
            v_t_o = v_b_o = 0
        return h_l_o, h_r_o, v_t_o, v_b_o

    def _draw_cell_bg(  # pylint: disable=too-many-arguments
        self,
        row: int,
        col: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> None:
        style = self._resolve_style(row, col)
        if not style.bg_color:
            return
        draw = self._get_draw()
        # propagate grid ine mid-point offset correction to cell drawing
        h_l_o, h_r_o, v_t_o, v_b_o = self.__grid_border_pixel_correction()
        dw = self._style.grid_border.column_border_width
        dh = self._style.grid_border.row_border_width
        draw.rectangle(
            (
                x1 + style.outer_margin.left + dw - h_l_o,  # + style.border.left,
                y1 + style.outer_margin.top + dh - v_t_o,  # + style.border.top,
                x2 - style.outer_margin.right - dw + h_r_o,  # - style.border.right,
                y2 - style.outer_margin.bottom - dh + v_b_o,  # - style.border.bottom,
            ),
            fill=style.bg_color,
        )

    def _draw_cell_border(  # pylint: disable=too-many-arguments, too-many-locals
        self, row: int, col: int, x1: int, y1: int, x2: int, y2: int, collapsed=False
    ) -> None:
        style = self._resolve_style(row, col)
        draw = self._get_draw()
        # propagate grid ine mid-point offset correction to cell drawing
        h_l_o, h_r_o, v_t_o, v_b_o = self.__grid_border_pixel_correction()
        dw = self._style.grid_border.column_border_width
        dh = self._style.grid_border.row_border_width
        if (
            not style.border.left
            and not style.border.right
            and not style.border.top
            and not style.border.bottom
        ):
            return
        draw_rectangle(
            draw,
            (
                x1 + style.outer_margin.left + dw - h_l_o,
                y1 + style.outer_margin.top + dh - v_t_o,
                x2 - style.outer_margin.right - dw + h_r_o,
                y2 - style.outer_margin.bottom - dh + v_b_o,
            ),
            left_width=style.border.left,
            right_width=style.border.right,
            top_width=style.border.top,
            bottom_width=style.border.bottom,
            left_color=style.border.left_color,
            right_color=style.border.right_color,
            top_color=style.border.top_color,
            bottom_color=style.border.bottom_color,
            row_priority=self._style.grid_border.row_border_priority,
            collapsed=collapsed,
        )

    def __draw_cell_borders(self) -> None:
        for row in range(self._rows):
            for col in range(self._cols):
                x1, y1, x2, y2 = self.__resolve_cell_position(row, col)
                self._draw_cell_bg(row, col, x1, y1, x2, y2)
                self._draw_cell_border(row, col, x1, y1, x2, y2)

    def __draw_collapsed_cell_borders(self) -> None:
        if not self._canvas:
            return
        for row in range(self._rows):
            for col in range(self._cols):
                x1, y1, x2, y2 = self.__resolve_cell_position(row, col)
                if x2 >= self._canvas.width:
                    x2 -= 1
                if y2 >= self._canvas.height:
                    y2 -= 1
                self._draw_cell_border(row, col, x1, y1, x2, y2, collapsed=True)

    def __draw_cell_content(self, debug: bool) -> None:
        for row in range(self._rows):
            for col in range(self._cols):
                x1, y1, x2, y2 = self.__resolve_cell_position(row, col)
                self._draw_cell(row, col, x1, y1, x2, y2, debug=debug)

    def __draw_grid_borders(
        self,
        h_lines: List[Tuple[Tuple[int, int], Tuple[int, int]]],
        v_lines: List[Tuple[Tuple[int, int], Tuple[int, int]]],
    ) -> None:
        draw = self._get_draw()
        if self._style.grid_border.row_border_priority:
            if self._style.grid_border.column_border_width:
                for xy in v_lines:
                    draw.line(
                        xy,
                        width=self._style.grid_border.column_border_width,
                        fill=self._style.grid_border.column_border_color,
                    )
            if self._style.grid_border.row_border_width:
                for xy in h_lines:
                    draw.line(
                        xy,
                        width=self._style.grid_border.row_border_width,
                        fill=self._style.grid_border.row_border_color,
                    )
        else:
            if self._style.grid_border.row_border_width:
                for xy in h_lines:
                    draw.line(
                        xy,
                        width=self._style.grid_border.row_border_width,
                        fill=self._style.grid_border.row_border_color,
                    )
            if self._style.grid_border.column_border_width:
                for xy in v_lines:
                    draw.line(
                        xy,
                        width=self._style.grid_border.column_border_width,
                        fill=self._style.grid_border.column_border_color,
                    )

    def __render(  # pylint: disable=too-many-locals
        self,
        canvas,
        origin_x: int = 0,
        origin_y: int = 0,
        debug: bool = False,
    ) -> Image.Image:
        if self._style.edge_align:
            self.__cell_edge_align()
        self._canvas = canvas
        self._origin_x = origin_x
        self._origin_y = origin_y
        self.__resolve_cell_sizes()
        if not self._canvas:
            self._canvas = Image.new(
                "RGBA",
                (
                    self._width,
                    self._height,
                    # int(self._width + self._style.grid_border.column_border_width),
                    # int(self._height + +self._style.grid_border.row_border_width),
                ),
                (255, 255, 255),
            )  # TODO bg fill color
            self._canvas_width = self._width
            self._canvas_height = self._height

        h_l_o, h_r_o, v_t_o, v_b_o = self.__grid_border_pixel_correction()
        h_grids: List[Tuple[Tuple[int, int], Tuple[int, int]]] = []
        v_grids: List[Tuple[Tuple[int, int], Tuple[int, int]]] = []
        for col in range(self._cols):
            ax1, ay1, _, ay2 = self.__resolve_cell_position(0, col)
            _, _, bx2, by2 = self.__resolve_cell_position(self._rows - 1, col)
            v_grids.append(((ax1, ay1 - v_t_o), (ax1, by2 + v_b_o)))
            if col == self._cols - 1:  # add right for last col
                v_grids.append(((bx2, ay1 - v_t_o), (bx2, by2 + v_b_o)))
        for row in range(self._rows):
            ax1, ay1, _, ay2 = self.__resolve_cell_position(row, 0)
            _, _, bx2, by2 = self.__resolve_cell_position(row, self._cols - 1)
            h_grids.append(((ax1 - h_l_o, ay1), (bx2 + h_r_o, ay1)))
            if row == self._rows - 1:  # add bottom for last row
                h_grids.append(((ax1 - h_l_o, ay2), (bx2 + h_r_o, ay2)))

        self.__draw_cell_borders()
        self.__draw_collapsed_cell_borders()
        self.__draw_cell_content(debug)
        self.__draw_grid_borders(h_grids, v_grids)

        if debug or self._debug:
            self.__debug()
        return self._canvas

    def __cell_size(  # pylint: disable=too-many-locals
        self,
        row: int,
        col: int,
    ) -> Tuple[int, int, int, int, float, float, Margin, Border]:
        style = self._resolve_style(row, col)
        w, h = self._cell_sizes[row][col]
        dw = 0
        dh = 0
        for i in range(col):
            dw += self._cell_sizes[row][i][0]
        for i in range(row):
            dh += self._cell_sizes[i][col][1]

        x = self._origin_x + int(style.grid_border.column_border_width / 2) + dw
        y = self._origin_y + int(style.grid_border.row_border_width / 2) + dh

        l_b = (
            style.outer_margin.left
            + style.margin.left
            + style.border.left
            + style.grid_border.column_border_width
        )
        r_b = (
            style.outer_margin.right
            + style.margin.right
            + style.border.right
            + style.grid_border.column_border_width
        )
        t_b = (
            style.outer_margin.top
            + style.margin.top
            + style.border.top
            + style.grid_border.row_border_width
        )
        b_b = (
            style.outer_margin.bottom
            + style.margin.bottom
            + style.border.bottom
            + style.grid_border.row_border_width
        )

        c_w = w - (l_b + r_b)
        c_h = h - (t_b + b_b)
        cx = x + l_b + (c_w / 2)
        cy = y + t_b + (c_h / 2)

        return (
            x,
            y,
            w,
            h,
            cx,
            cy,
            style.margin,
            style.border,
        )  # TODO Improve return values

    def _cell_content_size_align(  # pylint: disable=too-many-arguments,too-many-locals
        self,
        row: int,
        col: int,
        cell_data_w: int,
        cell_data_h: int,
        left: bool = False,
        right: bool = False,
        top: bool = False,
        bottom: bool = False,
    ) -> Tuple[float, float]:
        style = self._resolve_style(row, col)
        x, y, w, h, cx, cy, margin, border = self.__cell_size(row, col)
        ax = cx - (cell_data_w / 2)
        if left:
            ax = (
                x
                + margin.left
                + border.left
                + style.outer_margin.left
                + style.grid_border.column_border_width
            )
        if right:
            ax = x + (
                w
                - cell_data_w
                - margin.right
                - border.right
                - style.outer_margin.right
                - style.grid_border.column_border_width
            )
        ay = cy - (cell_data_h / 2)
        if top:
            ay = (
                y
                + margin.top
                + border.top
                + style.outer_margin.top
                + style.grid_border.row_border_width
            )
        if bottom:
            ay = y + (
                h
                - cell_data_h
                - margin.bottom
                - border.bottom
                - style.outer_margin.bottom
                - style.grid_border.row_border_width
            )
        return ax, ay

    def _parent_cell_fit(self) -> None:
        if (
            self._parent
            and self._parent_row is not None
            and self._parent_col is not None
        ):
            pcw, pch = self._parent._cell_sizes[self._parent_row][self._parent_col]
            parent_style = self._parent._resolve_style(
                self._parent_row, self._parent_col
            )
            pcw -= (
                parent_style.margin.left
                + parent_style.margin.right
                + parent_style.border.left
                + parent_style.border.right
                + parent_style.outer_margin.left
                + parent_style.outer_margin.right
                + parent_style.grid_border.column_border_width
            )
            pch -= (
                parent_style.margin.top
                + parent_style.margin.bottom
                + parent_style.border.top
                + parent_style.border.bottom
                + parent_style.outer_margin.top
                + parent_style.outer_margin.bottom
                + parent_style.grid_border.row_border_width
            )
            if pcw > self._width:
                self._width = pcw
            if pch > self._height:
                self._height = pch

    def __text_height(self, font: FreeTypeFont) -> int:
        # Use characters top tall 'b' and bottom tall 'g' for max height for the given font
        # NOTE: This only works for Latin characters
        # TODO: explore using Pillow text anchors for a generic text bbox alignment
        # https://pillow.readthedocs.io/en/stable/handbook/text-anchors.html
        draw = self._get_draw()
        _, _, _, b = draw.textbbox((0, 0), "bg", font)
        return b

    def __text_size(self, text: str, font: FreeTypeFont) -> Tuple[int, int]:
        draw = self._get_draw()
        _, _, w, _ = draw.textbbox((0, 0), text, font, spacing=Grid.MULTI_LINE_SPACING)
        line_h = self.__text_height(font)  # single line height
        line_count = len(text.splitlines())
        h = line_h * line_count  # multi line height
        # TODO: Verify half of line spacing
        h += int((Grid.MULTI_LINE_SPACING / 2) * (line_count - 1))
        return w, h

    def _get_draw(self) -> ImageDraw.ImageDraw:
        if self._canvas:
            return ImageDraw.Draw(self._canvas)
        return ImageDraw.Draw(Image.new("RGBA", (1, 1)))

    def __cell_edge_align(
        self,
    ):  # pylint: disable=too-many-statements,too-many-branches
        style = self.get_cell_style(0, 0)
        if not style:
            style = copy.deepcopy(self._style)
        if not style.align.aligned():
            style.align = Align(left=True, top=True)
        self.set_cell_style(style, 0, 0)

        style = self.get_cell_style(0, self._cols - 1)
        if not style:
            style = copy.deepcopy(self._style)
        if not style.align.aligned():
            style.align = Align(right=True, top=True)
        self.set_cell_style(style, 0, self._cols - 1)

        style = self.get_cell_style(self._rows - 1, 0)
        if not style:
            style = copy.deepcopy(self._style)
        if not style.align.aligned():
            style.align = Align(left=True, bottom=True)
        self.set_cell_style(style, self._rows - 1, 0)

        style = self.get_cell_style(self._rows - 1, self._cols - 1)
        if not style:
            style = copy.deepcopy(self._style)
        if not style.align.aligned():
            style.align = Align(right=True, bottom=True)
        self.set_cell_style(style, self._rows - 1, self._cols - 1)

        for row in range(self._rows):
            style = self.get_cell_style(row, 0)
            if not style:
                style = copy.deepcopy(self._style)
            if not style.align.aligned():
                style.align.left = True
            self.set_cell_style(style, row, 0)
            if self._cols > 1:
                style = self.get_cell_style(row, self._cols - 1)
                if not style:
                    style = copy.deepcopy(self._style)
                if not style.align.aligned():
                    style.align.right = True
                self.set_cell_style(style, row, self._cols - 1)
        for col in range(self._cols):
            style = self.get_cell_style(0, col)
            if not style:
                style = copy.deepcopy(self._style)
            if not style.align.aligned():
                style.align.top = True
            self.set_cell_style(style, 0, col)
            if self._rows > 1:
                style = self.get_cell_style(self._rows - 1, col)
                if not style:
                    style = copy.deepcopy(self._style)
                if not style.align.aligned():
                    style.align.bottom = True
                self.set_cell_style(style, self._rows - 1, col)

    def __debug_mark(self, x: int, y: int, mark_len: int = 2) -> None:
        draw = self._get_draw()
        draw.line(
            (x - mark_len, y, x + mark_len, y),
            fill=(255, 0, 0),
        )
        draw.line(
            (x, y - mark_len, x, y + mark_len),
            fill=(255, 0, 0),
        )

    def __debug(self) -> None:  # pylint: disable=too-many-statements,too-many-locals
        draw = self._get_draw()
        dw = self._style.grid_border.column_border_width
        dh = self._style.grid_border.row_border_width
        h_l_o, h_r_o, v_t_o, v_b_o = self.__grid_border_pixel_correction()
        # Odd size pixel correction
        x_offset = 0
        y_offset = 0
        if self._width % 2:
            x_offset = 1
        if self._height % 2:
            y_offset = 1
        self.__debug_mark(
            self._origin_x - x_offset,
            self._origin_y - y_offset,
        )
        self.__debug_mark(
            self._origin_x + self._width,
            self._origin_y + self._height,
        )
        for row in range(self._rows):
            for col in range(self._cols):
                style = self._resolve_style(row, col)
                x, y, w, h, cx, cy, _, _ = self.__cell_size(row, col)
                self.__debug_mark(int(cx), int(cy))
                self.__debug_mark(
                    x + style.outer_margin.left + dw - h_l_o,
                    y + style.outer_margin.top + dh - v_t_o,
                )
                self.__debug_mark(
                    x + w - style.outer_margin.right - dw + h_r_o,
                    y + h - style.outer_margin.bottom - dh + v_b_o,
                )
                x1 = (
                    x
                    + style.outer_margin.left
                    + style.border.left
                    + style.margin.left
                    + dw
                    - h_l_o
                )
                y1 = (
                    y
                    + style.outer_margin.top
                    + style.border.top
                    + style.margin.top
                    + dh
                    - v_t_o
                )
                x2 = (
                    x
                    + w
                    - style.outer_margin.right
                    - style.border.right
                    - style.margin.right
                    - dw
                    + h_r_o
                )
                y2 = (
                    y
                    + h
                    - style.outer_margin.bottom
                    - style.border.bottom
                    - style.margin.bottom
                    - dh
                    + v_b_o
                )
                if x2 >= x1 and y2 >= y1:
                    draw.rectangle(
                        (x1, y1, x2, y2),
                        outline=Grid.DEBUG_COLOR,
                    )
                self.__debug_mark(
                    x
                    + style.outer_margin.left
                    + style.border.left
                    + style.margin.left
                    + dw
                    - h_l_o,
                    y
                    + style.outer_margin.top
                    + style.border.top
                    + style.margin.top
                    + dh
                    - v_t_o,
                )
                self.__debug_mark(
                    x
                    + w
                    - style.outer_margin.right
                    - style.border.right
                    - style.margin.right
                    - dw
                    + h_r_o,
                    y
                    + h
                    - style.outer_margin.bottom
                    - style.border.bottom
                    - style.margin.bottom
                    - dh
                    + v_b_o,
                )

    def image(
        self,
        debug: bool = False,
    ) -> Image.Image:
        return self.__render(canvas=None, debug=debug)

    def draw(
        self,
        image: Image.Image,
        origin_x: int = 0,
        origin_y: int = 0,
        debug: bool = False,
    ) -> None:
        self._canvas = image
        self._canvas_width = self._canvas.width
        self._canvas_height = self._canvas.height
        self.__render(self._canvas, origin_x, origin_y, debug=debug)

    def style(self, row: Optional[int] = None, col: Optional[int] = None) -> GridStyle:
        if row is None or col is None:  # Allow valid index 0
            return self._style
        return self._resolve_style(row, col)

    def get_grid_size(self) -> Tuple[int, int]:
        return self._width, self._height

    def set_grid_size(self, width: int, height: int) -> None:
        self._width = width
        self._height = height

    def set_grid_width(self, width: int) -> None:
        self._width = width

    def set_grid_height(self, height: int) -> None:
        self._height = height

    def set_style(self, style: GridStyle) -> None:
        self._style = copy.deepcopy(style)

    def set_cell_style(
        self, style: GridStyle, row: Optional[int] = None, col: Optional[int] = None
    ) -> None:
        if row is not None and col is not None:
            self._cell_style[row][col] = copy.deepcopy(style)

    def get_cell_style(self, row: int, col: int) -> Optional[GridStyle]:
        return self._cell_style[row][col]

    def set_row_cell_style(self, style: GridStyle, row: int) -> None:
        for col in range(self._cols):
            self.set_cell_style(style, row, col)

    def set_col_cell_style(self, style: GridStyle, col: int) -> None:
        for row in range(self._rows):
            self.set_cell_style(style, row, col)

    def set_odd_row_cell_style(self, style: GridStyle) -> None:
        for row in range(self._rows):
            if row % 2:
                self.set_row_cell_style(copy.deepcopy(style), row)

    def set_even_row_cell_style(self, style: GridStyle) -> None:
        for row in range(self._rows):
            if row % 2 == 0:
                self.set_row_cell_style(copy.deepcopy(style), row)

    def set_odd_col_cell_style(self, style: GridStyle) -> None:
        for row in range(self._rows):
            if row % 2:
                self.set_col_cell_style(copy.deepcopy(style), row)

    def set_even_col_cell_style(self, style: GridStyle) -> None:
        for row in range(self._rows):
            if row % 2 == 0:
                self.set_col_cell_style(copy.deepcopy(style), row)

    def set_odd_cell_style(self, style: GridStyle) -> None:
        for row in range(self._rows):
            for col in range(self._cols):
                if row % 2 and col % 2:
                    self.set_cell_style(style, row, col)

    def set_even_cell_style(self, style: GridStyle) -> None:
        for row in range(self._rows):
            for col in range(self._cols):
                if row % 2 == 0 and col % 2 == 0:
                    self.set_cell_style(style, row, col)

    def invert(self) -> None:
        self._data = self.invert_lists(self._data)
        self._cell_style = self.invert_lists(self._cell_style)
        self._cell_sizes = self.invert_lists(self._cell_sizes)
        self._cols = len(self._data[0])
        self._rows = len(self._data)

    @staticmethod
    def resolve_positions(x: int, y: int, w: int, h: int):
        return x, y, x + w, y + h

    @staticmethod
    def invert_lists(lists: List[List[Any]]):
        return [list(x) for x in zip(*lists)]

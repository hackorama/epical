import os
import sys
from datetime import datetime

from PIL import Image, ImageDraw

from test_utils import create_test_image, same_image_files, create_image

if os.path.exists("../lib"):
    sys.path.append("../lib")

from grid import Grid
from style import GridStyle


def draw_styles(debug=False):
    canvas = Image.new("RGBA", (1000, 2150), (255, 255, 255))
    draw = ImageDraw.Draw(canvas)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    draw.text((10, 5), f"STYLE TEST {now}", fill=(0, 0, 0))

    y = 30
    x = 10

    data = [["hello"], ["world"]]

    grid = Grid(data)
    grid.draw(canvas, x, y, debug=debug)

    x += 45

    grid = Grid(data)
    grid.style().set_grid_row_border(1, (0, 200, 200))
    grid.style().set_grid_column_border(1, (0, 200, 200))
    grid.draw(canvas, x, y, debug=debug)

    x += 45

    grid = Grid(data)
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.draw(canvas, x, y, debug=debug)

    x += 45

    grid = Grid(data)
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_grid_row_border(1, (0, 200, 200))
    grid.style().set_grid_column_border(1, (0, 200, 200))
    grid.draw(canvas, x, y, debug=debug)

    x += 50

    grid = Grid(data)
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_grid_row_border(1, (0, 200, 200))
    grid.style().set_grid_column_border(1, (0, 200, 200))
    grid.draw(canvas, x, y, debug=True)

    x += 50

    grid = Grid(data)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.draw(canvas, x, y, debug=debug)

    x += 45

    grid = Grid(data)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_grid_row_border(1, (0, 200, 200))
    grid.style().set_grid_column_border(1, (0, 200, 200))
    grid.draw(canvas, x, y, debug=debug)

    x += 45

    grid = Grid(data)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.draw(canvas, x, y, debug=debug)

    x += 45

    grid = Grid(data)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_grid_row_border(1, (0, 200, 200))
    grid.style().set_grid_column_border(1, (0, 200, 200))
    grid.draw(canvas, x, y, debug=debug)

    x += 50

    grid = Grid(data)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_grid_row_border(1, (0, 200, 200))
    grid.style().set_grid_column_border(1, (0, 200, 200))
    grid.draw(canvas, x, y, debug=True)

    x += 50

    grid = Grid(data)
    grid.style().set_margin(0, 0, 0, 0)
    grid.draw(canvas, x, y, debug=debug)

    x += 45

    grid = Grid(data)
    grid.style().set_margin(0, 0, 0, 0)
    grid.style().set_grid_row_border(1, (0, 200, 200))
    grid.style().set_grid_column_border(1, (0, 200, 200))
    grid.draw(canvas, x, y, debug=debug)

    x += 45

    grid = Grid(data)
    grid.style().set_margin(0, 0, 0, 0)
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.draw(canvas, x, y, debug=debug)

    x += 45

    grid = Grid(data)
    grid.style().set_margin(0, 0, 0, 0)
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_grid_row_border(1, (0, 200, 200))
    grid.style().set_grid_column_border(1, (0, 200, 200))
    grid.draw(canvas, x, y, debug=debug)

    x += 50

    grid = Grid(data)
    grid.style().set_margin(0, 0, 0, 0)
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_grid_row_border(1, (0, 200, 200))
    grid.style().set_grid_column_border(1, (0, 200, 200))
    grid.draw(canvas, x, y, debug=True)

    x += 50

    grid = Grid(data)
    grid.style().set_margin(0, 0, 0, 0)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.draw(canvas, x, y, debug=debug)

    x += 45

    grid = Grid(data)
    grid.style().set_margin(0, 0, 0, 0)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_grid_row_border(1, (0, 200, 200))
    grid.style().set_grid_column_border(1, (0, 200, 200))
    grid.draw(canvas, x, y, debug=debug)

    x += 45

    grid = Grid(data)
    grid.style().set_margin(0, 0, 0, 0)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.draw(canvas, x, y, debug=debug)

    x += 45

    grid = Grid(data)
    grid.style().set_margin(0, 0, 0, 0)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_grid_row_border(1, (0, 200, 200))
    grid.style().set_grid_column_border(1, (0, 200, 200))
    grid.draw(canvas, x, y, debug=debug)

    x += 50

    grid = Grid(data)
    grid.style().set_margin(0, 0, 0, 0)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_grid_row_border(1, (0, 200, 200))
    grid.style().set_grid_column_border(1, (0, 200, 200))
    grid.draw(canvas, x, y, debug=True)

    x = 10
    y += 70

    data = [["The", "quick", "brown"], ["fox", "jumps", "over"], ["the", "lazy", "dog"]]

    grid = Grid(data)
    grid.style().set_margin(5, 5, 5, 5).set_font_size(20)
    grid.draw(canvas, x, y, debug=debug)

    x += 250

    grid = Grid(data)
    grid.style().set_grid_border(1, (0, 0, 0)).set_margin(5, 5, 5, 5).set_font_size(20)
    grid.draw(canvas, x, y, debug=debug)

    x += 250

    grid = Grid(data)
    grid.style().set_grid_row_border(1, (200, 100, 100))
    grid.style().set_margin(5, 5, 5, 5).set_font_size(20)
    grid.draw(canvas, x, y, debug=debug)

    x += 250

    grid = Grid(data)
    grid.style().set_grid_column_border(1, (100, 200, 100))
    grid.style().set_margin(5, 5, 5, 5).set_font_size(20)
    grid.draw(canvas, x, y, debug=debug)

    x = 10
    y += 150

    grid = Grid(data)
    grid.style().set_grid_column_border(5, (100, 200, 100))
    grid.style().set_grid_row_border(5, (200, 100, 100))
    grid.style().set_margin(1, 1, 1, 1).set_font_size(20)
    grid.style().set_grid_row_border_priority()
    grid.draw(canvas, x, y, debug=debug)

    x += 250

    grid = Grid(data)
    grid.style().set_grid_column_border(5, (100, 200, 100))
    grid.style().set_grid_row_border(5, (200, 100, 100))
    grid.style().set_margin(1, 1, 1, 1).set_font_size(20)
    grid.style().set_grid_column_border_priority()
    grid.draw(canvas, x, y, debug=debug)

    x += 250

    grid = Grid(data)
    grid.style().set_margin(5, 5, 5, 5).set_font_size(20)
    grid.style().set_grid_column_border_priority()
    grid.style().set_cell_border(
        3, 3, 3, 3, (100, 200, 100), (100, 200, 100), (200, 100, 100), (200, 100, 100)
    )
    grid.style().set_grid_row_border_priority()
    grid.draw(canvas, x, y, debug=debug)

    x += 250

    grid = Grid(data)
    grid.style().set_margin(5, 5, 5, 5).set_font_size(20)
    grid.style().set_grid_column_border_priority()
    grid.style().set_cell_border(
        3, 3, 3, 3, (100, 200, 100), (100, 200, 100), (200, 100, 100), (200, 100, 100)
    )
    grid.style().set_grid_column_border_priority()
    grid.draw(canvas, x, y, debug=debug)

    x = 10
    y += 150

    grid = Grid(data)
    grid.style().set_margin(5, 5, 5, 5).set_font_size(20)
    grid.style(1, 0).set_bg_color((137, 207, 240))
    grid.draw(canvas, x, y, debug=debug)

    x += 250
    grid = Grid(data)
    grid.style().set_margin(5, 5, 5, 5).set_font_size(20)
    grid.style(1, 0).set_cell_border(1, 1, 1, 1)
    grid.draw(canvas, x, y, debug=debug)

    x += 250
    grid = Grid(data)
    grid.style().set_margin(5, 5, 5, 5).set_font_size(20)
    grid.style(1, 0).set_cell_border(1, 1, 1, 1).set_bg_color((240, 255, 255))
    grid.style(1, 0).set_font_color((0, 150, 255))
    grid.draw(canvas, x, y, debug=debug)

    x += 250
    grid = Grid(data)
    grid.style().set_margin(5, 5, 5, 5).set_font_size(20)
    grid.style(1, 0).set_cell_border(
        left=0, right=0, top=0, bottom=5, bottom_color=(255, 0, 0)
    )
    grid.draw(canvas, x, y, debug=debug)

    x = 10
    y += 150

    grid = Grid(data)
    grid.style().set_margin(5, 5, 5, 5).set_font_size(20)
    grid.style(0, 0).set_bg_color((200, 200, 200))
    grid.style(0, 1).set_bg_color((200, 200, 200))
    grid.style(0, 2).set_bg_color((200, 200, 200))
    grid.draw(canvas, x, y, debug=debug)

    x += 250
    grid = Grid(data)
    grid.style().set_margin(5, 5, 5, 5).set_font_size(20)
    grid.style().set_grid_column_border(1, (200, 200, 200))
    grid.style().set_grid_row_border(1, (200, 200, 200))
    grid.style(0, 0).set_bg_color((200, 200, 200))
    grid.style(0, 1).set_bg_color((200, 200, 200))
    grid.style(0, 2).set_bg_color((200, 200, 200))
    grid.draw(canvas, x, y, debug=debug)

    x += 250
    grid = Grid(data)
    grid.style().set_margin(5, 5, 5, 5).set_font_size(20)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style(0, 0).set_bg_color((200, 200, 200))
    grid.style(0, 1).set_bg_color((200, 200, 200))
    grid.style(0, 2).set_bg_color((200, 200, 200))
    grid.draw(canvas, x, y, debug=debug)

    x += 250
    grid = Grid(data)
    grid.style().set_margin(5, 5, 5, 5).set_font_size(20)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_grid_column_border(4, (200, 200, 200))
    grid.style().set_grid_row_border(4, (200, 200, 200))
    grid.style(0, 0).set_bg_color((200, 200, 200))
    grid.style(0, 1).set_bg_color((200, 200, 200))
    grid.style(0, 2).set_bg_color((200, 200, 200))
    grid.draw(canvas, x, y, debug=debug)

    x = 10
    y += 150

    grid = Grid(data)
    grid.style().set_margin(5, 5, 5, 5).set_font_size(20)
    grid.style().set_cell_border(
        1, 1, 1, 1, (0, 150, 255), (0, 150, 255), (0, 150, 255), (0, 150, 255)
    )
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.draw(canvas, x, y, debug=debug)

    x += 250
    grid = Grid(data)
    grid.style().set_margin(5, 5, 5, 5).set_font_size(20)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_cell_border(1, 1, 1, 1).set_bg_color((240, 255, 255))
    grid.draw(canvas, x, y, debug=debug)

    x += 250
    grid = Grid(data)
    grid.style().set_margin(5, 5, 5, 5).set_font_size(20)
    grid.style().set_outer_margin(4, 4, 4, 4)
    grid.style().set_cell_border(
        1, 1, 1, 1, (0, 150, 255), (0, 150, 255), (0, 150, 255), (0, 150, 255)
    )
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.draw(canvas, x, y, debug=debug)

    x += 250

    x -= 10
    y -= 10
    grid = Grid(data)
    grid.style().set_margin(5, 5, 5, 5).set_font_size(20)
    grid.style().set_outer_margin(5, 5, 5, 5)
    grid.style().set_cell_border(3, 3, 3, 3).set_bg_color((240, 255, 255))
    grid.draw(canvas, x, y, debug=debug)
    y += 5

    y -= 10
    x = 10
    y += 180

    data = [["The quick brown fox"], ["jumps over"], ["the lazy dog"]]
    grid = Grid(data)
    grid.style().set_margin(5, 5, 5, 5).set_font_size(20)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.draw(canvas, x, y, debug=debug)

    x += 250
    grid = Grid(data)
    grid.style().set_margin(5, 5, 5, 5).set_font_size(20)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.style().set_align(left=True)
    grid.draw(canvas, x, y, debug=debug)

    x += 250
    grid = Grid(data)
    grid.style().set_margin(5, 5, 5, 5).set_font_size(20)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.style().set_align(right=True)
    grid.draw(canvas, x, y, debug=debug)

    x += 250
    grid = Grid(data)
    grid.style().set_margin(5, 5, 5, 5).set_font_size(20)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.style(1, 0).set_align(right=True)
    grid.style(2, 0).set_align(left=True)
    grid.draw(canvas, x, y, debug=debug)

    x = 10
    y += 150

    data = [["The", "quick", "brown"], ["fox", "jumps", "over"], ["the", "lazy", "dog"]]

    grid = Grid(data)
    grid.style().set_margin(5, 5, 5, 5).set_font_size(16)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_grid_column_border(5, (0, 0, 0))
    grid.style().set_grid_row_border(5, (0, 0, 0))
    grid.style().set_cell_border(
        3, 0, 3, 0, left_color=(200, 200, 200), top_color=(150, 150, 150)
    )
    grid.draw(canvas, x, y, debug=debug)

    x += 250

    grid = Grid(data)
    grid.style().set_margin(5, 5, 5, 5).set_font_size(16)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_grid_column_border(5, (0, 0, 0))
    grid.style().set_grid_row_border(5, (0, 0, 0))
    grid.style().set_cell_border(
        3, 0, 3, 0, left_color=(200, 200, 200), top_color=(150, 150, 150)
    )
    grid.style(0, 1).set_bg_color((240, 240, 255))
    grid.draw(canvas, x, y, debug=debug)

    x += 250

    drop_shadow = GridStyle()
    drop_shadow.set_grid_column_border(5, (0, 0, 0))

    drop_shadow = GridStyle()
    drop_shadow.set_margin(5, 5, 5, 5).set_font_size(16)
    drop_shadow.set_outer_margin(0, 0, 0, 0)
    drop_shadow.set_grid_column_border(5, (0, 0, 0))
    drop_shadow.set_grid_row_border(5, (0, 0, 0))
    drop_shadow.set_cell_border(
        3, 0, 3, 0, left_color=(200, 200, 200), top_color=(150, 150, 150)
    )

    selection = GridStyle()
    selection.set_margin(5, 5, 5, 5).set_font_size(16)
    selection.set_outer_margin(0, 0, 0, 0)
    selection.set_grid_column_border(5, (0, 0, 0))
    selection.set_grid_row_border(5, (0, 0, 0))
    selection.set_cell_border(
        3, 0, 3, 0, left_color=(200, 200, 200), top_color=(150, 150, 150)
    )
    selection.set_bg_color((240, 240, 255))

    grid = Grid(data)
    grid.set_style(drop_shadow)
    grid.draw(canvas, x, y, debug=debug)

    x += 250

    grid.set_style(drop_shadow)
    grid.set_cell_style(selection, 0, 1)
    grid.draw(canvas, x, y, debug=debug)

    x = 10
    y += 150

    child_grid = Grid([[1, 2], [3, 4]])
    child_grid.style().set_cell_border(1, 1, 1, 1)
    child_grid.style().set_margin(1, 1, 1, 1).set_font_size(16)
    data = [["Default child grid"], [child_grid]]
    grid = Grid(data)
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_margin(1, 1, 1, 1).set_font_size(16)
    grid.draw(canvas, x, y, debug=debug)

    x += 250

    child_grid = Grid([[1, 2], [3, 4]])
    child_grid.style().set_cell_border(1, 1, 1, 1)
    child_grid.style().set_margin(1, 1, 1, 1).set_font_size(16)
    child_grid.style().set_elastic_fit(True)
    data = [["Expand child grid to fit"], [child_grid]]
    grid = Grid(data)
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_margin(1, 1, 1, 1).set_font_size(16)
    grid.draw(canvas, x, y, debug=debug)

    x += 250
    child_grid = Grid([[12345]])
    child_grid_2 = Grid([[55], [55]])
    child_grid.style().set_cell_border(1, 1, 1, 1)
    child_grid_2.style().set_cell_border(1, 1, 1, 1)
    data = [
        [1111, 2, "3\n3", 4],
        [child_grid_2, 66, 7, 9],
        [10, "1\n1", 12, child_grid],
    ]
    grid = Grid(data)
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_margin(1, 1, 1, 1).set_font_size(16)
    grid.draw(canvas, x, y, debug=debug)

    x += 250
    data = [
        [1111, 2, "3\n3", 4],
        [child_grid_2, 66, 7, 9],
        [10, "1\n1", 12, child_grid],
    ]
    grid = Grid(data)
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_margin(1, 1, 1, 1).set_font_size(16)
    grid.style().set_edge_fit(True)
    grid.draw(canvas, x, y, debug=debug)

    x = 10
    y += 170

    data = [[1, 2, 3], [4, "auto", 6], [7, 8, 9]]

    grid = Grid(data)
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(3, 3, 3, 3).set_font_size(16)
    grid.draw(canvas, x, y, debug=debug)
    w = grid._width
    h = grid._height

    x += 150
    data = [[1, 2, 3], [4, "auto+", 6], [7, 8, 9]]
    grid = Grid(data, width=w * 2, height=h * 2)
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(3, 3, 3, 3).set_font_size(16)
    grid.draw(canvas, x, y, debug=debug)

    x += 200
    data = [[1, 2, 3], [4, "auto-", 6], [7, 8, 9]]
    grid = Grid(data, width=int(w / 2), height=int(h / 2))
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(3, 3, 3, 3).set_font_size(16)
    grid.draw(canvas, x, y, debug=debug)

    x += 200
    data = [[1, 2, 3], [4, "fixed", 6], [7, 8, 9]]
    grid = Grid(data, 150, height=150)
    grid.style().set_fixed_fit(True)
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(3, 3, 3, 3).set_font_size(16)
    grid.draw(canvas, x, y, debug=debug)

    x += 250
    data = [[1, 2, 3], [4, "fixed\noverflow", 6], [7, 8, 9]]
    grid = Grid(data, 100, height=100)
    grid.style().set_fixed_fit(True)
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(3, 3, 3, 3).set_font_size(16)
    grid.draw(canvas, x, y, debug=debug)

    x = 10
    y += 200

    data = [
        ["Sunday"],
        ["Monday"],
        ["Tuesday"],
        ["Thursday"],
        ["Friday"],
        ["Saturday"],
    ]

    class MyCustomGridWithDataTransform(Grid):
        def _get_cell_data(self, row, col):
            return self._data[row][col][:3].upper()

    grid = MyCustomGridWithDataTransform(data)
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_margin(1, 1, 1, 1).set_font_size(16)
    grid.draw(canvas, x, y, debug=debug)

    x += 70

    class MyCustomGridWithCustomDrawing(Grid):
        def _draw_cell(
            self,
            row: int = 0,
            col: int = 0,
            x1: int = 1,
            y1: int = 1,
            x2: int = 1,
            y2: int = 1,
            debug: bool = False,
        ) -> None:
            if self._data[row][col] == "Sunday":
                draw = self._get_draw()
                draw.ellipse(
                    (x1 + 4, y1 + 4, x2 - 4, y2 - 4),
                    fill=(255, 240, 240),
                    outline=(255, 0, 0),
                )
            super()._draw_cell(row, col, x1, y1, x2, y2, debug)

    grid = MyCustomGridWithCustomDrawing(data)
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_margin(1, 1, 1, 1).set_font_size(16)
    grid.draw(canvas, x, y, debug=debug)

    x += 100

    class MyCustomGridWithDataTransformAndCustomDrawing(MyCustomGridWithCustomDrawing):
        def _get_cell_data(self, row, col):
            return self._data[row][col][:3].upper()

    grid = MyCustomGridWithDataTransformAndCustomDrawing(data)
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_margin(1, 1, 1, 1).set_font_size(16)
    grid.draw(canvas, x, y, debug=debug)

    x += 70

    data = [["X", "Y", "Z"], [1, 2, 3]]
    grid = Grid(data)
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_margin(2, 2, 2, 2).set_font_size(16)
    grid.style(0, 1).set_bg_color((255, 200, 200))
    grid.draw(canvas, x, y, debug=debug)

    x += 70

    grid.invert()
    grid.draw(canvas, x, y, debug=debug)

    x += 100

    child_grid = Grid([["FOO"], ["BAR"]])
    child_grid.style().set_grid_column_border(1, (0, 0, 0))
    child_grid.style().set_grid_row_border(1, (0, 0, 0))

    an_image = create_test_image()
    data = [["FOO", 42, 3.14], [an_image, "FOO\nBAR", child_grid]]
    grid = Grid(data)
    grid.style().set_margin(5, 5, 5, 5).set_font_size(20)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.draw(canvas, x, y, debug=debug)

    x += 200
    child_grid = Grid(data)
    child_grid.style().set_margin(5, 5, 5, 5).set_font_size(20)
    child_grid.style().set_grid_column_border(1, (0, 0, 0))
    child_grid.style().set_grid_row_border(1, (0, 0, 0))
    data = [["The quick brown fox\njumps over\nthe lazy dog", child_grid]]
    grid = Grid(data)
    grid.style().set_margin(5, 5, 5, 5).set_font_size(20)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.style(0, 0).set_font_size(10)
    grid.draw(canvas, x, y, debug=debug)

    y += 200
    x = 10

    data = [["A", 5], ["B", 4], ["C", 9], ["D", 3]]
    grid = Grid(data)
    grid.style().set_margin(5, 5, 5, 5)
    grid.style().set_outer_margin(0, 0, 4, 4)
    grid.style().set_align(right=True)
    grid.style(0, 1).set_cell_border(
        0, 50, 0, 0, right_color=(255, 255, 255)
    ).set_bg_color((255, 0, 0)).set_font_color((255, 255, 255))
    grid.style(1, 1).set_cell_border(
        0, 60, 0, 0, right_color=(255, 255, 255)
    ).set_bg_color((255, 0, 0)).set_font_color((255, 255, 255))
    grid.style(2, 1).set_cell_border(
        0, 10, 0, 0, right_color=(255, 255, 255)
    ).set_bg_color((255, 0, 0)).set_font_color((255, 255, 255))
    grid.style(3, 1).set_cell_border(
        0, 70, 0, 0, right_color=(255, 255, 255)
    ).set_bg_color((255, 0, 0)).set_font_color((255, 255, 255))
    grid.draw(canvas, x, y, debug=debug)

    x += 150

    data = [[5, 4, 9, 3], ["A", "B", "C", "D"]]
    grid = Grid(data)
    grid.style().set_margin(5, 5, 5, 1)
    grid.style().set_outer_margin(4, 4, 0, 0)
    grid.style().set_align(bottom=True)
    grid.style(0, 0).set_cell_border(
        0, 0, 50, 0, top_color=(255, 255, 255)
    ).set_bg_color((255, 0, 0)).set_font_color((255, 255, 255))
    grid.style(0, 1).set_cell_border(
        0, 0, 60, 0, top_color=(255, 255, 255)
    ).set_bg_color((255, 0, 0)).set_font_color((255, 255, 255))
    grid.style(0, 2).set_cell_border(
        0, 0, 10, 0, top_color=(255, 255, 255)
    ).set_bg_color((255, 0, 0)).set_font_color((255, 255, 255))
    grid.style(0, 3).set_cell_border(
        0, 0, 70, 0, top_color=(255, 255, 255)
    ).set_bg_color((255, 0, 0)).set_font_color((255, 255, 255))
    grid.draw(canvas, x, y, debug=debug)

    y += 150
    x -= 150

    data = [[5, 4, 9, 3], ["A", "B", "C", "D"]]
    grid = Grid(data)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(5, 5, 5, 0)
    grid.style(0, 0).set_cell_border(50, 0, 0, 0, left_color=(255, 0, 0)).set_bg_color(
        (255, 0, 0)
    ).set_font_color((255, 255, 255))
    grid.style(0, 1).set_cell_border(40, 0, 0, 0, left_color=(0, 200, 0)).set_bg_color(
        (0, 200, 0)
    ).set_font_color((255, 255, 255))
    grid.style(0, 2).set_cell_border(90, 0, 0, 0, left_color=(0, 0, 200)).set_bg_color(
        (0, 0, 200)
    ).set_font_color((255, 255, 255))
    grid.style(0, 3).set_cell_border(
        30, 0, 0, 0, left_color=(0, 200, 200)
    ).set_bg_color((0, 200, 200)).set_font_color((255, 255, 255))
    grid.draw(canvas, x, y, debug=debug)

    x += 150
    y -= 150

    x += 150

    data = [["S", "F"], [4, 9]]
    grid = Grid(data)
    grid.style().set_margin(1, 1, 1, 1).set_font_size(60)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style(0, 0).set_bg_color((170, 0, 0)).set_margin(20, 10, 0, 0).set_font_color(
        (255, 255, 255)
    )
    grid.style(0, 1).set_bg_color((170, 0, 0)).set_margin(10, 20, 0, 0).set_font_color(
        (255, 255, 255)
    )
    grid.style(1, 0).set_bg_color((173, 153, 93)).set_margin(20, 10, 0, 0)
    grid.style(1, 1).set_bg_color((173, 153, 93)).set_margin(10, 20, 0, 0)
    grid.draw(canvas, x, y, debug=debug)

    x += 150

    data = [
        ["A quick brown fox jumps over the lazy dog"],
        ["A slow fox jumps over the quick brown dog"],
        ["A lazy brown dog jumps over the quick fox"],
    ]
    grid = Grid(data)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style(0, 0).set_cell_border(5, 1, 1, 0, left_color=(200, 0, 0))
    grid.style(1, 0).set_cell_border(5, 1, 0, 0, left_color=(0, 0, 200))
    grid.style(2, 0).set_cell_border(5, 1, 0, 1, left_color=(0, 200, 0))
    grid.draw(canvas, x, y, debug=debug)

    y += 80

    time_grid = Grid([["10:16"], ["Friday 13"]])
    time_grid.style().set_bg_color((255, 255, 0))
    time_grid.style().set_margin(5, 5, 0, 5)
    time_grid.style().set_outer_margin(0, 0, 0, 0)
    time_grid.style().set_align(top=True)
    time_grid.style(0, 0).set_font_size(32)
    time_grid.style(1, 0).set_font_size(16)

    messages_grid = Grid(
        [
            ["72 Sunny, High of 74"],
            ["3 Meetings, Next one in 2 hours"],
            ["4 New messages"],
        ]
    )
    messages_grid.style().set_bg_color((0, 0, 0))
    messages_grid.style().set_font_color((255, 255, 255))
    messages_grid.style().set_margin(100, 0, 0, 0)
    messages_grid.style().set_align(right=True)
    messages_grid.style().set_font_size(14)
    messages_grid.style(0, 0).set_font_size(18)

    main_grid = Grid([[time_grid, messages_grid]])
    main_grid.style().set_bg_color((0, 0, 0))
    main_grid.style().set_margin(10, 10, 0, 10)
    main_grid.style().set_outer_margin(0, 0, 0, 0)
    main_grid.style().set_align(top=True)

    main_grid.draw(canvas, x, y, debug=debug)

    y -= 80

    x += 280

    data = [["N", "E"], ["W", "S"]]
    grid = Grid(data, 70, 70)
    grid.style().set_fixed_fit(True)
    grid.style().set_margin(1, 1, 1, 1).set_font_size(20)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style(0, 0).set_font_color((255, 0, 0))
    grid.style(0, 0).set_margin(0, 5, 0, 5).set_cell_border(0, 2, 0, 2).set_align(
        left=True, top=True
    )
    grid.style(0, 1).set_margin(5, 0, 0, 5).set_cell_border(2, 0, 0, 2).set_align(
        right=True, top=True
    )
    grid.style(1, 0).set_margin(0, 5, 5, 0).set_cell_border(0, 2, 2, 0).set_align(
        left=True, bottom=True
    )
    grid.style(1, 1).set_margin(5, 0, 5, 0).set_cell_border(2, 0, 2, 0).set_align(
        right=True, bottom=True
    )
    grid.draw(canvas, x, y, debug=debug)

    compact = GridStyle()
    compact.set_margin(0, 0, 0, 0).set_outer_margin(0, 0, 0, 0).set_bg_color(
        (0, 161, 225)
    )

    block = create_image(6, 6, (0, 161, 225))
    grid1 = Grid([[block]])
    grid1.set_style(compact)
    grid1.style().set_grid_column_border(5, (0, 191, 255))
    grid1.style().set_grid_row_border(5, (0, 191, 255))

    x += 100
    grid1.draw(canvas, x, y, debug=debug)

    grid2 = Grid([[grid1]])
    grid2.set_style(compact)
    grid2.style().set_grid_column_border(5, (0, 181, 245))
    grid2.style().set_grid_row_border(5, (0, 181, 245))

    grid3 = Grid([[grid2]])
    grid3.set_style(compact)
    grid3.style().set_grid_column_border(5, (0, 171, 235))
    grid3.style().set_grid_row_border(5, (0, 171, 235))

    grid4 = Grid([[grid3]])
    grid4.set_style(compact)
    grid4.style().set_grid_column_border(5, (0, 161, 225))
    grid4.style().set_grid_row_border(5, (0, 161, 225))

    x += 20
    grid4.draw(canvas, x, y, debug=debug)

    x += 65
    grid1.style().set_elastic_fit(True)
    grid2.style().set_elastic_fit(True)
    grid3.style().set_elastic_fit(True)
    grid4.style().set_elastic_fit(True)
    grid4.draw(canvas, x, y, debug=debug)

    x = 10
    y += 200

    data = ["01234567890 abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ !@#$%^&"]
    grid = Grid(data)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.draw(canvas, x, y, debug=debug)

    x = 10
    y += 40

    data = [[1, 2], [3, 4]]

    grid = Grid(data)
    grid.style().set_grid_column_border(1, (0, 0, 255))
    grid.style().set_grid_row_border(1, (0, 0, 255))
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_bg_color((200, 200, 200))
    grid.draw(canvas, x, y, debug=debug)

    x += 50

    grid = Grid(data)
    grid.style().set_grid_column_border(2, (0, 0, 255))
    grid.style().set_grid_row_border(2, (0, 0, 255))
    grid.style().set_cell_border(2, 2, 2, 2)
    grid.style().set_bg_color((200, 200, 200))
    grid.draw(canvas, x, y, debug=debug)

    x += 60

    grid = Grid(data)
    grid.style().set_grid_column_border(3, (0, 0, 255))
    grid.style().set_grid_row_border(3, (0, 0, 255))
    grid.style().set_cell_border(3, 3, 3, 3)
    grid.style().set_bg_color((200, 200, 200))
    grid.draw(canvas, x, y, debug=debug)

    x += 70

    grid = Grid(data)
    grid.style().set_grid_column_border(4, (0, 0, 255))
    grid.style().set_grid_row_border(4, (0, 0, 255))
    grid.style().set_cell_border(4, 4, 4, 4)
    grid.style().set_bg_color((200, 200, 200))
    grid.draw(canvas, x, y, debug=debug)

    x += 80

    grid = Grid(data)
    grid.style().set_grid_column_border(4, (0, 0, 255))
    grid.style().set_grid_row_border(4, (0, 0, 255))
    grid.style().set_cell_border(4, 4, 3, 4)
    grid.style().set_bg_color((200, 200, 200))
    grid.draw(canvas, x, y, debug=debug)

    x += 80

    grid = Grid(data)
    grid.style().set_grid_column_border(3, (0, 0, 255))
    grid.style().set_grid_row_border(4, (0, 0, 255))
    grid.style().set_cell_border(4, 4, 3, 4)
    grid.style().set_bg_color((200, 200, 200))
    grid.draw(canvas, x, y, debug=debug)

    x += 70

    grid = Grid(data)
    grid.style().set_grid_column_border(3, (0, 0, 255))
    grid.style().set_grid_row_border(3, (0, 0, 255))
    grid.style().set_cell_border(3, 4, 3, 4)
    grid.style().set_bg_color((200, 200, 200))
    grid.draw(canvas, x, y, debug=debug)

    x += 80

    grid = Grid(data)
    grid.style().set_grid_column_border(7, (0, 0, 255))
    grid.style().set_grid_row_border(10, (0, 0, 255))
    grid.style().set_cell_border(5, 8, 5, 8)
    grid.style().set_outer_margin(6, 6, 6, 6).set_font_size(14)
    grid.style().set_bg_color((200, 200, 200))
    grid.draw(canvas, x, y, debug=debug)

    x += 110

    grid = Grid(data)
    grid.style().set_grid_column_border(8, (0, 0, 0))
    grid.style().set_grid_row_border(13, (200, 200, 200))
    grid.style().set_cell_border(
        8, 5, 5, 8, (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255)
    )
    grid.style().set_bg_color((200, 200, 200))
    grid.style().set_grid_column_border_priority()
    grid.style().set_outer_margin(5, 5, 5, 5).set_font_size(16)
    grid.draw(canvas, x, y, debug=debug)

    x += 110

    grid = Grid([["abgABG"]])
    grid.style().set_font_size(8)
    grid.style().set_cell_border(2, 4, 8, 16)
    grid.style().set_margin(16, 8, 4, 2).set_font_size(16)
    grid.style().set_outer_margin(4, 2, 8, 16)
    grid.style().set_grid_column_border(7, (200, 0, 0))
    grid.style().set_grid_row_border(4, (0, 0, 200))
    grid.draw(canvas, x, y, debug=True)

    y += 100

    grid = Grid([["abgABG"]])
    grid.style().set_font_size(8)
    grid.style().set_cell_border(15, 7, 3, 1)
    grid.style().set_margin(1, 3, 7, 15).set_font_size(16)
    grid.style().set_outer_margin(15, 7, 3, 1)
    grid.style().set_grid_column_border(4, (200, 0, 0))
    grid.style().set_grid_row_border(7, (0, 0, 200))
    grid.draw(canvas, x, y, debug=True)

    y -= 160

    x += 130

    data = [[""]]
    grid = Grid(data)
    grid.draw(canvas, x, y, debug=True)

    data = [[]]
    grid = Grid(data)
    grid.draw(canvas, x, y, debug=True)

    data = [[], [1, 2]]
    grid = Grid(data)
    grid.draw(canvas, x, y, debug=True)

    x += 10

    data = [[1], []]
    grid = Grid(data)
    grid.draw(canvas, x, y, debug=True)

    x += 10

    data = [[1], [1, 2]]
    grid = Grid(data)
    grid.draw(canvas, x, y, debug=True)

    x = 10
    y += 140

    data = [[1, 2], [3, 4]]
    grid = Grid(data)
    grid.style().set_grid_column_border(4, (0, 0, 0))
    grid.style().set_grid_row_border(3, (200, 200, 200))
    grid.style().set_cell_border(
        1, 2, 3, 4, (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255)
    )
    grid.style().set_bg_color((200, 200, 200))
    grid.draw(canvas, x, y, debug=debug)

    x += 60

    grid = Grid(data)
    grid.style().set_grid_column_border(3, (0, 0, 0))
    grid.style().set_grid_row_border(4, (200, 200, 200))
    grid.style().set_cell_border(
        1, 2, 3, 4, (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255)
    )
    grid.style().set_bg_color((200, 200, 200))
    grid.draw(canvas, x, y, debug=debug)

    x += 60

    grid = Grid(data)
    grid.style().set_grid_column_border(4, (0, 0, 0))
    grid.style().set_grid_row_border(3, (200, 200, 200))
    grid.style().set_cell_border(
        4, 3, 2, 1, (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255)
    )
    grid.style().set_bg_color((200, 200, 200))
    grid.draw(canvas, x, y, debug=debug)

    x += 60

    grid = Grid(data)
    grid.style().set_grid_column_border(4, (0, 0, 0))
    grid.style().set_grid_row_border(3, (200, 200, 200))
    grid.style().set_cell_border(
        4, 3, 2, 1, (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255)
    )
    grid.style().set_bg_color((200, 200, 200))
    grid.draw(canvas, x, y, debug=debug)

    x += 60

    grid = Grid(data)
    grid.style().set_grid_column_border(4, (0, 0, 0))
    grid.style().set_grid_row_border(3, (200, 200, 200))
    grid.style().set_cell_border(
        1, 2, 3, 4, (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255)
    )
    grid.style().set_bg_color((200, 200, 200))
    grid.style().set_grid_column_border_priority()
    grid.draw(canvas, x, y, debug=debug)

    x += 60

    grid = Grid(data)
    grid.style().set_grid_column_border(3, (0, 0, 0))
    grid.style().set_grid_row_border(4, (200, 200, 200))
    grid.style().set_cell_border(
        1, 2, 3, 4, (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255)
    )
    grid.style().set_bg_color((200, 200, 200))
    grid.style().set_grid_column_border_priority()
    grid.draw(canvas, x, y, debug=debug)

    x += 50

    grid = Grid(data)
    grid.style().set_grid_column_border(4, (0, 0, 0))
    grid.style().set_grid_row_border(3, (200, 200, 200))
    grid.style().set_cell_border(
        4, 3, 2, 1, (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255)
    )
    grid.style().set_bg_color((200, 200, 200))
    grid.style().set_grid_column_border_priority()
    grid.draw(canvas, x, y, debug=debug)

    x += 60

    grid = Grid(data)
    grid.style().set_grid_column_border(4, (0, 0, 0))
    grid.style().set_grid_row_border(3, (200, 200, 200))
    grid.style().set_cell_border(
        4, 3, 2, 1, (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255)
    )
    grid.style().set_bg_color((200, 200, 200))
    grid.style().set_grid_column_border_priority()
    grid.draw(canvas, x, y, debug=debug)

    y -= 80
    x += 470

    data = [[1, 2], [3, 4]]

    grid = Grid(data)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.style().set_cell_border(
        1, 1, 1, 1, (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)
    )
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_bg_color((0, 255, 0))
    grid.draw(canvas, x, y, debug=debug)

    x += 50
    grid = Grid(data)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.style().set_cell_border(
        1, 1, 1, 1, (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)
    )
    grid.style().set_outer_margin(1, 1, 1, 1)
    grid.style().set_bg_color((0, 255, 0))
    grid.draw(canvas, x, y, debug=debug)

    y += 50
    x -= 50

    grid = Grid(data)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.style().set_cell_border(
        1, 2, 1, 2, (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)
    )
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_bg_color((0, 255, 0))
    grid.draw(canvas, x, y, debug=debug)

    x += 50

    grid = Grid(data)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.style().set_cell_border(
        2, 1, 2, 1, (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)
    )
    grid.style().set_outer_margin(1, 1, 1, 1)
    grid.style().set_bg_color((0, 255, 0))
    grid.draw(canvas, x, y, debug=debug)

    y += 60
    x -= 50

    grid = Grid(data)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.style().set_cell_border(
        1, 2, 3, 4, (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)
    )
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_bg_color((0, 255, 0))
    grid.draw(canvas, x, y, debug=debug)

    x += 50

    grid = Grid(data)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.style().set_cell_border(
        4, 3, 2, 1, (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)
    )
    grid.style().set_outer_margin(1, 1, 1, 1)
    grid.style().set_bg_color((0, 255, 0))
    grid.draw(canvas, x, y, debug=debug)

    return canvas


def test_styles():
    name = "style"
    canvas = draw_styles()
    canvas.save(f"./actual/test_{name}.png", "PNG")
    assert same_image_files(
        f"./expected/test_{name}.png", f"./actual/test_{name}.png", name
    )

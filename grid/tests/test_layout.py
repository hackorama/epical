import os
import sys
from datetime import datetime

from PIL import Image, ImageDraw

if os.path.exists("../lib"):
    sys.path.append("../lib")

from test_utils import same_image_files, text_align
from grid import Grid
from style import Align, Margin, GridStyle


def draw_layouts(debug=False):
    canvas = Image.new("RGBA", (600, 1650), (255, 255, 255))
    draw = ImageDraw.Draw(canvas)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    draw.text((10, 5), f"LAYOUT TEST {now}", fill=(0, 0, 0))

    # generate or load test image from file: test_img = Image.open("test_image.png")
    test_img = Image.new("RGBA", (50, 50))
    draw = ImageDraw.Draw(test_img)
    draw.rectangle((0, 0, 50, 50), fill=(0, 0, 255))
    draw.text((5, 5), "TEST")
    draw.text((5, 20), "IMAGE")

    x1 = 30
    y = 30
    x2 = x1
    grid = Grid(
        data=[
            ["one", "two", "three"],
            ["four", "five", "six"],
            ["sever", "eight", "nine"],
        ],
        width=100,
        height=100,
    )
    grid.draw(canvas, x2, y, debug=debug)

    x2 += 120
    grid = Grid(
        data=[
            ["one", "two", "three"],
            ["four", "five", "six"],
            ["sever", "eight", "nine"],
        ],
        width=100,
        height=100,
    )
    grid.style().set_edge_fit(True)
    grid.draw(canvas, x2, y, debug=debug)

    x2 += 120
    text_align(canvas, x2, y)

    y += 130
    x2 = 250

    child_grid_1 = Grid(data=[[11, 2], [3, 44]])
    child_grid_2 = Grid(data=[["1", 2], [3, 4]])
    child_grid_2.style().set_elastic_fit(True)
    child_grid_3 = Grid(data=[["1", 2], [3, 4]])
    child_grid_3.style().set_elastic_fit(True).set_edge_fit(True)
    child_grid_4 = Grid(data=[["1", 2], [3, 4]], width=40, height=20)
    child_grid_4.style().set_fixed_fit(True)
    child_grid_5 = Grid(data=[[111, 2], [3, 4444]])
    child_grid_5.style().set_edge_fit(True)
    grid = Grid(
        data=[
            [child_grid_1, 2, test_img],
            ["a", "foobar", "c\nd\ne"],
            ["", child_grid_3, child_grid_4],
            [1.0, child_grid_5, child_grid_2],
        ],
    )
    grid.draw(canvas, x1, y, debug=debug)
    grid = Grid(
        data=[
            [child_grid_1, 2, test_img],
            ["a", "foobar", "c\nd\ne"],
            ["", child_grid_3, child_grid_4],
            [1.0, child_grid_5, child_grid_2],
        ],
        width=300,
    )
    grid.draw(canvas, x2, y, debug=debug)

    y += 250
    child_grid_1 = Grid(data=[["1", 2], [3, 4]])
    child_grid_2 = Grid(data=[["1", 2], [3, 4]])
    child_grid_2.style().set_elastic_fit(True)
    grid = Grid(
        data=[
            [child_grid_1, 2, test_img],
            ["a", "foobar", "c\nd\ne"],
            [1.0, 2.0, child_grid_2],
        ],
        width=100,
        height=100,
    )
    grid.style().set_fixed_fit(True)
    grid.draw(canvas, x1, y, debug=debug)
    grid = Grid(
        data=[
            [child_grid_1, 2, test_img],
            ["a", "foobar", "c\nd\ne"],
            [1.0, 2.0, child_grid_2],
        ],
        width=300,
        height=100,
    )
    grid.style().set_fixed_fit(True)
    grid.draw(canvas, x2, y, debug=debug)

    y += 160
    child_grid_1 = Grid(data=[["1", 2], [3, 4]])
    child_grid_2 = Grid(data=[["1", 2], [3, 4]])
    child_grid_2.style().set_elastic_fit(True)
    grid = Grid(
        data=[
            [child_grid_1, 2, test_img],
            ["a", "foobar", "c\nd\ne"],
            [1.0, 2.0, child_grid_2],
        ],
    )
    grid.style().set_edge_fit(True)
    grid.draw(canvas, x1, y, debug=debug)
    grid = Grid(
        data=[
            [child_grid_1, 2, test_img],
            ["a", "foobar", "c\nd\ne"],
            [1.0, 2.0, child_grid_2],
        ],
        width=300,
    )
    grid.style().set_elastic_fit(True).set_edge_fit(True)
    grid.draw(canvas, x2, y, debug=debug)

    y += 180
    child_grid_1 = Grid(data=[["1", 2], [3, 4]])
    child_grid_2 = Grid(data=[["1", 2], [3, 4]])
    child_grid_2.style().set_elastic_fit(True).set_edge_fit(True)
    grid = Grid(
        data=[
            [child_grid_1, 2, test_img],
            ["a", "foobar", "c\nd\ne"],
            [1.0, 2.0, child_grid_2],
        ],
    )
    grid.style().set_elastic_fit(True).set_edge_fit(True)
    grid.draw(canvas, x1, y, debug=debug)
    grid = Grid(
        data=[
            [child_grid_1, 2, test_img],
            ["a", "foo bar baz qux quux garply waldo", "c\nd\ne"],
            [1.0, 2.0, child_grid_2],
        ],
        width=300,
    )
    grid.style().set_elastic_fit(True).set_edge_fit(True)
    grid.draw(canvas, x2, y, debug=debug)

    y += 200
    child_grid_1 = Grid(data=[["1", 2], [3, 4]])
    child_grid_2 = Grid(data=[["1", 2], [3, 4]])
    grid = Grid(
        data=[
            [child_grid_1, 2, test_img],
            ["a", "foobar", "c\nd\ne"],
            [1.0, 2.0, child_grid_2],
        ],
    )
    grid.set_cell_style(
        GridStyle(align=Align(bottom=True), margin=Margin(bottom=5)), 0, 0
    )
    grid.set_cell_style(GridStyle(align=Align(right=True)), 0, 1)
    grid.set_cell_style(
        GridStyle(align=Align(left=True), margin=Margin(5, 5, 5, 5)), 0, 2
    )
    grid.set_cell_style(GridStyle(align=Align(left=True, bottom=True)), 1, 0)
    grid.set_cell_style(
        GridStyle(
            align=Align(top=True, right=True),
            margin=Margin(5, 5, 5, 5),
        ).set_font_size(16),
        1,
        1,
    )
    grid.set_cell_style(GridStyle(align=Align(left=True)), 1, 2)
    grid.set_cell_style(
        GridStyle(margin=Margin(5, 5, 5, 5))
        .set_font_size(20)
        .set_font_color((0, 128, 0)),
        2,
        0,
    )
    child_grid_2.style().set_elastic_fit(True).set_edge_fit(True)
    child_grid_2.style(1, 1).set_align(left=True).set_font_color((255, 0, 0))
    grid.style().set_elastic_fit(True).set_edge_fit(True)
    grid.draw(canvas, x1, y, debug=debug)

    child_grid_1 = Grid(data=[["1", 2], [3, 4]])
    child_grid_2 = Grid(data=[["1", 2], [3, 4]])
    grid = Grid(
        data=[
            [child_grid_1, 2, test_img],
            ["a", "foo bar baz qux", "c\nd\ne"],
            [1.0, 2.0, child_grid_2],
        ],
        width=300,
    )
    grid.set_cell_style(
        GridStyle(align=Align(bottom=True), margin=Margin(bottom=5)), 0, 0
    )
    grid.set_cell_style(GridStyle(align=Align(right=True)), 0, 1)
    grid.set_cell_style(
        GridStyle(align=Align(left=True), margin=Margin(5, 5, 5, 5)), 0, 2
    )
    grid.set_cell_style(GridStyle(align=Align(left=True, bottom=True)), 1, 0)
    grid.set_cell_style(
        GridStyle(
            align=Align(top=True, right=True),
            margin=Margin(5, 5, 5, 5),
        ).set_font_size(20),
        1,
        1,
    )
    grid.set_cell_style(GridStyle(align=Align(left=True)), 1, 2)
    grid.set_cell_style(
        GridStyle(margin=Margin(5, 5, 5, 5), font_color=(0, 128, 0), font_size=20),
        2,
        0,
    )
    child_grid_2.set_cell_style(
        GridStyle(align=Align(left=True), font_color=(255, 0, 0)), 1, 1
    )
    child_grid_2.style().set_elastic_fit(True).set_edge_fit(True)
    grid.style().set_elastic_fit(True).set_edge_fit(True)
    grid.draw(canvas, x2, y, debug=debug)

    y += 200
    x3 = x1
    grid_style = GridStyle(
        font_size=16, font_color=(255, 0, 0), margin=Margin(5, 5, 5, 5)
    )
    cell_style = GridStyle(font_size=8, margin=Margin(5, 5, 5, 5))
    grid = Grid(
        data=[
            ["a", "quick", "brown"],
            ["fox", "jumps", "over"],
            ["the", "lazy", "dog"],
        ],
    )
    grid.set_style(grid_style)
    # replace cell style
    grid.set_cell_style(cell_style, 1, 1)
    # update cell style
    grid.style(1, 2).set_font_size(8)
    grid.draw(canvas, x3, y, debug=debug)

    x3 += 150
    grid = Grid(
        data=[
            ["foo", "bar", "baz"],
        ],
    )
    grid.set_style(GridStyle(margin=Margin(5, 5, 5, 5)))
    # update grid style
    grid.style().set_font_color((0, 0, 256))
    grid.draw(canvas, x3, y, debug=debug)

    x3 += 100
    grid = Grid(
        data=[
            ["foo", "bar", "baz"],
        ],
    )
    grid.set_style(GridStyle(margin=Margin(5, 5, 5, 5)))
    wide_margin = GridStyle(margin=Margin(left=20, right=20, top=2, bottom=2))
    right_align = GridStyle(align=Align(right=True))
    grid.set_cell_style(wide_margin, 0, 1)
    grid.draw(canvas, x3, y, debug=debug)

    x3 += 130
    grid = Grid(
        data=[
            ["foo", "bar", "baz"],
        ],
    )
    grid.set_style(GridStyle(font_color=(255, 0, 0)))
    # replace grid style, removes margins
    green_margin = GridStyle().set_font_color((0, 128, 0)).set_margin(5)
    grid.set_style(green_margin)
    grid.draw(canvas, x3, y, debug=debug)

    y += 130
    x3 = x1
    grid = Grid(
        data=[
            [
                "a quick brown fox jumps over the lazy dog",
                "a quick brown fox \njumps over\n the lazy dog",
                "a\nquick\nbrown\nfox\njumps\nover\nthe\nlazy\ndog",
            ],
        ],
    )
    grid.set_cell_style(right_align, 0, 1)
    grid.draw(canvas, x3, y, debug=debug)

    x3 += 400

    class MyCustomGrid(Grid):
        def _get_cell_data(self, row, col):
            return self._data[row][col][:3].upper()

    grid = MyCustomGrid(
        data=[
            ["Sunday"],
            ["Monday"],
            ["Tuesday"],
            ["Thursday"],
            ["Friday"],
            ["Saturday"],
        ],
    )
    grid.set_style(GridStyle(margin=Margin(5, 5, 5, 5)))
    grid.draw(canvas, x3, y, debug=debug)

    x3 += 50

    class MyCustomGrid2(Grid):
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
                draw.ellipse((x1, y1, x2, y2), fill=(255, 200, 200))
            super()._draw_cell(row, col, x1, y1, x2, y2, debug)

    grid = MyCustomGrid2(
        data=[
            ["Sunday"],
            ["Monday"],
            ["Tuesday"],
            ["Thursday"],
            ["Friday"],
            ["Saturday"],
        ],
    )
    grid.set_style(GridStyle(margin=Margin(5, 5, 5, 5)))
    grid.draw(canvas, x3, y, debug=debug)

    y += 180
    grid = Grid(
        data=[
            ["MALAYALAM മലയാളം", "JAPANESE 日本語", "EMOJI 🙂△"],
        ],
    )
    grid.draw(canvas, x1, y, debug=debug)

    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    red = GridStyle(bg_color=(255, 0, 0))
    green = GridStyle(bg_color=(0, 128, 0))

    y += 60
    x3 = x1

    grid = Grid(data)
    grid.set_even_row_cell_style(green)
    grid.draw(canvas, x3, y, debug=debug)

    x3 += 50
    grid = Grid(data)
    grid.set_odd_row_cell_style(green)
    grid.draw(canvas, x3, y, debug=debug)

    x3 += 50
    grid = Grid(data)
    grid.set_even_col_cell_style(green)
    grid.draw(canvas, x3, y, debug=debug)

    x3 += 50
    grid = Grid(data)
    grid.set_odd_col_cell_style(green)
    grid.draw(canvas, x3, y, debug=debug)

    x3 += 50
    grid = Grid(data)
    grid.set_even_cell_style(green)
    grid.draw(canvas, x3, y, debug=debug)

    x3 += 50
    grid = Grid(data)
    grid.set_odd_cell_style(green)
    grid.draw(canvas, x3, y, debug=debug)

    x1 += 300

    data = [[1, 2, 3], ["one", "two", "three"]]
    grid = Grid(data)
    grid.draw(canvas, x1, y, debug=debug)

    x1 += 100

    grid = Grid(data)
    grid.invert()
    grid.draw(canvas, x1, y, debug=debug)

    return canvas


def test_layout():
    name = "layout"
    canvas = draw_layouts(True)
    canvas.save(f"./actual/test_{name}.png", "PNG")
    assert same_image_files(
        f"./expected/test_{name}.png", f"./actual/test_{name}.png", name
    )

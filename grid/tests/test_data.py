import os
import sys

from PIL import Image, ImageDraw

from test_utils import same_image_files

if os.path.exists("../lib"):
    sys.path.append("../lib")

from grid import Grid


def check_data(canvas, x, y, data, debug=False):
    grid = Grid(data)
    grid.style().set_grid_border(1, (0, 0, 0))
    grid.draw(canvas, x, y, debug=debug)


def draw_data():
    canvas = Image.new("RGBA", (500, 100), (255, 255, 255))
    x = y = 10
    check_data(canvas, x, y, None)
    x += 30
    check_data(canvas, x, y, [])
    x += 30
    check_data(canvas, x, y, [[]])
    x += 30
    check_data(canvas, x, y, [[None]])
    x += 40
    check_data(canvas, x, y, [[None, 1]])
    x += 50
    check_data(canvas, x, y, [[None, 1], None])
    x += 50
    check_data(canvas, x, y, [[None], [1]])
    x += 50
    check_data(canvas, x, y, [[None, 1], [1, None]])
    x += 50
    check_data(canvas, x, y, [[None, 1, [None]], [1, None]])
    x += 50
    check_data(canvas, x, y, "")
    x += 30
    check_data(canvas, x, y, [""])
    x += 30
    check_data(canvas, x, y, ["123"])
    return canvas


def test_data():
    name = "data"
    canvas = draw_data()
    canvas.save(f"./actual/test_{name}.png", "PNG")
    assert same_image_files(
        f"./expected/test_{name}.png", f"./actual/test_{name}.png", name
    )

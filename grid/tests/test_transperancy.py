import os
import sys

from PIL import Image

from test_utils import same_image_files

if os.path.exists("../lib"):
    sys.path.append("../lib")

from grid import Grid


def draw_transparency():
    canvas = Image.new("RGBA", (350, 60), (0, 200, 200))

    x = y = 5

    # transparent by default
    grid = Grid([[1, 2], [3, 4]])
    grid.draw(canvas, x, y)

    x += 50

    # set whole grid bg
    grid = Grid([[1, 2], [3, 4]])
    grid.style().set_bg_color((255, 255, 255))
    grid.draw(canvas, x, y)

    x += 50

    # set partial bg
    grid = Grid([[1, 2], [3, 4]])
    grid.style(0, 0).set_bg_color((255, 255, 255))
    grid.draw(canvas, x, y)

    x += 50

    # borders
    grid = Grid([[1, 2], [3, 4]])
    grid.style().set_grid_border(1, (255, 0, 0))
    grid.draw(canvas, x, y)

    x += 50

    # borders
    grid = Grid([[1, 2], [3, 4]])
    grid.style().set_grid_border(1, (255, 0, 0))
    grid.style(0, 0).set_bg_color((255, 255, 255))
    grid.draw(canvas, x, y)

    x += 50

    # margins
    grid = Grid([[1, 2], [3, 4]])
    grid.style().set_bg_color((255, 255, 255))
    grid.style().set_margin(0, 0, 0, 0)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.draw(canvas, x, y)

    x += 50

    # borders + margins
    grid = Grid([[1, 2], [3, 4]])
    grid.style().set_bg_color((255, 255, 255))
    grid.style().set_grid_border(1, (255, 0, 0))
    grid.style().set_margin(0, 0, 0, 0)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.draw(canvas, x, y)

    return canvas


def test_transparency():
    name = "transparency"
    canvas = draw_transparency()
    canvas.save(f"./actual/test_{name}.png", "PNG")
    assert same_image_files(
        f"./expected/test_{name}.png", f"./actual/test_{name}.png", name
    )

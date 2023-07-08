import os
import sys
from datetime import datetime

from PIL import Image, ImageDraw

if os.path.exists("../lib"):
    sys.path.append("../lib")

from grid import Grid
from test_utils import same_image_files, create_image


def margins(canvas, x, y, l, r, t, b, debug=False):
    image = create_image()
    data = [[image, image], [image, image]]

    grid = Grid(data)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.style().set_cell_border(
        1, 1, 1, 1, (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)
    )
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_bg_color((0, 255, 0))
    grid.style().set_margin(l, r, t, b)
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
    grid.style().set_margin(l, r, t, b)
    grid.draw(canvas, x, y, debug=debug)

    x += 50

    grid = Grid(data)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.style().set_cell_border(
        1, 2, 1, 2, (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)
    )
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_bg_color((0, 255, 0))
    grid.style().set_margin(l, r, t, b)
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
    grid.style().set_margin(l, r, t, b)
    grid.draw(canvas, x, y, debug=debug)

    x += 50

    grid = Grid(data)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.style().set_cell_border(
        1, 2, 3, 4, (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)
    )
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_bg_color((0, 255, 0))
    grid.style().set_margin(l, r, t, b)
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
    grid.style().set_margin(l, r, t, b)
    grid.draw(canvas, x, y, debug=debug)


def mixed_margins(
    canvas, x, y, l, r, t, b, al=False, ar=False, at=False, ab=False, debug=False
):
    sx = x
    sy = y

    image1 = create_image(2, 2)
    image2 = create_image(2, 16)
    image3 = create_image(16, 2)
    image4 = create_image()
    data = [[image1, image2], [image3, image4]]

    grid = Grid(data)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.style().set_cell_border(
        1, 1, 1, 1, (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)
    )
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_bg_color((0, 255, 0))
    grid.style().set_margin(l, r, t, b)
    grid.style().set_align(al, ar, at, ab)
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
    grid.style().set_margin(l, r, t, b)
    grid.style().set_align(al, ar, at, ab)
    grid.draw(canvas, x, y, debug=debug)

    x += 50

    grid = Grid(data)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.style().set_cell_border(
        1, 2, 1, 2, (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)
    )
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_bg_color((0, 255, 0))
    grid.style().set_margin(l, r, t, b)
    grid.style().set_align(al, ar, at, ab)
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
    grid.style().set_margin(l, r, t, b)
    grid.style().set_align(al, ar, at, ab)
    grid.draw(canvas, x, y, debug=debug)

    x += 60

    grid = Grid(data)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.style().set_cell_border(
        1, 2, 3, 4, (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)
    )
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_bg_color((0, 255, 0))
    grid.style().set_margin(l, r, t, b)
    grid.style().set_align(al, ar, at, ab)
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
    grid.style().set_margin(l, r, t, b)
    grid.style().set_align(al, ar, at, ab)
    grid.draw(canvas, x, y, debug=debug)

    image1 = create_image(3, 3)
    image2 = create_image(3, 15)
    image3 = create_image(15, 3)
    image4 = create_image()
    data = [[image1, image2], [image3, image4]]

    x = sx
    y = sy + 60

    grid = Grid(data)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.style().set_cell_border(
        1, 1, 1, 1, (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)
    )
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_bg_color((0, 255, 0))
    grid.style().set_margin(l, r, t, b)
    grid.style().set_align(al, ar, at, ab)
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
    grid.style().set_margin(l, r, t, b)
    grid.style().set_align(al, ar, at, ab)
    grid.draw(canvas, x, y, debug=debug)

    x += 50

    grid = Grid(data)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.style().set_cell_border(
        1, 2, 1, 2, (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)
    )
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_bg_color((0, 255, 0))
    grid.style().set_margin(l, r, t, b)
    grid.style().set_align(al, ar, at, ab)
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
    grid.style().set_margin(l, r, t, b)
    grid.style().set_align(al, ar, at, ab)
    grid.draw(canvas, x, y, debug=debug)

    x += 50

    grid = Grid(data)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.style().set_cell_border(
        1, 2, 3, 4, (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)
    )
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_bg_color((0, 255, 0))
    grid.style().set_margin(l, r, t, b)
    grid.style().set_align(al, ar, at, ab)
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
    grid.style().set_margin(l, r, t, b)
    grid.style().set_align(al, ar, at, ab)
    grid.draw(canvas, x, y, debug=debug)


def draw_align(debug=False):
    canvas = Image.new("RGBA", (670, 1300), (255, 255, 255))
    draw = ImageDraw.Draw(canvas)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    draw.text((10, 5), f"ALIGN TEST {now}", fill=(0, 0, 0))

    x = 10
    y = 20

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

    x += 50

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

    x += 50

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

    image = create_image()
    data = [[image, image], [image, image]]

    x = 10
    y = 100

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

    x += 50

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

    x += 50

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

    image4 = create_image()
    image2 = create_image(2, 16)
    image3 = create_image(16, 2)
    image1 = create_image(2, 2)
    data = [[image1, image2], [image3, image4]]

    x = 10
    y = 150

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

    x += 50

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

    x += 50

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

    image1 = create_image(3, 3)
    image2 = create_image(3, 15)
    image3 = create_image(15, 3)
    image4 = create_image()
    data = [[image1, image2], [image3, image4]]

    x = 10
    y = 200

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

    x += 50

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

    x += 50

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
    x = 10
    y = 270

    child = Grid([["1234"]])
    data = [[child, child], [child, child]]

    grid = Grid(data)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.style().set_cell_border(
        1, 1, 1, 1, (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)
    )
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_bg_color((0, 255, 0))
    grid.draw(canvas, x, y, debug=debug)

    x += 100
    grid = Grid(data)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.style().set_cell_border(
        1, 1, 1, 1, (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)
    )
    grid.style().set_outer_margin(1, 1, 1, 1)
    grid.style().set_bg_color((0, 255, 0))
    grid.draw(canvas, x, y, debug=debug)

    x += 100

    grid = Grid(data)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.style().set_cell_border(
        1, 2, 1, 2, (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)
    )
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_bg_color((0, 255, 0))
    grid.draw(canvas, x, y, debug=debug)

    x = 10
    y = 350

    grid = Grid(data)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.style().set_cell_border(
        2, 1, 2, 1, (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)
    )
    grid.style().set_outer_margin(1, 1, 1, 1)
    grid.style().set_bg_color((0, 255, 0))
    grid.draw(canvas, x, y, debug=debug)

    x += 100

    grid = Grid(data)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.style().set_cell_border(
        1, 2, 3, 4, (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)
    )
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_bg_color((0, 255, 0))
    grid.draw(canvas, x, y, debug=debug)

    x += 100

    grid = Grid(data)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.style().set_cell_border(
        4, 3, 2, 1, (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)
    )
    grid.style().set_outer_margin(1, 1, 1, 1)
    grid.style().set_bg_color((0, 255, 0))
    grid.draw(canvas, x, y, debug=debug)

    x = 10
    y = 450

    child1 = Grid([["1"]])
    child2 = Grid([["1\n2\n3\n4"]])
    child3 = Grid([["1234"]])
    child4 = Grid([["12"], ["34"]])
    data = [[child1, child2], [child3, child4]]

    grid = Grid(data)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.style().set_cell_border(
        1, 1, 1, 1, (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)
    )
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_bg_color((0, 255, 0))
    grid.draw(canvas, x, y, debug=debug)

    x += 100
    grid = Grid(data)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.style().set_cell_border(
        1, 1, 1, 1, (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)
    )
    grid.style().set_outer_margin(1, 1, 1, 1)
    grid.style().set_bg_color((0, 255, 0))
    grid.draw(canvas, x, y, debug=debug)

    x += 100

    grid = Grid(data)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.style().set_cell_border(
        1, 2, 1, 2, (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)
    )
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_bg_color((0, 255, 0))
    grid.draw(canvas, x, y, debug=debug)

    x = 10
    y = 600

    grid = Grid(data)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.style().set_cell_border(
        2, 1, 2, 1, (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)
    )
    grid.style().set_outer_margin(1, 1, 1, 1)
    grid.style().set_bg_color((0, 255, 0))
    grid.draw(canvas, x, y, debug=debug)

    x += 100

    grid = Grid(data)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.style().set_cell_border(
        1, 2, 3, 4, (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)
    )
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_bg_color((0, 255, 0))
    grid.draw(canvas, x, y, debug=debug)

    x += 100

    grid = Grid(data)
    grid.style().set_grid_column_border(1, (0, 0, 0))
    grid.style().set_grid_row_border(1, (0, 0, 0))
    grid.style().set_cell_border(
        4, 3, 2, 1, (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)
    )
    grid.style().set_outer_margin(1, 1, 1, 1)
    grid.style().set_bg_color((0, 255, 0))
    grid.draw(canvas, x, y, debug=debug)

    margins(canvas, 340, 20, 0, 0, 0, 0, debug)
    margins(canvas, 340, 70, 1, 1, 1, 1, debug)
    margins(canvas, 340, 120, 3, 3, 3, 3, debug)
    margins(canvas, 340, 170, 4, 4, 4, 4, debug)
    margins(canvas, 340, 220, 1, 2, 3, 4, debug)
    margins(canvas, 340, 270, 4, 3, 2, 1, debug)

    mixed_margins(canvas, 340, 330, 0, 0, 0, 0, debug)
    mixed_margins(canvas, 340, 440, 1, 1, 1, 1, debug)
    mixed_margins(canvas, 340, 550, 1, 2, 3, 4, debug)
    mixed_margins(canvas, 340, 670, 4, 3, 2, 1, debug)

    x = 10
    y = 800
    mixed_margins(canvas, x, y, 0, 0, 0, 0, al=True, debug=debug)
    y += 130
    mixed_margins(canvas, x, y, 0, 0, 0, 0, ar=True, debug=debug)
    y += 130
    mixed_margins(canvas, x, y, 0, 0, 0, 0, at=True, debug=debug)
    y += 130
    mixed_margins(canvas, x, y, 0, 0, 0, 0, ab=True, debug=debug)

    x = 340
    y = 800
    mixed_margins(canvas, x, y, 0, 0, 0, 0, al=True, at=True, debug=debug)
    y += 130
    mixed_margins(canvas, x, y, 0, 0, 0, 0, al=True, ab=True, debug=debug)
    y += 130
    mixed_margins(canvas, x, y, 0, 0, 0, 0, ar=True, at=True, debug=debug)
    y += 130
    mixed_margins(canvas, x, y, 0, 0, 0, 0, ar=True, ab=True, debug=debug)

    return canvas


def test_align():
    name = "align"
    canvas = draw_align()
    canvas.save(f"./actual/test_{name}.png", "PNG")
    assert same_image_files(
        f"./expected/test_{name}.png", f"./actual/test_{name}.png", name
    )

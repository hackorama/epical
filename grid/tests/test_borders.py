import os
import sys
from datetime import datetime

from PIL import Image, ImageDraw

if os.path.exists("../lib"):
    sys.path.append("../lib")

from grid import Grid
from test_utils import same_image_files, create_image


def draw_borders(debug=False):
    canvas = Image.new("RGBA", (400, 740), (255, 255, 255))
    draw = ImageDraw.Draw(canvas)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    draw.text((10, 5), f"BORDERS TEST {now}", fill=(0, 0, 0))

    x = 10
    y = 20
    red = create_image(8, 8, color=(255, 0, 0))
    green = create_image(8, 8, color=(0, 255, 0))
    blue = create_image(8, 8, color=(0, 0, 255))
    yellow = create_image(8, 8, color=(255, 0, 255))

    grid = Grid([[red, green], [blue, yellow]])
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(0, 0, 0, 0)
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(1, 1, 1, 1)
    grid.draw(canvas, x, y, debug)

    red = create_image(7, 7, color=(255, 0, 0))
    green = create_image(7, 7, color=(0, 255, 0))
    blue = create_image(7, 7, color=(0, 0, 255))
    yellow = create_image(7, 7, color=(255, 0, 255))

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(0, 0, 0, 0)
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(1, 1, 1, 1)
    grid.draw(canvas, x, y, debug)

    x = 10
    y += 50

    red = create_image(8, 8, color=(255, 0, 0))
    green = create_image(8, 8, color=(0, 255, 0))
    blue = create_image(8, 8, color=(0, 0, 255))
    yellow = create_image(8, 8, color=(255, 0, 255))

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_grid_border(1, (0, 0, 0))
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_grid_border(1, (0, 0, 0))
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(0, 0, 0, 0)
    grid.style().set_grid_border(1, (0, 0, 0))
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(1, 1, 1, 1)
    grid.style().set_grid_border(1, (0, 0, 0))
    grid.draw(canvas, x, y, debug)

    red = create_image(7, 7, color=(255, 0, 0))
    green = create_image(7, 7, color=(0, 255, 0))
    blue = create_image(7, 7, color=(0, 0, 255))
    yellow = create_image(7, 7, color=(255, 0, 255))

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_grid_border(1, (0, 0, 0))
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_grid_border(1, (0, 0, 0))
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(0, 0, 0, 0)
    grid.style().set_grid_border(1, (0, 0, 0))
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(1, 1, 1, 1)
    grid.style().set_grid_border(1, (0, 0, 0))
    grid.draw(canvas, x, y, debug)

    x = 10
    y += 50

    red = create_image(8, 8, color=(255, 0, 0))
    green = create_image(8, 8, color=(0, 255, 0))
    blue = create_image(8, 8, color=(0, 0, 255))
    yellow = create_image(8, 8, color=(255, 0, 255))

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_grid_border(2, (0, 0, 0))
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_grid_border(2, (0, 0, 0))
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(0, 0, 0, 0)
    grid.style().set_grid_border(2, (0, 0, 0))
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(1, 1, 1, 1)
    grid.style().set_grid_border(2, (0, 0, 0))
    grid.draw(canvas, x, y, debug)

    red = create_image(7, 7, color=(255, 0, 0))
    green = create_image(7, 7, color=(0, 255, 0))
    blue = create_image(7, 7, color=(0, 0, 255))
    yellow = create_image(7, 7, color=(255, 0, 255))

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_grid_border(2, (0, 0, 0))
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_grid_border(2, (0, 0, 0))
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(0, 0, 0, 0)
    grid.style().set_grid_border(2, (0, 0, 0))
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(1, 1, 1, 1)
    grid.style().set_grid_border(2, (0, 0, 0))
    grid.draw(canvas, x, y, debug)

    x = 10
    y += 50

    red = create_image(8, 8, color=(255, 0, 0))
    green = create_image(8, 8, color=(0, 255, 0))
    blue = create_image(8, 8, color=(0, 0, 255))
    yellow = create_image(8, 8, color=(255, 0, 255))

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_grid_border(1, (0, 0, 0))
    grid.style().set_cell_border(3, 3, 3, 3)
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_grid_border(1, (0, 0, 0))
    grid.style().set_cell_border(3, 3, 3, 3)
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(0, 0, 0, 0)
    grid.style().set_grid_border(1, (0, 0, 0))
    grid.style().set_cell_border(3, 3, 3, 3)
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(1, 1, 1, 1)
    grid.style().set_grid_border(1, (0, 0, 0))
    grid.style().set_cell_border(3, 3, 3, 3)
    grid.draw(canvas, x, y, debug)

    red = create_image(7, 7, color=(255, 0, 0))
    green = create_image(7, 7, color=(0, 255, 0))
    blue = create_image(7, 7, color=(0, 0, 255))
    yellow = create_image(7, 7, color=(255, 0, 255))

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_grid_border(1, (0, 0, 0))
    grid.style().set_cell_border(3, 3, 3, 3)
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_grid_border(1, (0, 0, 0))
    grid.style().set_cell_border(3, 3, 3, 3)
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(0, 0, 0, 0)
    grid.style().set_grid_border(1, (0, 0, 0))
    grid.style().set_cell_border(3, 3, 3, 3)
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(1, 1, 1, 1)
    grid.style().set_grid_border(1, (0, 0, 0))
    grid.style().set_cell_border(3, 3, 3, 3)
    grid.draw(canvas, x, y, debug)

    x = 10
    y += 50

    red = create_image(8, 8, color=(255, 0, 0))
    green = create_image(8, 8, color=(0, 255, 0))
    blue = create_image(8, 8, color=(0, 0, 255))
    yellow = create_image(8, 8, color=(255, 0, 255))

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_grid_border(2, (0, 0, 0))
    grid.style().set_cell_border(2, 2, 2, 2)
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_grid_border(2, (0, 0, 0))
    grid.style().set_cell_border(2, 2, 2, 2)
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(0, 0, 0, 0)
    grid.style().set_grid_border(2, (0, 0, 0))
    grid.style().set_cell_border(2, 2, 2, 2)
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(1, 1, 1, 1)
    grid.style().set_grid_border(2, (0, 0, 0))
    grid.style().set_cell_border(2, 2, 2, 2)
    grid.draw(canvas, x, y, debug)

    red = create_image(7, 7, color=(255, 0, 0))
    green = create_image(7, 7, color=(0, 255, 0))
    blue = create_image(7, 7, color=(0, 0, 255))
    yellow = create_image(7, 7, color=(255, 0, 255))

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_grid_border(2, (0, 0, 0))
    grid.style().set_cell_border(2, 2, 2, 2)
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_grid_border(2, (0, 0, 0))
    grid.style().set_cell_border(2, 2, 2, 2)
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(0, 0, 0, 0)
    grid.style().set_grid_border(2, (0, 0, 0))
    grid.style().set_cell_border(2, 2, 2, 2)
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(1, 1, 1, 1)
    grid.style().set_grid_border(2, (0, 0, 0))
    grid.style().set_cell_border(2, 2, 2, 2)
    grid.draw(canvas, x, y, debug)

    x = 10
    y += 50

    red = create_image(8, 8, color=(255, 0, 0))
    green = create_image(8, 8, color=(0, 255, 0))
    blue = create_image(8, 8, color=(0, 0, 255))
    yellow = create_image(8, 8, color=(255, 0, 255))

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_grid_border(3, (0, 0, 0))
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_grid_border(3, (0, 0, 0))
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(0, 0, 0, 0)
    grid.style().set_grid_border(3, (0, 0, 0))
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(1, 1, 1, 1)
    grid.style().set_grid_border(3, (0, 0, 0))
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.draw(canvas, x, y, debug)

    red = create_image(7, 7, color=(255, 0, 0))
    green = create_image(7, 7, color=(0, 255, 0))
    blue = create_image(7, 7, color=(0, 0, 255))
    yellow = create_image(7, 7, color=(255, 0, 255))

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_grid_border(3, (0, 0, 0))
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_grid_border(3, (0, 0, 0))
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(0, 0, 0, 0)
    grid.style().set_grid_border(3, (0, 0, 0))
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[red, green], [blue, yellow]])
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(1, 1, 1, 1)
    grid.style().set_grid_border(3, (0, 0, 0))
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.draw(canvas, x, y, debug)
    x = 10
    y += 50

    data = [[111, "2\n2"], ["3\n3", 4444]]

    grid = Grid(data)
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_margin(0, 0, 0, 0)
    grid.style().set_align(left=True)
    grid.draw(canvas, x, y, debug)

    x += 70

    grid = Grid(data)
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_margin(0, 0, 0, 0)
    grid.style().set_align(right=True)
    grid.draw(canvas, x, y, debug)

    x += 70

    grid = Grid(data)
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_margin(0, 0, 0, 0)
    grid.style().set_align(top=True)
    grid.draw(canvas, x, y, debug)

    x += 70

    grid = Grid(data)
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_margin(0, 0, 0, 0)
    grid.style().set_align(bottom=True)
    grid.draw(canvas, x, y, debug)

    x = 10
    y += 100

    red = create_image(7, 8, color=(255, 0, 0))
    child = Grid([[red]])
    child.style().set_cell_border(
        2, 2, 2, 2, (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0)
    )
    child.style().set_margin(0, 0, 0, 0)
    child.style().set_outer_margin(0, 0, 0, 0)

    child.draw(canvas, x, y + 50)

    grid = Grid([[child]])
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.draw(canvas, x, y, debug)

    x += 20

    grid = Grid([[child]])
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_margin(0, 0, 0, 0)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.draw(canvas, x, y, debug)

    x += 20

    grid = Grid([[child]])
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_margin(1, 1, 1, 1)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.draw(canvas, x, y, debug)

    x += 20

    grid = Grid([[child], ["111"]])
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_margin(0, 0, 0, 0)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_align(left=True)
    grid.draw(canvas, x, y, debug)

    x += 30

    grid = Grid([[child], ["111"]])
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_margin(0, 0, 0, 0)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_align(right=True)
    grid.draw(canvas, x, y, debug)

    x += 30

    grid = Grid([[child, "1\n1"]])
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_margin(0, 0, 0, 0)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_align(top=True)
    grid.draw(canvas, x, y, debug)

    x += 30

    grid = Grid([[child, "1\n1"], ["11", "22"]])
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_margin(0, 0, 0, 0)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_align(left=True, top=True)
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[child, "1\n1"], ["11", "22"]])
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_margin(0, 0, 0, 0)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_align(right=True, bottom=True)
    grid.draw(canvas, x, y, debug)

    x = 10
    y += 70

    grid = Grid([[child]])
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(0, 0, 0, 0)
    grid.draw(canvas, x, y, debug)

    x += 30

    grid = Grid([[child]])
    grid.style().set_cell_border(2, 2, 2, 2)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(0, 0, 0, 0)
    grid.draw(canvas, x, y, debug)

    x += 30

    grid = Grid([[child]])
    grid.style().set_cell_border(3, 3, 3, 3)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(0, 0, 0, 0)
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[child]])
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(1, 1, 1, 1)
    grid.draw(canvas, x, y, debug)

    x += 30

    grid = Grid([[child]])
    grid.style().set_cell_border(2, 2, 2, 2)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(1, 1, 1, 1)
    grid.draw(canvas, x, y, debug)

    x += 30

    grid = Grid([[child]])
    grid.style().set_cell_border(3, 3, 3, 3)
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(1, 1, 1, 1)
    grid.draw(canvas, x, y, debug)

    x = 10
    y += 50

    grid = Grid([[child]])
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_grid_border(1, (255, 0, 0))
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(0, 0, 0, 0)
    grid.draw(canvas, x, y, debug)

    x += 30

    grid = Grid([[child]])
    grid.style().set_cell_border(2, 2, 2, 2)
    grid.style().set_grid_border(1, (255, 0, 0))
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(0, 0, 0, 0)
    grid.draw(canvas, x, y, debug)

    x += 30

    grid = Grid([[child]])
    grid.style().set_cell_border(3, 3, 3, 3)
    grid.style().set_grid_border(1, (255, 0, 0))
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(0, 0, 0, 0)
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[child]])
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_grid_border(1, (255, 0, 0))
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(1, 1, 1, 1)
    grid.draw(canvas, x, y, debug)

    x += 30

    grid = Grid([[child]])
    grid.style().set_cell_border(2, 2, 2, 2)
    grid.style().set_grid_border(1, (255, 0, 0))
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(1, 1, 1, 1)
    grid.draw(canvas, x, y, debug)

    x += 30

    grid = Grid([[child]])
    grid.style().set_cell_border(3, 3, 3, 3)
    grid.style().set_grid_border(1, (255, 0, 0))
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(1, 1, 1, 1)
    grid.draw(canvas, x, y, debug)

    x = 10
    y += 50

    grid = Grid([[child]])
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_grid_border(2, (255, 0, 0))
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(0, 0, 0, 0)
    grid.draw(canvas, x, y, debug)

    x += 30

    grid = Grid([[child]])
    grid.style().set_cell_border(2, 2, 2, 2)
    grid.style().set_grid_border(2, (255, 0, 0))
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(0, 0, 0, 0)
    grid.draw(canvas, x, y, debug)

    x += 30

    grid = Grid([[child]])
    grid.style().set_cell_border(3, 3, 3, 3)
    grid.style().set_grid_border(2, (255, 0, 0))
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(0, 0, 0, 0)
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[child]])
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_grid_border(2, (255, 0, 0))
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(1, 1, 1, 1)
    grid.draw(canvas, x, y, debug)

    x += 30

    grid = Grid([[child]])
    grid.style().set_cell_border(2, 2, 2, 2)
    grid.style().set_grid_border(2, (255, 0, 0))
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(1, 1, 1, 1)
    grid.draw(canvas, x, y, debug)

    x += 30

    grid = Grid([[child]])
    grid.style().set_cell_border(3, 3, 3, 3)
    grid.style().set_grid_border(2, (255, 0, 0))
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(1, 1, 1, 1)
    grid.draw(canvas, x, y, debug)

    x = 10
    y += 50

    grid = Grid([[child]])
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_grid_border(3, (255, 0, 0))
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(0, 0, 0, 0)
    grid.draw(canvas, x, y, debug)

    x += 30

    grid = Grid([[child]])
    grid.style().set_cell_border(2, 2, 2, 2)
    grid.style().set_grid_border(3, (255, 0, 0))
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(0, 0, 0, 0)
    grid.draw(canvas, x, y, debug)

    x += 30

    grid = Grid([[child]])
    grid.style().set_cell_border(3, 3, 3, 3)
    grid.style().set_grid_border(3, (255, 0, 0))
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(0, 0, 0, 0)
    grid.draw(canvas, x, y, debug)

    x += 50

    grid = Grid([[child]])
    grid.style().set_cell_border(1, 1, 1, 1)
    grid.style().set_grid_border(3, (255, 0, 0))
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(1, 1, 1, 1)
    grid.draw(canvas, x, y, debug)

    x += 30

    grid = Grid([[child]])
    grid.style().set_cell_border(2, 2, 2, 2)
    grid.style().set_grid_border(3, (255, 0, 0))
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(1, 1, 1, 1)
    grid.draw(canvas, x, y, debug)

    x += 30

    grid = Grid([[child]])
    grid.style().set_cell_border(3, 3, 3, 3)
    grid.style().set_grid_border(3, (255, 0, 0))
    grid.style().set_outer_margin(0, 0, 0, 0)
    grid.style().set_margin(1, 1, 1, 1)
    grid.draw(canvas, x, y, debug)

    return canvas


def test_borders():
    name = "borders"
    canvas = draw_borders()
    canvas.save(f"./actual/test_{name}.png", "PNG")
    assert same_image_files(
        f"./expected/test_{name}.png", f"./actual/test_{name}.png", name
    )

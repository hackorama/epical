import os
import sys

from PIL import Image, ImageDraw

if os.path.exists("../lib"):
    sys.path.append("../lib")

from test_utils import same_image
from grid import Grid


def using_image(image_path):
    test_img = Image.new("RGBA", (50, 50))
    draw = ImageDraw.Draw(test_img)
    draw.rectangle((0, 0, 50, 50), fill=(0, 0, 128))

    child_grid_1 = Grid(data=[["1", 2], [3, 4]])
    child_grid_2 = Grid(data=[["1", 2], [3, 4]])
    child_grid_2.style().set_elastic_fit(True)
    child_grid_3 = Grid(data=[["1", 2], [3, 4]])
    child_grid_3.style().set_edge_fit(True).set_elastic_fit(True)
    child_grid_4 = Grid(data=[["1", 2], [3, 4]], width=20, height=20)
    child_grid_4.style().set_fixed_fit(True)
    grid = Grid(
        data=[
            [child_grid_1, 2, test_img],
            ["a", "foobar", "c\nd\ne"],
            ["", child_grid_2, child_grid_3],
            [1.0, 2.0, child_grid_4],
        ],
    )
    image = grid.image(debug=True)
    image.save(image_path, "PNG")
    return image


def using_draw(image, image_path):
    test_img = Image.new("RGBA", (50, 50))
    draw = ImageDraw.Draw(test_img)
    draw.rectangle((0, 0, 50, 50), fill=(0, 0, 128))

    child_grid_1 = Grid(data=[["1", 2], [3, 4]])
    child_grid_2 = Grid(data=[["1", 2], [3, 4]])
    child_grid_2.style().set_elastic_fit(True)
    child_grid_3 = Grid(data=[["1", 2], [3, 4]])
    child_grid_3.style().set_elastic_fit(True).set_edge_fit(True)
    child_grid_4 = Grid(data=[["1", 2], [3, 4]], width=20, height=20)
    child_grid_4.style().set_fixed_fit(True)
    grid = Grid(
        data=[
            [child_grid_1, 2, test_img],
            ["a", "foobar", "c\nd\ne"],
            ["", child_grid_2, child_grid_3],
            [1.0, 2.0, child_grid_4],
        ],
    )
    grid.draw(image, debug=True)
    image.save(image_path, "PNG")
    return image


def test_render():
    image_render = using_image("./actual/test_image.png")
    canvas = Image.new(
        "RGBA", (image_render.width, image_render.height), (255, 255, 255)
    )
    canvas_render = using_draw(canvas, "./actual/test_draw.png")
    assert same_image(image_render, canvas_render, "render")

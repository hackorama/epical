import os
import sys

from PIL import Image, ImageDraw, ImageChops

if os.path.exists("../lib"):
    sys.path.append("../lib")

from grid import Grid
from style import GridStyle, Margin, Align


def create_test_image():
    # load test image from file
    # test_img = Image.open("test_image.png")
    # or generate test image on the fly
    image = Image.new("RGBA", (50, 50))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 50, 50), fill=(0, 0, 255))
    draw.text((5, 5), "TEST")
    draw.text((5, 20), "IMAGE")
    return image


def create_image(w=8, h=8, color=(0, 0, 0)):
    image = Image.new("RGBA", (w, h))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, w, h), fill=color)
    return image


def same_image_files(path_one, path_two, tag=""):
    one = Image.open(path_one)
    two = Image.open(path_two)
    return same_image(one, two, tag)


def same_image(one, two, tag=""):
    w1, h1 = one.size
    w2, h2 = two.size
    if w1 != w2 or h1 != h2:
        print(f"Test failed, size do not match {w1} != {w2} or {h1} != {h2}")
        return False
    w = w1
    h = h1
    one_cropped = one.crop((0, 20, w, h))
    two_cropped = two.crop((0, 20, w, h))
    diff = ImageChops.difference(one_cropped.convert("RGB"), two_cropped.convert("RGB"))
    if diff.getbbox():
        name = f"test_failure_{tag}.png"
        diff.save(name, "PNG")
        print(f"Test failed check rendering diff: open {name}")
    return not diff.getbbox()


def text_align(canvas, x, y, debug=False):
    style = GridStyle(margin=Margin(0, 0, 0, 0))
    style.set_font_size(16)
    top_style = GridStyle(margin=Margin(0, 0, 10, 0), align=Align(top=True))
    top_style.set_font_size(16)
    bottom_style = GridStyle(
        margin=Margin(0, 0, 0, 10),
        align=Align(bottom=True),
    )
    bottom_style.set_font_size(16)
    data = [
        ["ace", "bdf", "gjq", "abg", "Abg"],
        ["ace", "bdf", "gjq", "abg", "Abg"],
        ["ace", "bdf", "gjq", "abg", "Abg"],
    ]
    grid = Grid(data, width=250, height=100)
    grid.set_style(style)
    grid.set_row_cell_style(top_style, 0)
    grid.set_row_cell_style(bottom_style, 2)
    grid.draw(canvas, x, y, debug=debug)

import os
import sys
import textwrap

if os.path.exists("./lib"):
    sys.path.append("./lib")

from grid import Grid

# simple example

grid = Grid([["hello"], ["world"]])

image = grid.image()
image.save("hello.png", "PNG")

# detailed styling example

grid = Grid([["a", "quick", "brown"], ["fox", "jumps", "over"], ["the", "lazy", "dog"]])
grid.style().set_grid_border(5, (200, 200, 200))
grid.style().set_cell_border(1, 1, 1, 1)
grid.style().set_bg_color((218, 247, 166))
grid.style().set_font_size(24).set_font_color((63, 0, 225))
grid.style().set_margin(10, 10, 5, 5).set_align(left=True)
grid.style(0, 2).set_font_color((165, 42, 42)).set_bg_color((255, 255, 255))

image = grid.image()
image.save("style.png", "PNG")

# complex layout with container grids

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

complex_image = main_grid.image()
complex_image.save("complex.png", "PNG")

# Another layout with wrapping and images


text_passage = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore 
et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea 
commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est 
laborum"""

wrapped_text = "\n".join(textwrap.wrap(text_passage, width=37))
text_grid = Grid([[wrapped_text.lower(), wrapped_text.upper()]])
text_grid.style().set_margin(10)
text_grid.style(0, 0).set_align(left=True)
text_grid.style(0, 1).set_align(right=True)
grid = Grid(
    [
        ["Flexible Layouts"],
        ["Grid layout with images and wrapped and aligned text"],
        [complex_image],
        [text_grid],
        ["2023"],
    ]
)
grid.style(0, 0).set_font_size(28)
grid.style(1, 0).set_font_size(12).set_font_color((100, 100, 100))
grid.style(0, 0).set_outer_margin(top=20)
grid.style(1, 0).set_outer_margin(bottom=20)
grid.style(0, 0).set_cell_border(bottom=1, bottom_color=(255, 0, 0))
grid.style(4, 0).set_outer_margin(0, 0, 0, 0)
grid.style(4, 0).set_font_size(8).set_font_color((100, 100, 100))
grid.style(4, 0).set_cell_border(1, 1, 1, 1, (0, 0, 0), (0, 0, 0), (0, 0, 0))
image = grid.image()
image.save("layout.png", "PNG")


# customize rendering by overriding


class MyGrid(Grid):
    def _draw_cell(
        self,
        row: int = 0,
        col: int = 0,
        x1: int = 1,
        y1: int = 1,
        x2: int = 1,
        y2: int = 1,
        debug: bool = False,  # pylint: disable=unused-argument
    ) -> None:
        if int(self._data[row][col]) > 100:
            draw = self._get_draw()
            draw.ellipse(
                (x1 + 4, y1 + 4, x2 - 4, y2 - 4),
                fill=(255, 240, 240),
                outline=(255, 0, 0),
            )
        super()._draw_cell(row, col, x1, y1, x2, y2, debug)


grid = MyGrid([[13, 128, 49], [256, 42, 100]])
grid.style().set_margin(5, 5, 5, 5).set_font_size(16)
grid.style().set_grid_border(1, (200, 200, 200))
image = grid.image()
image.save("custom.png", "PNG")

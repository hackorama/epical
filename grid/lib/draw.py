import math
from typing import Tuple

from PIL.ImageDraw import ImageDraw


def draw_rectangle(  # pylint: disable=too-many-arguments, too-many-locals, too-many-branches, too-many-statements
    draw: ImageDraw,
    xy: Tuple[int, int, int, int],
    left_width: int = 0,
    right_width: int = 0,
    top_width: int = 0,
    bottom_width: int = 0,
    left_color: Tuple[int, int, int] = (0, 0, 0),
    right_color: Tuple[int, int, int] = (0, 0, 0),
    top_color: Tuple[int, int, int] = (0, 0, 0),
    bottom_color: Tuple[int, int, int] = (0, 0, 0),
    row_priority: bool = True,
    collapsed: bool = False,
) -> None:
    """

    Teh ImageDraw.rectangle API does not allow width and color selection for sides
    This helper draws a rectangle with separate width and color for each side.

    :param draw: An ImageDraw object that will be used to draw this rectangle.
    :param xy: Two points to define the bounding box for the rectangle.
    :param left_width: The left line width, in pixels.
    :param right_width: The right line width, in pixels.
    :param top_width: The top line width, in pixels.
    :param bottom_width: The bottom line width, in pixels.
    :param left_color: The left line color.
    :param right_color:  The right line color.
    :param top_color: The top line color.
    :param bottom_color: The bottom line color.
    :param row_priority: If true draw horizontal lines on top of overlapping vertical lines,
           otherwise vertical lines will be on top.
    :param collapsed: Draw only sides with single pixel for collapsed border correction
    :return: None

    PIL Rectangle is drawn inside the given coordinates x,y while PIL Line draws on the given coordinates x,y
    To match PIL Line based rectangle to PIL Rectangle, shift line coordinates x,y by line width offset
    to fit lines inside

    +---------                 +------       +---------
    |               +----+     |             +    |
    |    +----  ==  |    |  +  +------   ==  +----+----
    |    |          |    |                   |    |
    |    |          |    |                   |    |

    Ref: https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#PIL.ImageDraw.ImageDraw.polygon
    '... The bounding box is inclusive of both endpoints ...'
    """
    lo = left_width / 2
    lo = math.floor(lo)
    ro = right_width / 2
    ro = math.floor(ro)
    to = top_width / 2
    to = math.floor(to)
    bo = bottom_width / 2
    bo = math.floor(bo)
    if left_width % 2 == 0:
        lo -= 1
    if top_width % 2 == 0:
        to -= 1

    if not left_width and not right_width and not top_width and not bottom_width:
        return
    if collapsed:
        # Draw only the sides with single width
        if row_priority:
            nxy = (xy[0] + lo, xy[1], xy[0] + lo, xy[3])
            if left_width == 1:
                draw.line(nxy, width=left_width, fill=left_color)  # left

            nxy = (xy[2] - ro, xy[1], xy[2] - ro, xy[3])
            if right_width == 1:
                draw.line(nxy, width=right_width, fill=right_color)  # right

            nxy = (xy[0], xy[1] + to, xy[2], xy[1] + to)
            if top_width == 1:
                draw.line(nxy, width=top_width, fill=top_color)  # top

            nxy = (xy[0], xy[3] - bo, xy[2], xy[3] - bo)
            if bottom_width == 1:
                draw.line(nxy, width=bottom_width, fill=bottom_color)  # bottom
        else:
            nxy = (xy[0], xy[1] + to, xy[2], xy[1] + to)
            if top_width == 1:
                draw.line(nxy, width=top_width, fill=top_color)  # top

            nxy = (xy[0], xy[3] - bo, xy[2], xy[3] - bo)
            if bottom_width == 1:
                draw.line(nxy, width=bottom_width, fill=bottom_color)  # bottom

            nxy = (xy[0] + lo, xy[1], xy[0] + lo, xy[3])
            if left_width == 1:
                draw.line(nxy, width=left_width, fill=left_color)  # left

            nxy = (xy[2] - ro, xy[1], xy[2] - ro, xy[3])
            if right_width == 1:
                draw.line(nxy, width=right_width, fill=right_color)  # right
    else:
        if row_priority:
            nxy = (xy[0] + lo, xy[1], xy[0] + lo, xy[3])
            if left_width:
                draw.line(nxy, width=left_width, fill=left_color)  # left

            nxy = (xy[2] - ro, xy[1], xy[2] - ro, xy[3])
            if right_width:
                draw.line(nxy, width=right_width, fill=right_color)  # right

            nxy = (xy[0], xy[1] + to, xy[2], xy[1] + to)
            if top_width:
                draw.line(nxy, width=top_width, fill=top_color)  # top

            nxy = (xy[0], xy[3] - bo, xy[2], xy[3] - bo)
            if bottom_width:
                draw.line(nxy, width=bottom_width, fill=bottom_color)  # bottom
        else:
            nxy = (xy[0], xy[1] + to, xy[2], xy[1] + to)
            if top_width:
                draw.line(nxy, width=top_width, fill=top_color)  # top

            nxy = (xy[0], xy[3] - bo, xy[2], xy[3] - bo)
            if bottom_width:
                draw.line(nxy, width=bottom_width, fill=bottom_color)  # bottom

            nxy = (xy[0] + lo, xy[1], xy[0] + lo, xy[3])
            if left_width:
                draw.line(nxy, width=left_width, fill=left_color)  # left

            nxy = (xy[2] - ro, xy[1], xy[2] - ro, xy[3])
            if right_width:
                draw.line(nxy, width=right_width, fill=right_color)  # right

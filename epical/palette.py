from typing import Tuple


class Palette:  # pylint: disable=too-few-public-methods
    BLACK: Tuple[int, int, int] = (0, 0, 0)
    WHITE: Tuple[int, int, int] = (255, 255, 255)
    RED: Tuple[int, int, int] = (255, 0, 0)
    GRAY: Tuple[int, int, int] = (136, 136, 136)
    SILVER: Tuple[int, int, int] = (204, 204, 204)
    FG: Tuple[int, int, int] = BLACK
    BG: Tuple[int, int, int] = WHITE
    HL: Tuple[int, int, int] = RED
    LL: Tuple[int, int, int] = BLACK

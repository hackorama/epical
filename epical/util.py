import logging
import os
import sys
from typing import Tuple

from PIL import ImageDraw, ImageFont
from PIL.features import features

log_format = "%(levelname)-8s %(asctime)s - %(message)s"
logging.basicConfig(
    stream=sys.stdout,
    filemode="w",
    format=log_format,
    level=logging.INFO,
)
log = logging.getLogger(__name__)


def abs_relative_path(filename: str) -> str:
    # Already absolute path
    if os.path.exists(filename):
        return filename
    # Else if relative to user home path
    if os.path.exists(os.path.expanduser(filename)):
        return os.path.expanduser(filename)
    # Else relative to source code file path
    this_file = os.path.abspath(__file__)
    this_dir = os.path.dirname(this_file)
    return os.path.join(this_dir, filename)


def draw_overlay_text(  # pylint: disable=too-many-arguments
    draw: ImageDraw.ImageDraw,
    x: int,
    y: int,
    text: str,
    font: ImageFont.FreeTypeFont,
    fg_color: Tuple[int, int, int],
    bg_color: Tuple[int, int, int],
) -> None:
    """
    Draw text with outline so that it stands out on top of background images
    """
    draw.text((x, y), text=text, fill=bg_color, stroke_width=1, font=font)
    draw.text((x, y), text=text, fill=fg_color, font=font)


def report_complex_font_support() -> None:
    if not features.get("raqm"):
        log.warning(
            "Please install 'libraqm' for complex text layout following docs/pillow.md"
        )

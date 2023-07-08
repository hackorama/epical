import os
import sys

import config
from system import System
from util import log

if os.path.exists(config.GRID_LIB_DIR):
    sys.path.append(config.GRID_LIB_DIR)
else:
    log.error(f"Missing grid lib folder {config.GRID_LIB_DIR}")
    log.error("Please install grid lib and retry")
    sys.exit(1)
if os.path.exists(config.EPD_LIB_DIR):
    sys.path.append(config.EPD_LIB_DIR)
else:
    log.warning(f"Missing EPD lib folder {config.EPD_LIB_DIR}")
    log.warning("Will try to run using virtual display")

from data.cal_data import CalData  # pylint: disable=wrong-import-position
from display import (  # pylint: disable=wrong-import-position
    Display,
    EPDisplay,
    VirtualDisplay,
)
from layout import Layout  # pylint: disable=wrong-import-position


def run(name: str = config.PROJECT_NAME.lower()) -> None:
    data = CalData()
    layout = Layout(data, config.SCREEN_W, config.SCREEN_H, config.SCREEN_BORDER)
    image = layout.display()
    display: Display = EPDisplay(image)
    if not display.init():
        display = VirtualDisplay(image, name)
    display.display()
    System.upload()


if __name__ == "__main__":
    log.info(f"{config.PROJECT_NAME} {config.PROJECT_VERSION}")
    run()

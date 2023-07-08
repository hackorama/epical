from datetime import datetime
from typing import Any, Optional, Tuple

import config
from PIL import Image
from system import System
from util import log


class Display:
    def __init__(self, image: Image.Image):
        self._image: Image.Image = image
        self.tolerance: float = self.get_color_distance((255, 0, 0), (128, 0, 0))

    @staticmethod
    def get_color_distance(
        rgb_color_a: Tuple[int, int, int], rgb_color_b: Tuple[int, int, int]
    ) -> float:
        red_mean = 0.5 * (rgb_color_a[0] + rgb_color_b[0])
        red_delta = ((2 + red_mean) * (rgb_color_a[0] - rgb_color_b[0])) ** 2
        green_delta = (4 * (rgb_color_a[1] - rgb_color_b[1])) ** 2
        blue_delta = ((3 - red_mean) * (rgb_color_a[2] - rgb_color_b[2])) ** 2
        return (red_delta + green_delta + blue_delta) ** 0.5

    def not_same_color(
        self, rgb_color_a: Tuple[int, int, int], rgb_color_b: Tuple[int, int, int]
    ) -> bool:
        return self.get_color_distance(rgb_color_a, rgb_color_b) > self.tolerance

    def mono(self, color: Tuple[int, int, int]) -> Image.Image:
        mono_image = self._image.copy()
        pixels = mono_image.load()
        for x in range(mono_image.width):
            for y in range(mono_image.height):
                if self.not_same_color(pixels[x, y], color):
                    pixels[x, y] = (255, 255, 255, 255)
        mono_image = mono_image.convert(mode="1", dither=True)
        if mono_image.width < mono_image.height:
            return mono_image.rotate(90, expand=True)
        return mono_image

    def mono_images(self) -> Tuple[Image.Image, Image.Image]:
        mono_black_image = self._image.copy()
        mono_red_image = self._image.copy()
        black_pixels = mono_black_image.load()
        red_pixels = mono_red_image.load()
        for x in range(mono_black_image.width):
            for y in range(mono_black_image.height):
                # Single color check faster than general color distance
                close_to_max_red = red_pixels[x, y][0] > 200
                only_red = (
                    red_pixels[x, y][0] > red_pixels[x, y][1] + red_pixels[x, y][2]
                )
                red_pixel = close_to_max_red and only_red
                if red_pixel:
                    black_pixels[x, y] = (
                        255,
                        255,
                        255,
                        255,
                    )  # remove red from black mono
                else:
                    red_pixels[x, y] = (
                        255,
                        255,
                        255,
                        255,
                    )  # remove non-red from red mono
        mono_black_image = mono_black_image.convert(mode="1", dither=True)
        mono_red_image = mono_red_image.convert(mode="1", dither=True)
        if mono_red_image.width < mono_red_image.height:
            return mono_black_image.rotate(90, expand=True), mono_red_image.rotate(
                90, expand=True
            )
        return mono_black_image, mono_red_image

    def mono_black(self) -> Image.Image:
        return self.mono((0, 0, 0))

    def mono_red(self) -> Image.Image:
        return self.mono((255, 0, 0))

    def init(self) -> bool:
        return True

    def display(self) -> None:
        pass


class EPDisplay(Display):
    def __init__(self, image: Image.Image):
        super().__init__(image)
        self.epd: Optional[Any] = None

    def init(self) -> bool:
        if self.epd:
            return True
        log.info("Initializing screen ...")
        try:
            import epd12in48b_V2
        except Exception as _error:
            log.warning(f"EPD lib import failed: {_error}")
            log.warning(
                f"  Please install EPD lib in {config.EPD_LIB_DIR} following epd/README.md"
            )
            log.warning("  Will run using virtual display")
            return False
        try:
            self.epd = epd12in48b_V2.EPD()
            if self.epd:
                self.epd.Init()
            return True
        except Exception as _error:
            log.warning(f"Failed EPD init: {_error}")
            log.warning("Will try to run using virtual display")
        return False

    def clear_needed(self) -> bool:
        if config.CLEAR_SCREEN_AFTER_REFRESH_COUNT == 0:
            return False
        if not config.CLEAR_SCREEN_AFTER_REFRESH_COUNT == 1:
            return True
        # When uprecords is available use one refresh per reboot
        boots = System.device_boots()
        if boots:
            return boots % config.CLEAR_SCREEN_AFTER_REFRESH_COUNT == 0
        # Else assume one boot per day and use day of month
        return (
            int(datetime.now().strftime("%d")) % config.CLEAR_SCREEN_AFTER_REFRESH_COUNT
            == 0
        )

    def display(self) -> None:
        self._image.save(f"{config.PROJECT_NAME.lower()}.png", "PNG")
        if self.init() and self.epd:
            log.info("Preparing mono images ...")
            if config.IMAGE_GEN_PREFER_SPEED_OVER_ACCURACY:
                black, red = self.mono_images()
            else:
                black = self.mono_black()
                red = self.mono_red()
            if self.clear_needed():
                log.info("Clearing screen ...")
                self.epd.clear()
            log.info("Updating screen ...")
            self.epd.display(black, red)
            log.info("Powering down screen ...")
            self.epd.EPD_Sleep()
            log.info("Finished screen")


class VirtualDisplay(Display):
    def __init__(self, image: Image.Image, name: str):
        super().__init__(image)
        self._name: str = name
        log.info("Using virtual display ...")

    def display(self) -> None:
        log.info("Preparing mono images ...")
        self._image.save(f"{self._name}.png", "PNG")
        if config.IMAGE_GEN_PREFER_SPEED_OVER_ACCURACY:
            black, red = self.mono_images()
        else:
            black = self.mono_black()
            red = self.mono_red()
        black.save(f"{self._name}_black.png", "PNG")
        red.save(f"{self._name}_red.png", "PNG")
        log.info(f"open {self._name}.png")
        log.info(f"open {self._name}_black.png")
        log.info(f"open {self._name}_red.png")

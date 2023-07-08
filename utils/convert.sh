#!/usr/bin/env bash
#
# eInk ready formatting of images
# https://learn.adafruit.com/preparing-graphics-for-e-ink-displays/command-line
#

if [ -z "$1" ]
  then
    echo "Convert given image to eink ready black, white, red tri-color image: photo.bmp"
    echo
    echo "Usage  : $0 <path to image>"
    echo "Example: $0  test.jpg"
    exit
fi

echo "Converting $1 -> photo.bmp"
test -f /tmp/eink.png || wget -q -O /tmp/eink.png https://cdn-learn.adafruit.com/assets/assets/000/079/736/large1024/eink___epaper_eink-3color.png
convert -resize 700x "$1" /tmp/photo.jpeg
convert /tmp/photo.jpeg -dither FloydSteinberg -define dither:diffusion-amount=85% -remap /tmp/eink.png -type truecolor BMP3:photo.bmp

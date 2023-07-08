﻿#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import os

libdir = "lib"
if os.path.exists(libdir):
    sys.path.append(libdir)

import epd12in48b_V2
import time

from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageColor

from PIL import Image


print("12.48inch e-paper B Demo...")
epd = epd12in48b_V2.EPD()
# Initialize library.
epd.Init()

# Clear epdlay.
print("clearing...")
epd.clear()

# Create blank image for drawing.
Blackimage = Image.new("1", (epd12in48b_V2.EPD_WIDTH, epd12in48b_V2.EPD_HEIGHT), 255)
Redimage = Image.new("1", (epd12in48b_V2.EPD_WIDTH, epd12in48b_V2.EPD_HEIGHT), 255)
Blackdraw = ImageDraw.Draw(Blackimage)
Reddraw = ImageDraw.Draw(Redimage)


print("drawing ...")
Blackdraw.rectangle(
    [(40, 40), (440, 440)],
    fill="BLUE",
)
Blackdraw.rectangle([(43, 43), (437, 437)], fill="WHITE")
Blackdraw.line([(40, 40), (440, 440)], fill="BLUE", width=3)
Blackdraw.line([(440, 40), (40, 440)], fill="BLUE", width=3)
Reddraw.arc([50, 50, 430, 430], 0, 360, fill="BLUE")

Blackimage = Blackimage.rotate(180)
Redimage = Redimage.rotate(180)
epd.display(Blackimage, Redimage)
time.sleep(2)

print("displaying ...")
Blackimage2 = Image.new("1", (epd12in48b_V2.EPD_WIDTH, epd12in48b_V2.EPD_HEIGHT), 255)
Redimage2 = Image.new("1", (epd12in48b_V2.EPD_WIDTH, epd12in48b_V2.EPD_HEIGHT), 255)
epd.display(Blackimage2, Redimage2)
time.sleep(2)

# Do not use for a long time, please save the white screen to save
print("clearing and go to sleep ...")
epd.clear()
epd.EPD_Sleep()

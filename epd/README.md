# Setup Waveshare Display Driver

Follow the Waveshare docs to set up Pi Zero 

- [Set up Pi Zero for Waveshare 12.48inch ePaper](https://www.waveshare.com/wiki/12.48inch_e-Paper_Module_(B)) using [setup.sh](./setup.sh)
- [Install Waveshare display driver files](https://github.com/waveshare/12.48inch-e-paper/tree/master/RaspberryPi/python/lib) in to `./epd/lib` using [download.sh](./download.sh)
 
## Pi Zero Setup

1. [Set up Pi Zero](../docs/zero.md)
2. Setup Display drivers and Python libs using [setup.sh](./setup.sh)

- Enabled SPI using raspi-config
- Installed BCM2835, wiringPi
- Pip installed RPi.GPIO, spidev

```shell
hackorama@pizero:~ $ uname -a
Linux pizero 5.15.84+ #1613 Thu Jan 5 11:58:09 GMT 2023 armv6l GNU/Linux

hackorama@pizero:~ $ sudo lsmod | grep spi
spidev                 20480  0
spi_bcm2835            20480  0

hackorama@pizero:~ $ sudo gpio -v
gpio version: 2.70
Copyright (c) 2012-2018 Gordon Henderson
This is free software with ABSOLUTELY NO WARRANTY.
For details type: gpio -warranty

Raspberry Pi Details:
  Type: Pi Zero-W, Revision: 01, Memory: 512MB, Maker: Sony
  * Device tree is enabled.
  *--> Raspberry Pi Zero W Rev 1.1
  * This Raspberry Pi supports user-level GPIO access.

hackorama@pizero:~ $ pip list | grep RPi
RPi.GPIO            0.7.0

hackorama@pizero:~ $ do pip list | grep spidev
spidev              3.5 

hackorama@pizero:~ $ pip list | grep Pillow
Pillow                9.5.0
```

## Install Waveshare display drivers

```shell
$ ./download.sh
Downloading EPD libs from https://raw.githubusercontent.com/waveshareteam/12.48inch-e-paper/master/RaspberryPi/python/lib into ./lib.
DEV_Config_32.so        DEV_Config_64.so        __init__.py             epd12in48b_V2.py        epdconfig.py

```
Verify EPD lib install on the device with ePaper display connected

```shell
(venv) hackorama@pizero:~/epical/epd $ ls lib
DEV_Config_32.so        DEV_Config_64.so        __init__.py             epd12in48b_V2.py        epdconfig.py
```

```shell
(venv) hackorama@pizero:~/epical/epd $ sudo python test.py
12.48inch e-paper B Demo...
EPD init...
set wiringPi lib success !!!
clearing...
1474.859336639
1437.6391003
use time: 37.220236
drawing ...
use time: 100.427525
displaying ...
use time: 100.842336
clearing and go to sleep ...
1810.27681208
1773.286159441
use time: 36.990653
module_exit
```

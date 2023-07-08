# Better Power using UPS

[Pi Juice Zero](https://uk.pi-supply.com/products/pijuice-zero) can be used as an additional
power option that can auto wake up and refresh the screen every day without using
the manual refresh button option or always on cable connected options described in [power management](power.md)

> This is a planned feature not validated yet

| Item                                                                          |  UK £ |
|-------------------------------------------------------------------------------|------:|
| [PiJuice Zero](https://uk.pi-supply.com/products/pijuice-zero)                | 30.00 |
| [5000 mAh Battery](https://uk.pi-supply.com/products/pijuice-5000mah-battery) | 21.00 |

## Pros

- Low power deep-sleep state with wake on interrupt/calendar event
- Raspberry Pi pHAT layout - designed to exactly fit
- Low profile design, to fit inside the smallest of projects
- Connect with single cell LiPo with an NTC temperature sensor
- Uses 2 GPIO pins, Communication over I2C

## Cons

- Fitting the UPS board inside the display frame and case
  - Attaching on top of display header socket using stacking headers
    - May need cutting out space on the acrylic back cover of the display
    - Could look at right angle header pins to change connection orientation
  - Or connect by soldering to exposed header pin ends on pi zero 
    - Not a clean solution 
- Confirm unused GPIO pins between display and ups board

## GPIO pin usage

[Display GPIO pin usage](https://www.waveshare.com/wiki/12.48inch_e-Paper_Module_(B)#Hardware_Connection)

```commandline
$ grep "_PIN " epd/lib/epdconfig.py
EPD_SCK_PIN   =11
EPD_MOSI_PIN  =10
EPD_M1_CS_PIN  =8
EPD_S1_CS_PIN  =7
EPD_M2_CS_PIN  =17
EPD_S2_CS_PIN  =18
EPD_M1S1_DC_PIN  =13
EPD_M2S2_DC_PIN  =22
EPD_M1S1_RST_PIN =6
EPD_M2S2_RST_PIN =23
EPD_M1_BUSY_PIN  =5
EPD_S1_BUSY_PIN  =19
EPD_M2_BUSY_PIN  =27
EPD_S2_BUSY_PIN  =24
```
 
[UPS GPIO pin usage](https://pinout.xyz/pinout/pijuice)

Use only GPIO 2 and GPIO 3 ?

> Uses 2 GPIO pins, Communication over I2C

> PiJuice only uses five of the Pi's GPIO pins (just power and I2C),
> the rest are free and made available via the stacking header
> which allows for other boards to be used alongside PiJuice. 

## Other boards

These boards may not support scheduled wake up

- [JuiceBox Zero](https://juiceboxzero.com) 
- [PiZ-UpTime](https://alchemy-power.com/piz-uptime-2-0/)
- [Zero2Go](https://www.adafruit.com/product/4114)
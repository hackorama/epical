# Power Status LED

A power status LED can be added to check for safe power off after Pi Zero halt.

Based on the [Display GPIO pin usage](https://www.waveshare.com/wiki/12.48inch_e-Paper_Module_(B)#Hardware_Connection) 
the following UART GPIO pin is not used by the display and can be used for power status LED.


```commandline
$ tail /boot/config.txt
enable_uart=1
```

| PIN | GPIO    | TYPE    | LED Connection                                |
|-----|---------|---------|-----------------------------------------------|
| 6   |         | GROUND  | LED - Cathode shorter lead, 330 Ohms Resistor |
| 8   | GPIO 14 | UART TX | LED + Anode longer lead                       |

Alternatively we can also use the power bank status LED for device power status or
use a light pipe or TOSLINK S/PDIF cable glued on to the status led on the Pi Zero.


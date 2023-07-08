# Pi Zero

Use [Raspberry Pi Imager](https://www.raspberrypi.com/software/)

- Format 32 GB SD Card to FAT 32 using the Imager
- Install Raspberry Pi OS LITE(32-Bit) with no desktop
- In 'Advanced Options' enable, user account, SSH, Wi-Fi
      
> Pi Zero W only supports 2.4GHz Wi-Fi SSID. Pi Zero 2 W can connect to both 2.4GHz and 5GHz 

Connect Pi Zero using the second peripherals usb port from the laptop and get the IP address.

```bash
$ ssh hackorama@pizero.local
hackorama@pizero:~ $ hostname -I
192.168.1.249
```

Verify WiFi

```bash
hackorama@pizero:~ $ iwconfig
...
wlan0     IEEE 802.11  ESSID:"hackorama"
...
```

```bash
hackorama@pizero:~ $ ifconfig wlan
...
inet 192.168.1.249  netmask 255.255.255.0  broadcast 192.168.1.255
...
```

Setup passwordless ssh

```bash
$ ssh hackorama@192.168.1.249
$ ssh-keygen -C "zero"
$ ssh-copy-id -i  ~/.ssh/id_zero_rsa.pub hackorama@192.168.1.249


$ cat ~/.ssh/config
...
Host zero
    HostName 192.168.1.249
    User hackorama
    IdentityFile ~/.ssh/id_zero_rsa
```

```bash
hackorama@pizero:~ $ eval "$(ssh-agent -s)"
Agent pid 928
```

```bash
$ ssh zero
hackorama@pizero:~ $
```

## Diag

```bash
hackorama@pizero:~/epical $ raspi-gpio get
BANK0 (GPIO 0 to 27):
GPIO 0: level=1 fsel=0 func=INPUT
GPIO 1: level=1 fsel=0 func=INPUT
GPIO 2: level=1 fsel=0 func=INPUT
GPIO 3: level=1 fsel=0 func=INPUT
GPIO 4: level=1 fsel=0 func=INPUT
GPIO 5: level=1 fsel=0 func=INPUT
GPIO 6: level=0 fsel=0 func=INPUT
GPIO 7: level=1 fsel=1 func=OUTPUT
GPIO 8: level=1 fsel=1 func=OUTPUT
GPIO 9: level=0 fsel=4 alt=0 func=SPI0_MISO
GPIO 10: level=0 fsel=4 alt=0 func=SPI0_MOSI
GPIO 11: level=0 fsel=4 alt=0 func=SPI0_SCLK
GPIO 12: level=0 fsel=0 func=INPUT
GPIO 13: level=0 fsel=0 func=INPUT
GPIO 14: level=0 fsel=0 func=INPUT
GPIO 15: level=1 fsel=0 func=INPUT
GPIO 16: level=0 fsel=0 func=INPUT
GPIO 17: level=0 fsel=0 func=INPUT
GPIO 18: level=0 fsel=0 func=INPUT
GPIO 19: level=0 fsel=0 func=INPUT
GPIO 20: level=0 fsel=0 func=INPUT
GPIO 21: level=0 fsel=0 func=INPUT
GPIO 22: level=0 fsel=0 func=INPUT
GPIO 23: level=0 fsel=0 func=INPUT
GPIO 24: level=0 fsel=0 func=INPUT
GPIO 25: level=0 fsel=0 func=INPUT
GPIO 26: level=0 fsel=0 func=INPUT
GPIO 27: level=0 fsel=0 func=INPUT
BANK1 (GPIO 28 to 45):
GPIO 28: level=1 fsel=0 func=INPUT
GPIO 29: level=1 fsel=0 func=INPUT
GPIO 30: level=0 fsel=7 alt=3 func=CTS0
GPIO 31: level=0 fsel=7 alt=3 func=RTS0
GPIO 32: level=1 fsel=7 alt=3 func=TXD0
GPIO 33: level=1 fsel=7 alt=3 func=RXD0
GPIO 34: level=0 fsel=7 alt=3 func=SD1_CLK
GPIO 35: level=1 fsel=7 alt=3 func=SD1_CMD
GPIO 36: level=1 fsel=7 alt=3 func=SD1_DAT0
GPIO 37: level=1 fsel=7 alt=3 func=SD1_DAT1
GPIO 38: level=1 fsel=7 alt=3 func=SD1_DAT2
GPIO 39: level=1 fsel=7 alt=3 func=SD1_DAT3
GPIO 40: level=0 fsel=1 func=OUTPUT
GPIO 41: level=1 fsel=1 func=OUTPUT
GPIO 42: level=0 fsel=0 func=INPUT
GPIO 43: level=1 fsel=4 alt=0 func=GPCLK2
GPIO 44: level=0 fsel=1 func=OUTPUT
GPIO 45: level=1 fsel=1 func=OUTPUT
BANK2 (GPIO 46 to 53):
GPIO 46: level=1 fsel=0 func=INPUT
GPIO 47: level=0 fsel=1 func=OUTPUT
GPIO 48: level=0 fsel=4 alt=0 func=SD0_CLK
GPIO 49: level=1 fsel=4 alt=0 func=SD0_CMD
GPIO 50: level=1 fsel=4 alt=0 func=SD0_DAT0
GPIO 51: level=1 fsel=4 alt=0 func=SD0_DAT1
GPIO 52: level=1 fsel=4 alt=0 func=SD0_DAT2
GPIO 53: level=1 fsel=4 alt=0 func=SD0_DAT3
```

```bash
hackorama@pizero:~/epical $ sudo vcgencmd measure_temp
temp=34.7'C
hackorama@pizero:~/epical $ sudo vcgencmd measure_volts
volt=1.3500V
hackorama@pizero:~/epical $ sudo vcgencmd get_mem arm
arm=448M
hackorama@pizero:~/epical $ sudo vcgencmd get_mem gpu
gpu=64M
```
```bash
hackorama@pizero:~/epical $ sudo vcgencmd get_config int
aphy_params_current=547
arm_freq=1000
arm_freq_min=700
audio_pwm_mode=514
camera_auto_detect=1
config_hdmi_boost=5
core_freq=400
disable_auto_turbo=1
disable_commandline_tags=2
disable_overscan=1
display_auto_detect=1
display_hdmi_rotate=-1
display_lcd_rotate=-1
dphy_params_current=547
dvfs=3
enable_tvout=1
force_eeprom_read=1
force_pwm_open=1
framebuffer_ignore_alpha=1
framebuffer_swap=1
gpu_freq=300
ignore_lcd=1
init_uart_clock=0x2dc6c00
mask_gpu_interrupt0=3072
mask_gpu_interrupt1=26370
max_framebuffers=2
over_voltage_avs=0x249f0
pause_burst_frames=1
program_serial_random=1
sdram_freq=450
total_mem=512
hdmi_force_cec_address:0=65535
hdmi_force_cec_address:1=65535
hdmi_pixel_freq_limit:0=0x9a7ec80
```
#!/bin/bash

echo "Enable SPI interface ..."
sleep 3

sudo raspi-config

sudo lsmod | grep spi

mkdir wavesahre
cd waveshare || exit

wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.71.tar.gz
tar zxvf bcm2835-1.71.tar.gz
cd bcm2835-1.71/ || exit
sudo ./configure && sudo make && sudo make check && sudo make install

echo "Check bcm2835 ..."
sleep 3

ls /usr/local/lib/libbcm2835.a

wget https://project-downloads.drogon.net/wiringpi-latest.deb
sudo dpkg -i wiringpi-latest.deb

echo "Check GPIO ..."
sleep 3

gpio -v

sudo apt-get install python3-venv
sudo apt-get install libopenjp2-7

echo "Setup python venv with pi zero packages ..."

python3 -m venv venv
source venv/bin/activate
pip3 install RPi.GPIO
pip3 install spidev

echo "Install epical python packages in the venv ..."

cd ../epical || exit
pip3 install -r requirements.txt

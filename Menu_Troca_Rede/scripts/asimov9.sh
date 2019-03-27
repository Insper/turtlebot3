#!/bin/bash
#sudo pkill -f ROBO
sudo killall wpa_supplicant
wpa_supplicant -B -i wlan0 -Dnl80211 -c /etc/wpa_supplicant/wpa_supplicant9.conf
#/home/pi/start_turtle.sh



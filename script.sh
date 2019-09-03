#!/bin/sh
git checkout master
git pull origin master
sudo apt-get update
sudo apt autoclean


hostn=$(uname -n)
mac=$(cat /sys/class/net/wlan0/address)

if [ "$hostn" == "raspberrypi" ]; then

        case $mac in 

        "b8:27:eb:87:39:ee") newhost="robo01";;

        "b8:27:eb:21:3c:9e") newhost="robo02";;

        "b8:27:eb:f1:86:7b") newhost="robo03";;

        "b8:27:eb:fb:1d:78") newhost="robo04";;

        "b8:27:eb:1e:78:1d") newhost="robo05";;

        "b8:27:eb:51:98:80") newhost="robo06";;
        
        "b8:27:eb:b0:59:3e") newhost="robo07";;

        "b8:27:eb:fb:f0:3d") newhost="robo08";;

        "b8:27:eb:02:2c:f4") newhost="robo09";;

        "b8:27:eb:e7:7b:2c") newhost="robo10";;

        "b8:27:eb:29:ff:58") newhost="robo11";;

        "b8:27:eb:b9:80:b5") newhost="robo12";;

        "b8:27:eb:a5:9f:5f") newhost="robo13";;

        "b8:27:eb:1a:03:6c") newhost="robo14";;

        "b8:27:eb:93:d6:9e") newhost="robo15";;

        "b8:27:eb:04:f6:2c") newhost="robo16";;

        "b8:27:eb:e0:af:4b") newhost="robo17";;

        "b8:27:eb:98:6a:20") newhost="robo18";;

        "b8:27:eb:24:71:d6") newhost="robo19";;

        "b8:27:eb:fb:1d:78") newhost="robo20";;
        
        "b8:27:eb:0f:71:4a") newhost="robo21";;
        
        "b8:27:eb:b9:da:ba") newhost="robo22";;
        
        "b8:27:eb:bc:ec:bb") newhost="robo23";;
        
        "b8:27:eb:d6:03:d1") newhost="robo24";;
        
        "b8:27:eb:51:b2:06") newhost="robo25";;


        *) echo 0;;

esac    


echo $newhost
sudo echo -e $newhost >/etc/hosts
sudo echo -e $newhost > /etc/hostname
sudo echo -e $newhost > /proc/sys/kernel/hostname
echo "Atualizando o hostname..." >> ~/update.txt
date >> ~/update.txt

else


echo 0 

fi

        
        

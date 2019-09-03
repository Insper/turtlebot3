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

        "b8:27:eb:fb:f0:3d") newhost="robo08";;

        "b8:27:eb:02:2c:f4") newhost="robo09";;

        "b8:27:eb:e7:7b:2c") newhost="robo10";;

        "fe80::9eb6:6ed3:f0e5:aa41") newhost="robo11";;

        "fe80::a33:6f84:4ace:d8fe") newhost="robo12";;

        "fe80::acff:f295:6c72:cc2b") newhost="robo13";;

        "b8:27:eb:1a:03:6c") newhost="robo14";;

        "b8:27:eb:93:d6:9e") newhost="robo15";;

        "b8:27:eb:04:f6:2c") newhost="robo16";;

        "b8:27:eb:e0:af:4b") newhost="robo17";;

        "b8:27:eb:98:6a:20") newhost="robo18";;

        "b8:27:eb:24:71:d6") newhost="robo19";;

        "b8:27:eb:fb:1d:78") newhost="robo20";;

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

        
        

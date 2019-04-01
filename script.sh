git checkout master
git pull
sudo apt-get update
sudo apt autoclean

sudo echo "ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=BR

network={
	ssid="asimov1"
	psk="a ultima pergunta"
	key_mgmt=WPA-PSK
	priority=6
}



network={
	ssid="asimov2"
	psk="a ultima pergunta"
	key_mgmt=WPA-PSK
	priority=4
}


network={
	ssid="asimov3"
	psk="a ultima pergunta"
	key_mgmt=WPA-PSK
	priority=3
}


network={
	ssid="asimov4"
	psk="a ultima pergunta"
	key_mgmt=WPA-PSK
	priority=3
}


network={
	ssid="asimov5"
	psk="a ultima pergunta"
	key_mgmt=WPA-PSK
	priority=3
}


network={
	ssid="asimov6"
	psk="a ultima pergunta"
	key_mgmt=WPA-PSK
	priority=3
}


network={
	ssid="asimov7"
	psk="a ultima pergunta"
	key_mgmt=WPA-PSK
	priority=3
}


network={
	ssid="asimov8"
	psk="a ultima pergunta"
	key_mgmt=WPA-PSK
	priority=3
}


network={
	ssid="asimov9"
	psk="a ultima pergunta"
	key_mgmt=WPA-PSK
	priority=3
}


network={
	ssid="asimov10"
	psk="a ultima pergunta"
	key_mgmt=WPA-PSK
	priority=3
}


network={
	ssid="asimov11"
	psk="a ultima pergunta"
	key_mgmt=WPA-PSK
	priority=3
}

network={
	ssid="asimov12"
	psk="a ultima pergunta"
	key_mgmt=WPA-PSK
	priority=3
}

network={
	ssid"Insper"
	priority=1
	proto=RSN
	key_mgmt=WPA-EAP
	pairwise=CCMP
	auth_alg=OPEN
	eap=PEAP
	identity="Robos_Engenharia"
	password=hash:d4c801dc01248340d875823f190c8a08
	phase1="peaplabel=0"
	phase2="MSCHAPV2"
}" > /etc/wpa_supplicant/wpa_supplicant.conf


sudo rm -rf wpa_supplicant_edit.conf 

sudo echo "ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=BR


network={
        ssid="asimov9"
        psk="a ultima pergunta"
}
" > /etc/wpa_supplicant/wpa_supplicant9.conf


sudo echo "
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=BR

network={
        ssid="Insper_Linux"
        proto=RSN
        key_mgmt=WPA-EAP
        pairwise=CCMP
        auth_alg=OPEN
        eap=PEAP
        identity="Robos_Engenharia"
        password=hash:7ad1bc9c412e7104bf16487fc0ac38b5
        phase1="peaplabel=0"
        phase2="auth=MSCHAPV2"
        priority=8
}

" >  /etc/wpa_supplicant/wpa_supplicant_linux.conf

echo "finish update"


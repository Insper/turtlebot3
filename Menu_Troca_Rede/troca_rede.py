#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
import math
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import subprocess
import RPi.GPIO as GPIO
from luma.core.render import canvas
from time import sleep
import socket
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
from luma.core.interface.serial import i2c


serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)
global gdraw, gdevice



gpio_pin_down = 27
gpio_pin_up = 17
gpio_pin_left = 22
gpio_pin_right = 23


# Botao
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_pin_down, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_pin_up, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_pin_left, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_pin_right, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Definições das variáveis
endereco = "ERROR"
rede = "nao conectada"
RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
padding = 2
shape_width = 20

# Configuração inicial
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
top = padding
emy=top
bottom = height-padding
x = padding
font = ImageFont.load_default()
draw = ImageDraw.Draw(image)
ja = 0
flag=0
names = ['asimov1', 'asimov3', 'asimov5', 'asimov7', 'asimov9', 'asimov11','Shutdown']

#fontes
font_small = ImageFont.truetype('/home/pi/fonts/OpenSans-Regular.ttf', 16)
font = ImageFont.truetype('/home/pi/fonts/OpenSans-ExtraBoldItalic.ttf', 14)
font14 = ImageFont.truetype('/home/pi/fonts/OpenSans-Regular.ttf', 16)




def invert(draw,x,y,text):
    font = ImageFont.load_default()
    draw.rectangle((x, y, x+120, y+10), outline=255, fill=255)
    draw.text((x, y), text, font=font, outline=0,fill="black")

# Box and text rendered in portrait mode
def menu(device, draw, menustr,index):
    global menuindex
    font = ImageFont.load_default()
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    for i in range(len(menustr)):
        if(i == index):
            menuindex = i
            invert(draw, 2, i*10, menustr[i])

        else:
            draw.text((2, i*10), menustr[i], font=font, fill=255)

def conecta():
	global ja
	try: 
		print(strval)
		sucesso="/home/pi/net/{}.sh".format(strval)
                sucesso=subprocess.check_output([sucesso])
		print(sucesso)
	finally: 
		ip_asimov=subprocess.check_output(["/home/pi/net/ipendereco.sh"])
		ip_asimov=ip_asimov.split()
		print(ip_asimov)		
		#rede=ip_asimov[0]
		#endereco=ip_asimov[1]
		ja=0

def desliga():
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        global menu
        menu=-12
        time.sleep(1)
        retorno = subprocess.check_output(["sudo","halt"])

def menu_mostra():
	global names
	draw.rectangle((0,0,width,height), outline=0, fill=0)
	menu(device, draw, names,1)
	menu_operation(strval)

def menu_operation(strval):
 
    if ( strval == "Shutdown"):
	global flag
	if flag==0:
		draw.rectangle((0,0,width,height), outline=0, fill=0)
		draw.rectangle(device.bounding_box, outline="white", fill="black")
       		draw.text((20,20), "SHUTDOWN ", font=font14,fill="white")            	
		draw.text((10, 50), "Press V to confirm ", fill="white")

	elif flag==1:
		uma=5	
		while uma!=0:
			uma-=1
			try:
				draw.rectangle((0,0,width,height), outline=0, fill=0)
                		draw.text((x,2),"     SHUTDOWN    ",font=font14,fill=255)
				draw.text((x,25),"             IN {}...   ".format(uma),font=font14,fill=255)
                		time.sleep(1)
			except:
				desliga()            	
		desliga()

    if ( strval == "asimov1"):
	draw.text((0, 26), "Conectando em Asimov1", fill="white")
    	conecta()			
    if ( strval == "asimov3"):
	draw.text((0, 26), "Conectando em Asimov3", fill="white")
	conecta()
    if ( strval == "asimov5"):
	draw.text((0, 26), "Conectando em Asimov5", fill="white")
	conecta()
    if ( strval == "asimov7"):
	draw.text((0, 26), "Conectando em Asimov7", fill="white")
	conecta()
    if ( strval == "asimov9"):
	draw.text((0, 26), "Conectando em Asimov9", fill="white")
	conecta()
    if ( strval == "asimov11"):
	draw.text((0, 26), "Conectando em Asimov11", fill="white")
	conecta()


def menu_left(channel):  
    global counter		
    strval = names[counter]
    menu_mostra()


def menu_right(channel):
	global strval
	strval = names[6]
	print(strval)
	menu_operation(strval)

def menu_up(channel):  
    global counter
    print(counter)
    if counter >1:
        counter -= 1
        print (counter)
        menu(device, draw, names,counter%7)
    

def menu_down(channel):
	global counter
	print(counter)
	global flag
	global strval
	if strval == names[6]:
		flag =1
		menu_operation(strval)
	elif counter<7:
		counter+= 1
        	print (counter)
      		menu(device,draw,names,counter%7)
        

    		
def limpa_tela():
        # Draw the image buffer.
        disp.image(image)
        disp.display()
        time.sleep(0.5)





counter = 0
insubmenu = 0
strval =names[0]


GPIO.add_event_detect(gpio_pin_up, GPIO.FALLING, callback = menu_up,bouncetime=300)
GPIO.add_event_detect(gpio_pin_down, GPIO.FALLING, callback = menu_down,bouncetime=300)
GPIO.add_event_detect(gpio_pin_left, GPIO.FALLING, callback = menu_left,bouncetime=300)
GPIO.add_event_detect(gpio_pin_right, GPIO.FALLING, callback = menu_right,bouncetime=300)


while True:
	limpa_tela()

	if ja==0:
		ip_asimov=subprocess.check_output(["/home/pi/net/ipendereco.sh"])
		ip_asimov=ip_asimov.split()
		rede=ip_asimov[0]
		endereco=ip_asimov[1]
		ja=1
		draw.rectangle(device.bounding_box, outline="white", fill="black")
       		draw.text((40, 20), rede, fill="white")
       		draw.text((20, 30), endereco, fill="white")
       		draw.text((5, 50), "SHUTDOWN        MENU  ", fill="white")

	
		
	

       


GPIO.cleanup()

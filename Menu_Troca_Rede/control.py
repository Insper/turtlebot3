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



# Load default font.
#font = ImageFont.load_default()
uma=6
font_small = ImageFont.truetype('/home/pi/fonts/OpenSans-Regular.ttf', 16)
font = ImageFont.truetype('/home/pi/fonts/OpenSans-ExtraBoldItalic.ttf', 14)
font14 = ImageFont.truetype('/home/pi/fonts/OpenSans-Regular.ttf', 16)
menu=0
endereco = "ERROR"
rede = "nao conectada"
p1=2
p2=2
p3=2
p4=2
linha1="     oi"
linha2="     oi"
linha3="     oi"
linha4="     oi"
font1=font
font2=font
font3=font
font4=font
global lista_rede
global Asimov
global flu
global fl
Asimov=None
fl=1 
flu=1
# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Initialize library.
disp.begin()

# Get display width and height.
width = disp.width
height = disp.height

# Clear display.
disp.clear()
disp.display()

# Create image buffer.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (width, height))
# First define some constants to allow easy resizing of shapes.
padding = 2
shape_width = 20
top = padding
emy=top
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = padding
# Load default font.
font = ImageFont.load_default()

# Create drawing object.
draw = ImageDraw.Draw(image)
names = ['Insper_linux','asimov1', 'asimov2', 'asimov3', 'asimov4', 'asimov5', 'asimov6', 'asimov7', 'asimov8', 'asimov9', 'asimov10', 'asimov11','asimov12']

def menu_up(channel):
	#teste para parar de andar 
        subprocess.check_output(['rostopic','pub','-1','/cmd_ve','geometry_msgs/Twist','--','[0.0,0.0,0.0]','[0.0,0.0,0.0]'])	        
        if menu==10:
		global flag
                global Asimov
              
                if flag in range(0,12):
                        Asimov=names[flag]
                        flag+=1
		else:
			flag=0
			Asimov=names[flag]
        else:
                return
        return(Asimov)
        

def menu_down(channel):
	global menu
	
        if menu==0:
		draw.rectangle((0,0,width,height), outline=0, fill=0)
                draw.text((x, 0),"        Press         ",font=font14,fill=255)
                draw.text((x,20),"   \/ to confirm     ",font=font14,fill=255)
		draw.text((x, 40),"  <  to return    ",font=font14,fill=255)
		menu=1
	elif menu==1:
		uma=5
		while uma!=0:
			uma-=1
			try:
				draw.rectangle((0,0,width,height), outline=0, fill=0)
                		draw.text((x,2),"     SHUTDOWN    ",font=font14,fill=255)
				draw.text((x,25),"             IN {}...   ".format(uma),font=font14,fill=255)
                		time.sleep(1)
			except:
				desliga_robo()            	
		desliga_robo()
        if menu==10:
                global Asimov
		global flag
	#	print(flag)
	
                if flag in range(1,13):
			Asimov=names[flag-1]
                        flag-=1
		else:
			flag=12
			Asimov=names[flag-1]
        return(Asimov)                        
                                        
        
                
        

def menu_left(channel):
        global menu
        menu=0
        
        return
 
def menu_right(channel):
        global menu
        global flag
        
        if menu ==0:
                flag=0
                menu=10
        elif menu ==10:
                menu=20
                
        elif menu ==20:
                menu=0

        else:
                return
        return



def troca_rede():
        global ip_asimov
        try:
	#	print(Asimov)
                sucesso="/home/pi/net/scripts/{}.sh".format(Asimov)
                sucesso=subprocess.check_output([sucesso])
                flu=1
        except:
                time.sleep(1)
def limpa_tela():
        # Draw the image buffer.
        disp.image(image)
        disp.display()
        time.sleep(0.5)
        return

def desliga_robo():
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        global menu
        menu=-12
        time.sleep(1)
        retorno = subprocess.check_output(["sudo","halt"])
       
        return
        
        
def escreveTela(p1,p2,p3,p4,linha1,linha2,linha3,linha4,font1,font2,font3,font4):
        try:
                draw.text((x+23, p1),linha1,font=font1,fill=255)
                draw.text((x+6, p2),linha2,font=font2,fill=255)
                draw.text((x, p3),linha3,font=font3,fill=255)
                draw.text((x, p4),linha4,font=font4,fill=255)

        except:
                draw.rectangle((0,0,width,height), outline=0, fill=0)

        return




GPIO.add_event_detect(gpio_pin_up, GPIO.FALLING, callback = menu_up,bouncetime=300)
GPIO.add_event_detect(gpio_pin_down, GPIO.FALLING, callback = menu_down,bouncetime=300)
GPIO.add_event_detect(gpio_pin_left, GPIO.FALLING, callback = menu_left,bouncetime=300)
GPIO.add_event_detect(gpio_pin_right, GPIO.FALLING, callback = menu_right,bouncetime=300)



while True:
        global lista_rede
        #global Asimov
        #global flu
        global f
        
        limpa_tela()
        
        if menu == 0:
                if flu ==0:
		#	print("troca de rede")
                        troca_rede()
                        flu=1
                try:
		#	print("primeira tela")
                        f=0
                        ip_asimov=subprocess.check_output(["/home/pi/net/scripts/ipendereco.sh"])
                        ip_asimov=ip_asimov.split()
                        rede=ip_asimov[0]
			Asimov=ip_asimov[0]
                        endereco=ip_asimov[1]
                        p1=top
                        p2=top+18
                        p3=45
                        p4=55
                        linha1=rede
                        linha2=endereco
                        linha3="SHUTDOWN        MENU  "
                        linha4="   \/            >"
                        font1=font14
                        font2=font14
                        font3=font
                        font4=font
                        draw.rectangle((0,0,width,height), outline=0, fill=0)
                        escreveTela(p1,p2,p3,p4,linha1,linha2,linha3,linha4,font1,font2,font3,font4)
                
                except:
                        menu=0
                        
        if menu == 10:
		global Asimov
		global flag
		Asimov=names[flag]
                draw.rectangle((0,0,width,height), outline=0, fill=0)
                draw.text((x, 2),"13 Signs Found,conect in",font=font,fill=255)
                draw.text((x+25, 20),"{}?".format(Asimov),font=font14,fill=255)
                draw.text((x, 55),"/\|\/ change     ok >",font=font,fill=255)

        if menu == 20:                               
                        
                        flu=0
                        if f ==0:
                                try:
				#	print("oi")
                                        p1=2
                                        p2=20
                                        p3=45
                                        p4=55
                                        linha4="                       "
                                        linha1="CONNECTING IN      "   
                                        linha2="   {} =3".format(Asimov)
                                        linha3="                       "
                                        font1=font
                                        font2=font14
                                        font3=font14
                                        font4=font14
                                        draw.rectangle((0,0,width,height), outline=0, fill=0)
                                        escreveTela(p1,p2,p3,p4,linha1,linha2,linha3,linha4,font1,font2,font3,font4)
                                        f=1

                                except:
                                     #   print("bugou")
                                        flu=0
                                	troca_rede(Asimov,rede,endereco)                                                

                        else:
                                menu=0

#!/usr/bin/env python

# Importa as bibliotecas do ROS e do Python
import rospy
from std_msgs.msg import String, Float32

import RPi.GPIO as GPIO
import time as time

# Seta o modo do  GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Seta o GPIO do servo motor
pinMotorBraco = 18
pinMotorGarra = 12

# Seta a frequencia
Frequency = 50

# Seta o DutyCycle da posicao da Braco 
# Braco Sobe
BracoSobe = 11 
# Braco no centro
BracoCentro = 5
# Braco recolhida
BracoRecolhe = 3
# garra fechada
GarraFechada = 5
# garra aberta
GarraAberta = 13


# Para o servo motor
Stop = 0

# Seta o pino do servo motor como saida
GPIO.setup(pinMotorBraco, GPIO.OUT)
GPIO.setup(pinMotorGarra, GPIO.OUT)

# Ajusta a frequencia do PWM
pwmMotorBraco = GPIO.PWM(pinMotorBraco, Frequency)
pwmMotorGarra = GPIO.PWM(pinMotorGarra, Frequency)

# Inicializa o PWM (servo parado)
pwmMotorBraco.start(Stop)
pwmMotorGarra.start(Stop)

# Funcao stop servo motor
def StopMotor():
    pwmMotorBraco.ChangeDutyCycle(Stop)
    pwmMotorGarra.ChangeDutyCycle(Stop)

# Funcao sobe Braco
def SobeBraco():
    pwmMotorBraco.ChangeDutyCycle(BracoSobe)

# Funcao Centro Braco
def DesceBraco():
    pwmMotorBraco.ChangeDutyCycle(BracoCentro)

# Funcao recolhe Braco
def RecolheBraco():
    pwmMotorBraco.ChangeDutyCycle(BracoRecolhe)

# Funcao posicao Braco
def PosBraco(command):
    pwmMotorBraco.ChangeDutyCycle(command)



# Funcao abre Garra
def AbreGarra():
    pwmMotorGarra.ChangeDutyCycle(GarraAberta)

# Funcao fecha Garra
def FechaGarra():
    pwmMotorGarra.ChangeDutyCycle(GarraFechada)

# Funcao posicao Garra
def PosGarra(command):
    pwmMotorGarra.ChangeDutyCycle(command)

# Funcao Callback (le o comando recebido para a posicao da Garra)
def CommandCallback(commandMessage):
    command = commandMessage.data
    if command == 'abre':
        print('abre a garra ')
        AbreGarra()
        time.sleep(0.5)
        StopMotor()
        time.sleep(0.5)

    elif command == 'fecha':
        print('fecha a garra')
        FechaGarra()
        time.sleep(0.5)
        StopMotor()
        time.sleep(0.5)

    elif command == 'stop':
        print('Parando')
        StopMotor()
    else:
        print('Posicao', command)
        PosGarra(command)
        time.sleep(0.5)
        StopMotor()
        time.sleep(0.5)

# Funcao Callback1 (le o comando recebido para possicao da Braco)
def CommandCallback1(commandMessage):
    command = commandMessage.data
    if command == 'sobe':
        print('sobe o Braco')
        SobeBraco()
        time.sleep(0.5)
        StopMotor()
        time.sleep(0.5)

    elif command == 'desce':
        print('Desce o Braco')
        DesceBraco()
        time.sleep(0.5)
        StopMotor()
        time.sleep(0.5)

    elif command == 'recolhe':
        print('Recolhe o Braco')
        RecolheBraco()
        time.sleep(0.5)
        StopMotor()
        time.sleep(0.5)

    elif command == 'stop':
        print('Parando')
        StopMotor()
    else:
        print('Posicao', command)
        PosBraco(command)
        time.sleep(0.5)
        StopMotor()
        time.sleep(0.5)




# Incia o node 
rospy.init_node('driver')

rospy.Subscriber('servo_garra/command', String, CommandCallback)
rospy.Subscriber('servo_garra/position', Float32, CommandCallback)
rospy.Subscriber('servo_braco/command', String, CommandCallback1)
rospy.Subscriber('servo_braco/position', Float32, CommandCallback1)

rospy.spin()
print('Shutting down: stopping motors')
StopMotor()

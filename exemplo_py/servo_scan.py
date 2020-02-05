#! /usr/bin/env python
# -*- coding:utf-8 -*-

# este programa faz a leitura de um objeto a sua frente, se descola até uma distancia de 
# 25 cm, neste ponto o robo para e prepara a garra para pegar o objeto, pega o objeto 
# e se descola ate o ponto de encontro e solta o objeto.

import rospy
import time
import numpy as np

from geometry_msgs.msg import Twist, Vector3 # import lib para o cmd Vel
from sensor_msgs.msg import LaserScan   # import lib para sensor Lidar
from std_msgs.msg import Float32, String   # import lib para garra


garrapronta = 0
flagobjeto = 0

def scaneou(dado):
    global garrapronta
    global flagobjeto
    distfrente = dado.ranges[0]
#    disttras = dado.ranges[180]

    print("A distancia e: ", distfrente)
    print("valor garrapronta ", garrapronta)
    if (0.26 < distfrente < 3.5) and (distfrente != 0.0):
        andarobo()
    
    if (0.19 < distfrente <= 0.26) and (distfrente != 0.0):
        print("valor garrapronta ", garrapronta)
        if (garrapronta != 0) and (flagobjeto !=1):
            andarobodevagar()
        else:
            paradarobo()
            preparagarra()
    if (0.17 <= distfrente <= 0.19) and (distfrente != 0.0) and (garrapronta != 0) and (flagobjeto !=1):
        paradarobo()
        pegaobjeto() 
        print("proxima distancia.. else")

def pegaobjeto():
    global flagobjeto
    print("fecha a garra")
    posicao_garra.publish("fecha")
    time.sleep(2)
    print("prepara o braco")
    posicao_braco.publish("sobe")
    time.sleep(2)
    flagobjeto = 1

def andarobodevagar():
    print("agora, se aproxima bemmm devagar")
    velocidade = Twist(Vector3(0.02, 0, 0), Vector3(0, 0, 0))
    velocidade_saida.publish(velocidade)    

def preparagarra():
    global garrapronta
    print("prepara o braco")
    posicao_braco.publish("desce")
    time.sleep(2)
    print("prepara a garra")
    posicao_garra.publish("abre")
    time.sleep(2)
    print("valor garrapronta preparagarra ", garrapronta)
    garrapronta = 1  
    print("valor garrapronta preparagarra", garrapronta) 

def andarobo():
    print("entao, bora pra frente!!")
    velocidade = Twist(Vector3(0.1, 0, 0), Vector3(0, 0, 0))
    velocidade_saida.publish(velocidade)

def paradarobo():
    print("entao, pode parar!!")
    velocidade = Twist(Vector3(0, 0, 0), Vector3(0, 0, 0))
    velocidade_saida.publish(velocidade)


if __name__=="__main__":

    rospy.init_node("garra_scan")

    recebe_scan = rospy.Subscriber("/scan", LaserScan, scaneou)
    velocidade_saida = rospy.Publisher("/cmd_vel", Twist, queue_size = 3 )
    posicao_braco = rospy.Publisher("/servo_braco/command", String, queue_size = 1 )
    posicao_garra = rospy.Publisher("/servo_garra/command", String, queue_size = 1 )

    while not rospy.is_shutdown():
        print("Oeee")
#        velocidade = Twist(Vector3(0.1, 0, 0), Vector3(0, 0, 0))
#       velocidade_saida.publish(velocidade)
        rospy.sleep(2)

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
    disttras = dado.ranges[180]

    print("A distancia frente e: ", distfrente)
    print("A distancia tras e: ", disttras)
    print("valor garrapronta ", garrapronta)
    if (0.26 < distfrente < 3.5) and (distfrente != 0.0) and (flagobjeto !=1):
        andarobo()
    
    if (0.19 < distfrente <= 0.26) and (distfrente != 0.0) and (flagobjeto !=1):
        print("valor garrapronta ", garrapronta)
        if (garrapronta != 0) and (flagobjeto !=1):
            andarobodevagar()
        else:
            paradarobo()
            preparagarra()

    if (0.17 <= distfrente <= 0.19) and (distfrente != 0.0) and (garrapronta != 0) and (flagobjeto !=1):
        paradarobo()
        pegaobjeto() 
        print("peguei objeto")
    
    if flagobjeto == 1: # ja estou com o objeto vou levar para o ponto de encontro
        if (0.26 < disttras < 3.5) and (disttras != 0.0):
            andarobo()
            print("voltando...")
        if (0.19 < disttras <= 0.26) and (disttras != 0.0):
            print("valor garrapronta ", garrapronta)
            if (garrapronta != 0) and (flagobjeto !=1):
                andarobodevagar()
            else:
                paradarobo()
                soltaobjeto() 
                print("missao completa")   

def pegaobjeto():
    global flagobjeto
    print("fecha a garra")
    posicao_garra.publish("fecha")
    time.sleep(2)
    print("prepara o braco")
    posicao_braco.publish("sobe")
    time.sleep(2)
    flagobjeto = 1

def soltaobjeto():
    global garrapronta
    global flagobjeto
    print("desce o braco")
    posicao_braco.publish("desce")
    time.sleep(2)
    print("abre a garra")
    posicao_garra.publish("abre")
    time.sleep(2)
    velocidade = Twist(Vector3(-0.02, 0, 0), Vector3(0, 0, 0.1))
    velocidade_saida.publish(velocidade)    
    time.sleep(2)
    velocidade = Twist(Vector3(0, 0, 0), Vector3(0, 0, 0))
    velocidade_saida.publish(velocidade)    
    time.sleep(2)
    posicao_garra.publish("fecha")
    time.sleep(2)
    posicao_braco.publish("recolhe")
    time.sleep(2)
    flagobjeto = 0
    garrapronta = 0

def andarobodevagar():
    global flagobjeto
    if flagobjeto == 0:
        print("agora, se aproxima bemmm devagar")
        velocidade = Twist(Vector3(0.02, 0, 0), Vector3(0, 0, 0))
        velocidade_saida.publish(velocidade)  
    else:
        print("agora, se aproxima bemmm devagar")
        velocidade = Twist(Vector3(-0.02, 0, 0), Vector3(0, 0, 0))
        velocidade_saida.publish(velocidade)           

def preparagarra():
    global garrapronta
    print("prepara o braco")
    posicao_braco.publish("desce")
    time.sleep(2)
    print("prepara a garra")
    posicao_garra.publish("abre")
    time.sleep(2)
    garrapronta = 1  

def andarobo():
    global flagobjeto
    if flagobjeto == 0:
        print("entao, bora pra frente!!")
        velocidade = Twist(Vector3(0.1, 0, 0), Vector3(0, 0, 0))
        velocidade_saida.publish(velocidade)
    else:
        print("entao, bora pra frente!!")
        velocidade = Twist(Vector3(-0.1, 0, 0), Vector3(0, 0, 0))
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
        print("programa rodando...")
        rospy.sleep(1)

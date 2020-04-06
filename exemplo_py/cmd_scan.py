#! /usr/bin/env python
# exemplo adaptado alura


import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

acelera = 0.1
freia = 0.0
gira_direita = -0.2
gira_esquerda = 0.2
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

def callback(msg):    
    move = Twist()
    direita = round(msg.ranges[315],2)
    frente = round(msg.ranges[0],2)
    esquerda = round(msg.ranges[45],2)

    print('===================================================================')
    print('Esquerda --> ', esquerda, 'Frente  --> ', frente, 'Direita --> ', direita)
    print('===================================================================')
    print('')

    if (esquerda < 0.6) or (frente < 0.5) or (direita < 0.6):
        move.linear.x = freia
        print('============================ DESVIANDO ============================')
        if esquerda >= direita: 
            move.angular.z = gira_esquerda
        else:
            move.angular.z = gira_direita

    else:
        move.angular.z = 0.0
        move.linear.x = acelera

    pub.publish(move)


def main():
    rospy.init_node('drive')
    try:
        rospy.Subscriber('/scan', LaserScan, callback)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass


if __name__ == '__main__':
   main()

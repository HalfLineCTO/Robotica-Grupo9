# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 22:13:05 2023

@author: amesa
"""

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import numpy as np
from numpy import loadtxt
from servicio.srv import RutaTxt
import time



global msgVelocidad
global file
global msg




msgVelocidad = Twist()
file = []
msg = Twist()
posicion = []


class MinimalPlayer(Node):

    def __init__(self):
        
        # NodoPlayer es publisher en cmdVel
        super().__init__('turtle_bot_player')
        self.publisher_ = self.create_publisher(Twist, '/turtlebot_cmdVel', 10)
        
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        self.lineal = float(0)
        self.angular = float(0)
        
        
        # NodoPlayer es servidor 
    
        self.srv = self.create_service(RutaTxt, 'ruta', self.ruta_callback)
        
        
    def ruta_callback(self, request, response):
        global file
        #función que recibe la ruta del archivo
        #request seria un String
        #response es la respuesta que le doy al usuario
        #request es lo que recibo del servicio
       
       
        ruta = request.ruta
        file=loadtxt(ruta,dtype='float',delimiter=',')
        
        print('Se ha iniciado el servicio')


	# Este for da 10 segundos para que el usuario de la opcion de guardar el mapa y el texto si asi quiere, y no se pierdan datos por lectura rapida
        for i in range(10):
            time.sleep(1)
            comienza = 10 - i
            print("Se comienza en: "+str(comienza))
            
        return response
       
    def timer_callback(self):
        global msg
        global file
        
        
        # Se inicia un arreglo con el size del archivo que se carga desde interface
        
        a=np.size(file,axis=0)
        
        for i in range(a):
            datos=file[:][i]
            
            # Aca se puede ver que el archivo si se este leyendo
            print(file[:][i])
            
            # Las velocidades que se publican se leen desde la tuple que se lee del archivo
            msg.linear.x = datos[0]
            msg.angular.z = datos[1]
            
            
            # Se publica el mensaje en el topico
            self.publisher_.publish(msg)
            
            # Este tiempo es para que no se pierdan datos por una lectura muy rapida. Tal vez pueda cambiarse porque cuando se tienen archivos muy largos, se demora mucho en leer todo

            
        
def main(args=None):
    
    rclpy.init(args=args)
    turtle_bot_player = MinimalPlayer()
    rclpy.spin(turtle_bot_player)
    
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    turtle_bot_player.destroy_node()
    rclpy.shutdown()
    
if __name__ == '_main_':
    main()

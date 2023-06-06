# Interfaz

import pygame
import threading

from tkinter import filedialog
from tkinter import *
from tkinter.filedialog import asksaveasfile
import math
import numpy as np

import sys # Esto es para el servidor


import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String





global velocidades
global archivo_guardado
#global ruta
#global abrir_servidor




archivo_guardado = ''
#ruta=''
#abrir_servidor = True


# Posiciones empieza en 250,250 porque es el centro del canvas de pygame

velocidades = [0, 0]



# Se inicia la primera ventana
ventana = Tk()
ventana.geometry("300x300")



class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('robot_manipulador_interface')
        self.subscription = self.create_subscription(
            Twist,
            '/turtlebot_position',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        
        
        self.subscription_2 = self.create_subscription(
            Twist,
            '/cmdVel',
            self.listener_callback_2,
            10)
        self.subscription_2  # prevent unused variable warning
        
        
       
              

    def listener_callback(self,msg):

        global velocidades
        
        
        # Estas operaciones son transformaciones para que se vea mejor el mapa de pygame
        
        
    def listener_callback_2(self,msg):
        global velocidades

       
        
        
        # Estas velocidades se usan para el archivo txt
        
        
        
        self.servo = msg.linear.x
        self.primer_joint = msg.linear.y
        self.segundo_joint = msg.angular.z
        
            
        velocidades = [self.servo, self.primer_joint, self.segundo_joint]
        
        

        
        
def interfaz():

    global velocidades
    global archivo_guardado
  

    
    
    
    # Aqui va todo lo nuevo
    base_angle = np.pi/2
    base_length = 50
    lower_arm_length = 100
    upper_arm_length = 100
    lower_arm_angle = np.pi/2
    upper_arm_angle = 0
    lower_arm_x = 50 + base_length * np.sin(base_angle)
    lower_arm_y = 300 - base_length * np.sin(base_angle) 
    upper_arm_x = lower_arm_x + lower_arm_length * np.cos(lower_arm_angle)
    upper_arm_y = lower_arm_y - lower_arm_length * np.sin(lower_arm_angle)
    end_effector_x = upper_arm_x + upper_arm_length * np.cos(upper_arm_angle)
    end_effector_y = upper_arm_y + upper_arm_length * np.sin(upper_arm_angle)
    
    # Fuente y color del Texto del mapa de pygame
    smallfont = pygame.font.SysFont('Corbel',60)
    salir = smallfont.render('Cerrar' , True , (255,255,255))
    
    # Este cambio de posiciones se utiliza para graficar el recorrido del robot
    
    
    # Este es el size de la ventana y el titulo
    wn_width = 500
    wn_height = 500    
    wn = pygame.display.set_mode((wn_width, wn_height))
    end_effector_surface = pygame.Surface((wn_width, wn_height))
    pygame.display.set_caption("TurtleBot by El Androide Paranoide")



    # Aqui comienza todo el tema de eventos, dibujar en pygame y guardar los archivos
    state = True
    
    while state:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 0 <= mouse[0] <= 500 and 400 <= mouse[1] <= 500:
                    # Si se pulsa el boton de cerrar, se cierra pygame, y en caso de que se haya escogido guardar el mapa, tambien se guarda
                    if archivo_guardado:
                        pygame.image.save(wn, archivo_guardado)
                    pygame.quit()
                
        # Aqui se transforman las posiciones para que se grafique
        if velocidades[0] == 1.0:
            
            base_angle += np.radians(velocidades[1])   * 0.1        # 0.5 para controlar la velocidad de la grafica
            
        
            # estos if es porque las funciones trigonométricas se quedan en cero entonces no mueve el brazo bien
            if base_angle < np.pi/2:
                lower_arm_angle += np.radians(velocidades[2]) * 0.1
                lower_arm_x = 50 + base_length * np.sin(base_angle)
                lower_arm_y = 300 - base_length * np.sin(base_angle)
                
            else:
                lower_arm_angle -= np.radians(velocidades[2]) * 0.1
                lower_arm_x = 100 - base_length * np.cos(base_angle)
                lower_arm_y = 250 - base_length * np.cos(base_angle)
                
                
            
            # Estos corresponden al otro brazo. Se ponen acá para actualizar las longitudes y que todo mantenga su proporción
            upper_arm_x = lower_arm_x + lower_arm_length * np.cos(lower_arm_angle)
            upper_arm_y = lower_arm_y - lower_arm_length * np.sin(lower_arm_angle)
            
            # Prueba del end effector.
            end_effector_x = upper_arm_x + upper_arm_length * np.cos(upper_arm_angle)
            end_effector_y = upper_arm_y + upper_arm_length * np.sin(upper_arm_angle)
            
        elif velocidades[0] == 2.0:
            base_angle -= np.radians(velocidades[1]) * 0.1
            
            
            if base_angle < np.pi/2:
                lower_arm_angle -= np.radians(velocidades[2]) * 0.1
                lower_arm_x = 50 + base_length * np.sin(base_angle)
                lower_arm_y = 300 - base_length * np.sin(base_angle) 
            else:
                lower_arm_angle += np.radians(velocidades[2]) * 0.1
                lower_arm_x = 100 - base_length * np.cos(base_angle)
                lower_arm_y = 250 - base_length * np.cos(base_angle)
            
            # Los otros brazos
            upper_arm_x = lower_arm_x + lower_arm_length * np.cos(lower_arm_angle)
            upper_arm_y = lower_arm_y - lower_arm_length * np.sin(lower_arm_angle)
            end_effector_x = upper_arm_x + upper_arm_length * np.cos(upper_arm_angle)
            end_effector_y = upper_arm_y + upper_arm_length * np.sin(upper_arm_angle)
            
        elif velocidades[0] == 4.0:		   #inverti el 3 con el 4 para la grafica
            lower_arm_angle += np.radians(velocidades[2]) * 0.1
            upper_arm_angle += np.radians(velocidades[2]) * 0.1 #este era 0.075 y el de arriba 0.05
            upper_arm_x = lower_arm_x + lower_arm_length * np.cos(lower_arm_angle)
            upper_arm_y = lower_arm_y - lower_arm_length * np.sin(lower_arm_angle)
            
            # Movimiento del end effector 
            end_effector_x = upper_arm_x + upper_arm_length * np.cos(upper_arm_angle)
            end_effector_y = upper_arm_y + upper_arm_length * np.sin(upper_arm_angle)
            
        elif velocidades[0] == 3.0:
            lower_arm_angle -= np.radians(velocidades[2]) * 0.1
            upper_arm_angle -= np.radians(velocidades[2]) * 0.2
            upper_arm_x = lower_arm_x + lower_arm_length * np.cos(lower_arm_angle)
            upper_arm_y = lower_arm_y - lower_arm_length * np.sin(lower_arm_angle)
            
            # Movimiento del end effector 
            end_effector_x = upper_arm_x + upper_arm_length * np.cos(upper_arm_angle)
            end_effector_y = upper_arm_y + upper_arm_length * np.sin(upper_arm_angle)
        
            
            
            
        
       
        
        
        # Clear the screen and blit the line surface and the cursor image
        wn.fill((0,0,0))
        wn.blit(end_effector_surface, (0, 0))

        
        
        # Draw the rectangles and text
        pygame.draw.rect(wn,(0,255,255),[0,400,500,500])
        
        
        # Rectángulo para la base del manipulador
        pygame.draw.rect(wn,(255,255,255),[50, 300, 100, 100])
        
        # Líneas que representan cada brazo
        
        pygame.draw.line(wn, (255,255,255), (100, 300), (lower_arm_x, lower_arm_y)) # Línea desde la superficie al primer nodo
        pygame.draw.line(wn, (255,255,255), (lower_arm_x, lower_arm_y), (upper_arm_x, upper_arm_y)) # Línea desde el segundo nodo al tercer nodo
        pygame.draw.line(wn, (255,255,255), (upper_arm_x, upper_arm_y), (end_effector_x, end_effector_y)) # Línea desde primer nodo a segundo nodo
        
        # Círculos de cada nodo
        pygame.draw.circle(wn, (255,255,255), [lower_arm_x,lower_arm_y], 10, 1)
        pygame.draw.circle(wn, (255,255,255), [upper_arm_x, upper_arm_y], 10, 1)
        pygame.draw.circle(wn, (255,255,255), [end_effector_x, end_effector_y], 10, 1)
        
        # Dibujo del recorrido
        pygame.draw.circle(end_effector_surface, (255,0,0), [end_effector_x, end_effector_y], 1)
        
        
        
        
        
        wn.blit(salir, (200, 425))
        
        
        pygame.display.update()


       
        
        
        
        
        
        pygame.display.update()
        
            
            
# Todas estas funciones son para guardar el mapa, guardar el txt y abrir el archivo txt
def guardar_archivo(robot_manipulador_interface):
    global archivo_guardado
    archivo_guardado = filedialog.asksaveasfilename()

    
   
    
    
    

def main(args=None):
    rclpy.init(args=args)
    
    robot_manipulador_interface = MinimalSubscriber()
    
    
    
    
    # Botones de la primera ventana
    Button(text="Guardar Mapa", bg="light blue", command=lambda:guardar_archivo(robot_manipulador_interface)).place(relx=.10, rely=.10, relheight=.2, relwidth=.5)
    
    

    # Estos son los hilos para la ventana de tkinter y para pygame
    ventana.mainloop()
    pygame.init()
    
    t = threading.Thread(target = interfaz)
    t.setDaemon(True)
    t.start()
    
   
    rclpy.spin(robot_manipulador_interface)

 
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    robot_manipulador_interface.destroy_node()
    rclpy.shutdown()
    quit()
 
if __name__ == '__main__':
    main()


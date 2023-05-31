import rclpy                   # Importa el módulo de Python 'rclpy', que proporciona la API de ROS2 para Python
from rclpy.node import Node    # Importa la clase 'Node' de 'rclpy.node'
from geometry_msgs.msg import Twist   # Importa el mensaje 'Vector3' del paquete 'geometry_msgs'
import sys, select, tty, termios    # Importa algunos módulos de Python
from pynput import keyboard as kb


class TeleopManipulador(Node):    # Define una clase tipo 'Node'
    
        def __init__(self):    # Define un método llamado '__init__' que se ejecutará cuando se cree una instancia de la clase
                super().__init__('robot_manipulador_teleop')    # Llama al método '__init__' de la clase 'Node' y le da un nombre al nodo
                
                self.publisher_ = self.create_publisher(Twist, 'robot_manipulador_teleop', 10) #Publisher del mensaje Vector3
                
                
                
                # self.paso_lineal  = float(input("Ingrese tamaño del paso en grados entre 0 y 180: "))
                self.paso_angular  = float(70) #Prompt para ingresar el tamaño del paso para los servos
                print("Listo para teleoperar el robot manipulador")

        def on_press(self, key): 
        
                self.manip._1 = Twist() 
                self.manip._2 = Twist() 
                self.manip._3 = Twist() 
                self.manip._4 = Twist() 
        
                if key == kb.KeyCode.from_char('1'):    # Si la tecla pulsada es '1', establece paso angular positivo para el servo 1
                        self.manip._1= self.paso_angular #El movimiento del servo 1 
                        resp = print('Estas pulsando la tecla 1')
                elif key == kb.KeyCode.from_char('2'):    # Si la tecla es '2', Invierte el sentido de giro del servo 2
                        self.manip._1= -self.paso_angular
                        resp =  print('Estas pulsando la tecla 2')
                elif key == kb.KeyCode.from_char('3'):    # Con la tecla '3', se establece paso angular positivo para el servo 2
                        self.manip._2= self.paso_angular #El movimiento del servo 2 
                        resp =  print('Estas pulsando la tecla 3')
                elif key == kb.KeyCode.from_char('4'):    # Si la tecla es '4', Invierte el sentido de giro del servo 2
                        self.manip._2= -self.paso_angular
                        resp = print('Estas pulsando la tecla 4')
                elif key == kb.KeyCode.from_char('5'):    # Con la tecla '5', se establece paso angular positivo para el servo 3
                        self.manip._3= self.paso_angular #El movimiento del servo 3 
                        resp =  print('Estas pulsando la tecla 5')
                elif key == kb.KeyCode.from_char('6'):    # si  la tecla es '6', Invierte el sentido de giro del servo 3
                        self.manip._3= -self.paso_angular
                        resp =  print('Estas pulsando la tecla 6')
                elif key == kb.KeyCode.from_char('7'):    # Con la tecla '7', se establece paso angular positivo para el servo 4
                        self.manip._3= self.paso_angular #El movimiento del servo 4
                        resp =  print('Estas pulsando la tecla 7')
                elif key == kb.KeyCode.from_char('8'):    # si  la tecla es '8', Invierte el sentido de giro del servo 4
                        self.manip._3= -self.paso_angular
                        resp =  print('Estas pulsando la tecla 8')
                else:    # Si no se presionó ninguna de las teclas anteriores, establece ambas velocidades en cero
                        self.manip._1= self.paso_angular= 0.0 
                        self.manip._2= self.paso_angular= 0.0 
                        self.manip._3= self.paso_angular= 0.0 
                        self.manip._2= self.paso_angular= 0.0 
                self.get_logger().info('Sending - Paso angular  : %f' % (self.manip._1,self.manip._2,self.manip._3,self.manip._4))
                self.publisher_.publish(self.manip)  

        def on_release(self, key): #Al soltar la tecla vuelve todos los valores a cero
        
                self.manip._1 = Twist() 
                self.manip._2 = Twist() 
                self.manip._3 = Twist() 
                self.manip._4 = Twist() 
        
                if key == kb.KeyCode.from_char('1'):    # 
                        self.manip._1= 0.0
                        resp = print(' Dejó de pulsar la tecla 1')
                elif key == kb.KeyCode.from_char('2'):    # 
                        self.manip._1= -0.0
                        resp =  print('Dejó de pulsar  la tecla 2')
                elif key == kb.KeyCode.from_char('3'):    # 
                        self.manip._2= 0.0
                        resp =  print('Dejó de pulsar  la tecla 3')
                elif key == kb.KeyCode.from_char('4'):    # 
                        self.manip._2= -0.0
                        resp = print(' Dejó de pulsar la tecla 4')
                elif key == kb.KeyCode.from_char('5'):    #
                        self.manip._3= 0.0
                        resp =  print('Dejó de pulsar  la tecla 5')
                elif key == kb.KeyCode.from_char('6'):    # 
                        self.manip._3= -0.0
                        resp =  print('Dejó de pulsar  la tecla 6')
                elif key == kb.KeyCode.from_char('7'):    #
                        self.manip._4= 0.0
                        resp =  print('Dejó de pulsar  la tecla 7')
                elif key == kb.KeyCode.from_char('8'):    # 
                        self.manip._4= -0.0
                        resp =  print('Dejó de pulsar  la tecla 8')
                else:    # Si no se presionó ninguna de las teclas anteriores, establece ambas velocidades en cero
                        self.manip._x= self.paso_angular= 0.0 
                        self.manip._y= self.paso_angular= 0.0 
                        self.manip._z= self.paso_angular= 0.0 
                self.get_logger().info('Sending - Paso angular  : %f' % (self.manip._1,self.manip._2,self.manip._3,self.manip._4))
                self.publisher_.publish(self.manip)  
def main():
    rclpy.init()    # Inicializa ROS2
    robot_manipulador_teleop = TeleopManipulador()    # Crea una instancia de la clase 
    with kb.Listener(on_press= robot_manipulador_teleop.on_press,on_release = robot_manipulador_teleop.on_release) as escuchador:
        escuchador.join()
    print('Enviando datos al robot')
    rclpy.spin(robot_manipulador_teleop)    # Inicia el bucle de eventos de ROS2
    robot_manipulador_teleop.destroy_node()    # Destruye el nodo cuando se cierra el bucle de eventos
    rclpy.shutdown()    # Cierra ROS2

if __name__ == '__main__':
    main()    # Llama a la función 'main' si se ejecuta este archivo como un script

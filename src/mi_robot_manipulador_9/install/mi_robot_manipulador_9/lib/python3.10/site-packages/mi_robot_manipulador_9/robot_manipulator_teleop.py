import rclpy                   # Importa el módulo de Python 'rclpy', que proporciona la API de ROS2 para Python
from rclpy.node import Node    # Importa la clase 'Node' de 'rclpy.node'
from geometry_msgs.msg import Twist   # Importa el mensaje 'Twist' del paquete 'geometry_msgs'
from std_msgs.msg import String, Float64
import sys, select, tty, termios    # Importa algunos módulos de Python
from pynput import keyboard as kb

class MyMessage:
    def __init__(self):
        self.my_string = String() #Crea un objeto de tipo String
        self.my_float64 = Float64() #Crea un objeto de tipo Float64

class TeleopManipulador(Node):    # Define una clase tipo 'Node'
    
        def __init__(self):    # Define un método llamado '__init__' que se ejecutará cuando se cree una instancia de la clase
                super().__init__('robot_manipulador_teleop')    # Llama al método '__init__' de la clase 'Node' y le da un nombre al nodo que publica
                
                self.publisher_ = self.create_publisher(MyMessage(), 'Teleop_manipulador_topic', 10) #Publisher del mensaje
                
                print("Listo para teleoperar el robot manipulador") 

                ask_user=String(input("¿Desea definir la velocidad de los servos?: y/n")) #Velocidad de los servos
                
                if ask_user == "y":
                        vel_servo = float(input("Velocidad servo: "))
                else:
                        vel_servo = 70.0

                self.message = MyMessage() #Crea un objeto de tipo MyMessage
                self.message.my_string.data = "0" #Inicializa el mensaje con un string vacio
                self.message.my_float64.data = 0.0 #Inicializa el mensaje con un float vacio

        def on_press(self, key): 
        
        
                if key == kb.KeyCode.from_char('1'):    # Si la tecla pulsada es '1', establece paso angular positivo para el servo 1
                        self.message.my_string.data = "1" #El movimiento del servo 1 
                        self.message.my_float64.data = self.vel_servo #con un paso de 0 grados
                        resp = print('Estas pulsando la tecla 1')
                elif key == kb.KeyCode.from_char('2'):    # Si la tecla es '2', Invierte el sentido de giro del servo 2
                        self.message.my_string.data = "2" #El movimiento del servo 1 
                        self.message.my_float64.data = self.vel_servo 
                        resp =  print('Estas pulsando la tecla 2')
                elif key == kb.KeyCode.from_char('3'):    # Con la tecla '3', se establece paso angular positivo para el servo 2
                        self.message.my_string.data = "3" #El movimiento del servo 1 
                        self.message.my_float64.data = self.vel_servo 
                        resp =  print('Estas pulsando la tecla 3')
                elif key == kb.KeyCode.from_char('4'):    # Si la tecla es '4', Invierte el sentido de giro del servo 2
                        self.message.my_string.data = "4" #El movimiento del servo 1 
                        self.message.my_float64.data = self.vel_servo 
                        resp = print('Estas pulsando la tecla 4')
                elif key == kb.KeyCode.from_char('5'):    # Con la tecla '5', se establece paso angular positivo para el servo 3
                        self.message.my_string.data = "5" #El movimiento del servo 1 
                        self.message.my_float64.data = self.vel_servo 
                        resp =  print('Estas pulsando la tecla 5')
                elif key == kb.KeyCode.from_char('6'):    # si  la tecla es '6', Invierte el sentido de giro del servo 3
                        self.message.my_string.data = "6" #El movimiento del servo 1 
                        self.message.my_float64.data = self.vel_servo 
                        resp =  print('Estas pulsando la tecla 6')
                elif key == kb.KeyCode.from_char('7'):    # Con la tecla '7', se establece paso angular positivo para el servo 4
                        self.message.my_string.data = "7" #El movimiento del servo 1 
                        self.message.my_float64.data = self.vel_servo #
                        resp =  print('Estas pulsando la tecla 7')
                elif key == kb.KeyCode.from_char('8'):    # si  la tecla es '8', Invierte el sentido de giro del servo 4
                        self.message.my_string.data = "8" #El movimiento del servo 1 
                        self.message.my_float64.data = self.vel_servo #
                        resp =  print('Estas pulsando la tecla 8')
                else:    # Si no se presionó ninguna de las teclas anteriores, establece ambas velocidades en cero
                        self.message.my_string.data = "0" #El movimiento del servo 1
                        self.message.my_float64.data = 0.0 #
                
                self.get_logger().info('Sending - Data  : %f' % (self.message.my_float64.data, self.message.my_string.data ))
                self.publisher_.publish(self.message)  

        def on_release(self, key): #Al soltar la tecla vuelve todos los valores a cero
        
                if key == kb.KeyCode.from_char('1'):    # 
                        self.message.my_string.data = "1" #
                        self.message.my_float64.data = 0.0
                        resp = print(' Dejó de pulsar la tecla 1')
                elif key == kb.KeyCode.from_char('2'):    # 
                        self.message.my_string.data = "2"  
                        self.message.my_float64.data = 0.0 
                        resp =  print('Dejó de pulsar  la tecla 2')
                elif key == kb.KeyCode.from_char('3'):    # 
                        self.message.my_string.data = "3" #
                        self.message.my_float64.data = 0.0 
                        resp =  print('Dejó de pulsar  la tecla 3')
                elif key == kb.KeyCode.from_char('4'):    # 
                        self.message.my_string.data = "4" 
                        self.message.my_float64.data = 0.0 
                        resp = print(' Dejó de pulsar la tecla 4')
                elif key == kb.KeyCode.from_char('5'):    #
                        self.message.my_string.data = "5" 
                        self.message.my_float64.data = 0.0 
                        resp =  print('Dejó de pulsar  la tecla 5')
                elif key == kb.KeyCode.from_char('6'):    # 
                        self.message.my_string.data = "6" #
                        self.message.my_float64.data = 0.0 #
                        resp =  print('Dejó de pulsar  la tecla 6')
                elif key == kb.KeyCode.from_char('7'):    #
                        self.message.my_string.data = "7" # 
                        self.message.my_float64.data = 0.0 #
                        resp =  print('Dejó de pulsar  la tecla 7')
                elif key == kb.KeyCode.from_char('8'):    # 
                        self.message.my_string.data = "8" # 
                        self.message.my_float64.data = 0.0 #
                        resp =  print('Dejó de pulsar  la tecla 8')
                else:    # Si no se presionó ninguna de las teclas anteriores, establece ambas velocidades en cero
                        self.message.my_string.data = "0" #El movimiento de los servos
                        self.message.my_float64.data = 0.0 #con un paso de 0 grados
                
                self.get_logger().info('Sending - Data  : %f' % (self.message.my_float64.data, self.message.my_string.data ))
                self.publisher_.publish(self.message)  
def main(args=None):
    rclpy.init(args=args)    # Inicializa ROS2
    robot_manipulador_teleop = TeleopManipulador()
        # Crea una instancia de la clase 
    with kb.Listener(on_press= robot_manipulador_teleop.on_press,on_release = robot_manipulador_teleop.on_release) as escuchador:
        escuchador.join()
        print('Enviando datos al robot')
    rclpy.spin(robot_manipulador_teleop)    # Inicia el bucle de eventos de ROS2
    robot_manipulador_teleop.destroy_node()    # Destruye el nodo cuando se cierra el bucle de eventos
    rclpy.shutdown()    # Cierra ROS2

if __name__ == '__main__':
    main()    # Llama a la función 'main' si se ejecuta este archivo como un script

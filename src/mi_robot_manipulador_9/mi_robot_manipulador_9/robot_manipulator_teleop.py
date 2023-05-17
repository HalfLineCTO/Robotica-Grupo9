import rclpy                   # Importa el módulo de Python 'rclpy', que proporciona la API de ROS2 para Python
from rclpy.node import Node    # Importa la clase 'Node' de 'rclpy.node'
from geometry_msgs.msg import Vector3   # Importa el mensaje 'Vector3' del paquete 'geometry_msgs'
import sys, select, tty, termios    # Importa algunos módulos de Python
from pynput import keyboard as kb


class TeleopManipulador(Node):    # Define una clase tipo 'Node'
    
        def __init__(self):    # Define un método llamado '__init__' que se ejecutará cuando se cree una instancia de la clase
                super().__init__('robot_manipulador_teleop')    # Llama al método '__init__' de la clase 'Node' y le da un nombre al nodo
                
                self.publisher_ = self.create_publisher(Vector3, 'robot_manipulador_position', 10) #Publisher del mensaje Vecror3
                
                
                print("Ingrese los parametros")
                # self.paso_lineal  = float(input("Ingrese tamaño del paso en grados entre 0 y 180: "))
                self.paso_angular  = float(input("Ingrese tamaño del paso en grados entre 0 y 180: "))
    
        def on_press(self, key): 
        
                self.Vector3 = Vector3() 
        
                if key == kb.KeyCode.from_char('q'):    # Si la tecla es 'q', establece lineal positiva
                        self.Vector3._x= self.paso_angular
                        resp = print('Estas pulsando la tecla q')
                elif key == kb.KeyCode.from_char('Q'):    # Si la tecla es 'e', establece lineal negativa
                        self.Vector3._x= -self.paso_angular
                        resp =  print('Estas pulsando la tecla Q')
                elif key == kb.KeyCode.from_char('e'):    # 
                        self.Vector3._y= self.paso_angular
                        resp =  print('Estas pulsando la tecla e')
                elif key == kb.KeyCode.from_char('E'):    # 
                        self.Vector3._y= -self.paso_angular
                        resp = print('Estas pulsando la tecla E')
                elif key == kb.KeyCode.from_char('f'):    #
                        self.Vector3._z= self.paso_angular
                        resp =  print('Estas pulsando la tecla f')
                elif key == kb.KeyCode.from_char('F'):    # 
                        self.Vector3._z= -self.paso_angular
                        resp =  print('Estas pulsando la tecla F')
                else:    # Si no se presionó ninguna de las teclas anteriores, establece ambas velocidades en cero
                        self.Vector3._x= self.paso_angular= 0.0 
                        self.Vector3._y= self.paso_angular= 0.0 
                        self.Vector3._z= self.paso_angular= 0.0 
                self.get_logger().info('Sending - Paso angular  : %f' % (self.Vector3._x,self.Vector3._x,self.Vector3._x))
                self.publisher_.publish(self.Vector3)  

        def on_press(self, key): 
        
                self.Vector3 = Vector3() 
        
                if key == kb.KeyCode.from_char('q'):    # Si la tecla es 'q', establece lineal positiva
                        self.Vector3._x= 0.0
                        resp = print('Estas pulsando la tecla q')
                elif key == kb.KeyCode.from_char('Q'):    # Si la tecla es 'e', establece lineal negativa
                        self.Vector3._x= -0.0
                        resp =  print('Estas pulsando la tecla Q')
                elif key == kb.KeyCode.from_char('e'):    # 
                        self.Vector3._y= 0.0
                        resp =  print('Estas pulsando la tecla e')
                elif key == kb.KeyCode.from_char('E'):    # 
                        self.Vector3._y= -0.0
                        resp = print('Estas pulsando la tecla E')
                elif key == kb.KeyCode.from_char('f'):    #
                        self.Vector3._z= 0.0
                        resp =  print('Estas pulsando la tecla f')
                elif key == kb.KeyCode.from_char('F'):    # 
                        self.Vector3._z= -0.0
                        resp =  print('Estas pulsando la tecla F')
                else:    # Si no se presionó ninguna de las teclas anteriores, establece ambas velocidades en cero
                        self.Vector3._x= self.paso_angular= 0.0 
                        self.Vector3._y= self.paso_angular= 0.0 
                        self.Vector3._z= self.paso_angular= 0.0 
                self.get_logger().info('Sending - Paso angular  : %f' % (self.Vector3._x,self.Vector3._x,self.Vector3._x))
                self.publisher_.publish(self.Vector3)  
def main():
    rclpy.init()    # Inicializa ROS2
    robot_manipulador_teleop = TeleopManipulador()    # Crea una instancia de la clase 
    with kb.Listener(on_press= robot_manipulador_teleop.on_press,on_release = robot_manipulador_teleop.on_release) as escuchador:
        escuchador.join()
    print('Enviando datos a la raspberry')
    rclpy.spin(robot_manipulador_teleop)    # Inicia el bucle de eventos de ROS2
    robot_manipulador_teleop.destroy_node()    # Destruye el nodo cuando se cierra el bucle de eventos
    rclpy.shutdown()    # Cierra ROS2

if __name__ == '__main__':
    main()    # Llama a la función 'main' si se ejecuta este archivo como un script

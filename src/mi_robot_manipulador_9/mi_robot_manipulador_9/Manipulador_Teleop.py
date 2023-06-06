import rclpy
from rclpy.node import Node
from pynput.keyboard import Key, Listener
from geometry_msgs.msg import Twist
import time

#Aqui va lo de serial

import serial
import serial.tools.list_ports

###

global msg
msg = Twist()


class MinimalPublisher(Node):

    def __init__(self):
    	
        super().__init__('mi_robot_manipulador_teleop')
        self.publisher_ = self.create_publisher(Twist, '/cmdVel', 10)
        
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        ports = list(serial.tools.list_ports.comports())
        arduino_port = ports[0].device
        
        self.arduino = serial.Serial(port=arduino_port, baudrate=250000, timeout=.1)
        
        self.primer_joint = float(input("Introduzca la velocidad del joint 1: "))
        
        if self.primer_joint > 5:
            self.lineal = 5.0
            print("La velocidad maxima del joint 1 es 10 deg/s. Se ha establecido este valor como velocidad del primer joint.")
        elif self.primer_joint < 1:
            self.lineal = 1.0
            print("La velocidad minima del joint 1 es 5 deg/s. Se ha establecido este valor como velocidad del primer joint.")
            
        self.segundo_joint = float(input("Introduzca la velocidad del joint 2: "))
        
        
        if self.segundo_joint > 5:
            self.lineal = 5.0
            print("La velocidad maxima del joint 2 es 10 deg/s. Se ha establecido este valor como velocidad del primer joint.")
        elif self.primer_joint < 1:
            self.lineal = 1.0
            print("La velocidad minima del joint 2 es 5 deg/s. Se ha establecido este valor como velocidad del primer joint.")
            
            
        time.sleep(0.5)
        self.listener = Listener(on_press=self.on_press,on_release=self.on_release)
        self.listener.start()
        
        
        
        
        
        
        
    def on_press(self, Key):
        global msg
        
        
        if Key == Key.right:
        
            msg.linear.x = 1.0							# Esto representa el label que le damos a cada servo
            msg.linear.y = self.primer_joint
            msg.angular.z = self.segundo_joint
            y = f'{msg.linear.x},{msg.linear.y},{0},{0}'				# Esto es lo que se va a enviar por el serial
            
            self.write(y)
            
        
        elif Key == Key.left:
        
            msg.linear.x = 2.0
            msg.linear.y = self.primer_joint
            msg.angular.z = self.segundo_joint
            y = f'{msg.linear.x},{msg.linear.y},{0},{0}'				# Esto es lo que se va a enviar por el serial
            self.write(y)
        
        elif Key == Key.up:
            
            msg.linear.x = 3.0
            msg.linear.y = self.primer_joint
            msg.angular.z = self.segundo_joint
            y = f'{msg.linear.x},{0},{msg.linear.y},{0}'				# Esto es lo que se va a enviar por el serial
            self.write(y)
        
        elif Key == Key.down:
            
            msg.linear.x = 4.0
            msg.linear.y = self.primer_joint
            msg.angular.z = self.segundo_joint
            y = f'{msg.linear.x},{0},{msg.linear.y},{0}'				# Esto es lo que se va a enviar por el serial
            self.write(y)
        
        elif Key == Key.space:
            
            msg.linear.x = 5.0
            msg.linear.y = self.primer_joint
            msg.angular.z = self.segundo_joint
            y = f'{msg.linear.x},{0.0},{0.0},{2.0}'				# Esto es lo que se va a enviar por el serial
            self.write(y)
        
        elif Key == Key.backspace:
            
            msg.linear.x = 6.0
            msg.linear.y = self.primer_joint
            msg.angular.z = self.segundo_joint
            y = f'{msg.linear.x},{0.0},{0.0},{2.0}'				# Esto es lo que se va a enviar por el serial
            self.write(y)
        
        

        
            
    
    def on_release(self, Key):
        global msg
        msg.linear.x = 0.0
        msg.linear.y = self.primer_joint
        msg.angular.z = 0.0
        y = f'{0},{0},{0},{0}'				# Esto es lo que se va a enviar por el serial
        self.write(y)
        

        
 
 
           
    def timer_callback(self):
        global msg
        self.publisher_.publish(msg)
        
        

    def write(self, x):
        self.arduino.write(bytes(x, 'utf-8'))
        #print(self.arduino.readline().decode('utf-8'))  
        #print("Done")
    
    	
        
        
def main(args=None):

    rclpy.init(args=args)

    mi_robot_manipulador_teleop = MinimalPublisher()

    rclpy.spin(mi_robot_manipulador_teleop)
    

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    mi_robot_manipulador_teleop.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

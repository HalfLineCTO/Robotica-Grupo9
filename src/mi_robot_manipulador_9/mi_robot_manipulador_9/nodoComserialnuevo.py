#intento3ComSerial

#nodo comunicacion serial entre raspberry y arduino
import serial,time

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

global varArduino#direccion movimiento
varArduino='varArdu'
global velLineal #lineal y angular
velLineal='velLin' 
global arduino
arduino=serial.Serial("/dev/ttyACM0", 9600, timeout=1)


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('turtle_bot_comserial')
        self.subscription = self.create_subscription(
            Twist,
            '/turtlebot_cmdVel',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        

        
    def listener_callback(self,msg):
        #modifica global varArd

        
        global arduino
        global varArduino
        global velLineal
        if msg.linear.x>0:
            varArduino='U'#UP
        elif msg.linear.x<0:
            varArduino='D'#DOWN
        elif msg.angular.z<0:
            varArduino='R'#RIGHT
        elif msg.angular.z>0:
            varArduino='L'#LEFT
        else:
            varArduino='X'#QUIETO
        velLineal=str(msg.linear.x)
        print('asignó vel lineal')

        if arduino.isOpen():
        
           
            #print("{} connected!".format(arduino.port))
            #arduino.write(velLineal.encode())
            arduino.write(varArduino.encode())
            time.sleep(0.1)
            #print(velLineal)
            #print(varArduino)
            #arduino.flushInput()
            #print('entro a while')
           
            answer=str(arduino.readline())
            print("---> {}".format(answer))

     
def main(args=None):

    rclpy.init(args=args)
    
    
    turtle_bot_comserial = MinimalSubscriber()
    arduino=serial.Serial("/dev/ttyACM0", 9600, timeout=1)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    rclpy.spin(turtle_bot_comserial)
    turtle_bot_interface.destroy_node()
    rclpy.shutdown()
    quit()
 
if __name__ == '__main__':
    main()

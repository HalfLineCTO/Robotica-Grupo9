#!/usr/bin/env python3
import rclpy
import time
import serial
from rclpy.node import Node
from geometry_msgs.msg import Twist 

ser = serial.Serial("/dev/ttyACM0", baudrate=115200)

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('conectionserial')
        self.subscription = self.create_subscription(
            Twist,
            'robot_manipulador_teleop',
            self.listener_callback,
            10)


    def listener_callback(self, msg):
        comando = "0"
        if(self.manip._1  == 1.0):
            comando = "primero"
        elif(self.manip._2  == -1.0):
            comado = "primero negado"
        elif(self.manip._3  == 1.0):
            comando = "segundo"
        elif(self.msg.linear._4 == -1.0):
            comando = "segundo negado"
        if(self.manip._5  == 1.0):
            comando = "tercero"
        elif(self.manip._6  == -1.0):
            comado = "tercero negado"
        elif(self.manip._7  == 1.0):
            comando = "cuarto"
        elif(self.manip._8 == -1.0):
            comando = "cuarto negado"
        comando = comando + "\n"
        comandoBytes = comando.encode()
        ser.write(comandoBytes)
        time.sleep(0.2)
        self.get_logger().info(comando)


            
def main(args=None):
    rclpy.init(args=args)

    # Thread encargado de la interfaz.

    # Proceso principal encargado de recibir las posiciones "(x, y)"
    minimal_subscriber= MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    ser.close()
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

#prueba1 cinematica inversa
#instruccion para escribir en el topico goal
#ros2 topic pub - - once /robot_manipulador_goal geometry_msgs/Vector3 '{x: 10, y: 1, z:1 }'

import numpy as np
from scipy.optimize import fsolve
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3
import serial
import serial.tools.list_ports

global y1#param para arduino hombro
global y2#param para arduino codo

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('robot_manipulator_planner')#nodo
        self.subscription = self.create_subscription(
            Vector3,
            'robot_manipulator_goal',#topico
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        # Encontrar puerto automáticamente
        ports = list(serial.tools.list_ports.comports())
        arduino_port = ports[0].device

        self.arduino = serial.Serial(port=arduino_port, baudrate=250000, timeout=.1)
      
    def listener_callback(self,msg):
        global y1
        global y2
        a1 = 9#longitud link1 
        a2 = 9#longitud link2
        goalx = msg.x
        goaly = msg.y
        goalz = msg.z
        x0 = np.array([1, 1, 1, 1])
        x = fsolve(paramfun, x0, args=(a1, a2, goalx, goaly))
        thetacos = np.degrees(np.arccos([x[0], x[1]]))
        alpha = 90 - np.real(thetacos[0])
        beta = 180 - np.real(thetacos[1])
        y1 = -alpha + 180
        y2 = alpha + beta
        print("y1:", y1)
        print("y2:", y2)
        
        if msg.z == 0:
            y = f'{1000},{y2}'
        else:
        
            y=f'{y1},{y2}'
        print(y)
        self.write(y)
    
    def write(self, x):
        self.arduino.write(bytes(x, 'utf-8'))
        print(self.arduino.readline().decode('utf-8'))  
        print("Done")
                
def paramfun(x, a1, a2, goalx, goaly):
    F = [
        a1 * x[0] + a2 * (x[0] * x[1] - x[2] * x[3]) - goalx,
        a1 * x[2] + a2 * (x[2] * x[1] + x[0] * x[3]) - goaly,
        x[2] ** 2 + x[0] ** 2 - 1,
        x[1] ** 2 + x[3] ** 2 - 1
    ]
    return F

def main(args=None):
    rclpy.init(args=args)
    
    robot_manipulator_planner = MinimalSubscriber()

    
   
    rclpy.spin(robot_manipulator_planner)

 
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    robot_manipulator_planner.destroy_node()
    rclpy.shutdown()
    quit()
 
if __name__ == '__main__':
    main()



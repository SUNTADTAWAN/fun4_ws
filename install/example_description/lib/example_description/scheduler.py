#!/usr/bin/python3

from example_description.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PoseStamped, Twist
from std_msgs.msg import Int16

from roboticstoolbox import DHRobot ,RevoluteMDH

from math import pi
from spatialmath import *

import numpy as np

from fun4_interfaces.srv import Mode


class robot(DHRobot):
    def __init__(self):
        deg = pi / 180

        L1 = RevoluteMDH(
            a = 0.0, d = 0.2, alpha = 0.0
        )
        L2 = RevoluteMDH(
            a = 0.0, d = 0.06, alpha = -pi / 2,
            offset = -pi / 2 
        )
        L3 = RevoluteMDH(
            a = 0.25, d = 0.04, alpha = 0.0
        )

        L = [L1, L2, L3]

        super().__init__(
            L,
            name="robot"
        )

class SchedulerNode(Node):
    def __init__(self):
        super().__init__('scheduler_node')

        self.mode_send = self.create_publisher(Int16,'/mode',10)

        self.create_service(Mode,'/request_mode',self.request_mode_callback)      

    def request_mode_callback(self,request:Mode.Request , response:Mode.Response):
        if request.request_mode.data == 1:
            msg =  Int16()
            msg.data = 1
            self.mode_send.publish(msg)
            response.response_mode.data = True
            return response
        elif request.request_mode.data == 2:
            msg =  Int16()
            msg.data = 2
            self.mode_send.publish(msg)
            response.response_mode.data = True
            return response
        elif request.request_mode.data == 3:
            msg =  Int16()
            msg.data = 3
            self.mode_send.publish(msg)
            response.response_mode.data = True
            return response
        
    
        



def main(args=None):
    rclpy.init(args=args)
    node = SchedulerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()

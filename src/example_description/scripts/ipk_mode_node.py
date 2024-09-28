#!/usr/bin/python3

from example_description.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
import numpy as np

import roboticstoolbox as rtb
from spatialmath import SE3
from math import pi

class IpkmodeNode(Node):
    def __init__(self):
        super().__init__('ipk_mode_node')
        
        self.create_subscription(PoseStamped,'/end_effector',self.end_effector_callback,10)
        self.position_endeffector = [0.0,0.0,0.0]
        # T_0e_target = SE3.Trans(0.511, 0.684, 0.926) * SE3.RPY(np.pi/6, np.pi/4, np.pi/3)

    def dh_parameter(self,x,y,z):
        L1 = 0.2
        L2 = 0.25
        L3 = 0.15
        q = [0,-pi/2,pi/2]
        robot = rtb.DHRobot(
        [
        rtb.RevoluteMDH(a=0,alpha=0,d=L1),
        rtb.RevoluteMDH(a=0,alpha=-pi/2,d=-0.12),
        rtb.RevoluteMDH(a=L2,alpha=0,d=0.1),
        ],
        name = "Robot"
        )
        robot.tool = SE3.Trans(0.0, -(0.13+L3) ,0.0)
        inverse_kinemetic = robot.ikine_LM(SE3(x,y,z),mask=[1,1,1,0,0,0]) 
        
        # inverse_kinemetic = robot.ikine_LM()
        print(inverse_kinemetic)

    def end_effector_callback(self,msg:PoseStamped):
        self.position_endeffector[0] = msg.pose.position.x
        self.position_endeffector[1] = msg.pose.position.y
        self.position_endeffector[2] = msg.pose.position.z
        self.dh_parameter(self.position_endeffector[0],self.position_endeffector[1],self.position_endeffector[2])
        

        

def main(args=None):
    rclpy.init(args=args)
    node = IpkmodeNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()

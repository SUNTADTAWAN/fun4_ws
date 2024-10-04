#!/usr/bin/python3

from example_description.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PoseStamped,Twist
from std_msgs.msg import Int16
from sensor_msgs.msg import JointState

from roboticstoolbox import DHRobot ,RevoluteMDH
import roboticstoolbox as rtb

from math import pi
from spatialmath import *

import numpy as np

from fun4_interfaces.srv import Mode,Random

class ControlNode(Node):
    def __init__(self):
        super().__init__('control')

        # self.create_subscription(Twist,'/cmd_vel',self.cmd_vel_callback,10)
        self.create_subscription(JointState, "/joint_states",self.joint_states_callback,1)
        self.create_subscription(Int16,'/mode',self.mode_callback,10)
        self.create_subscription(PoseStamped,'/target',self.position_target_callback,10)

        self.end_effector_send = self.create_publisher(PoseStamped,'/end_effector',10)
        self.joint_pub = self.create_publisher(JointState, "/joint_states", 10)

        self.dt = 0.01 
        self.create_timer(self.dt, self.timer_callback)

        self.joint = [0.0,0.0,0.0]
        self.name = ["joint_1", "joint_2", "joint_3"]

        self.random_client = self.create_client(Random,'/request_target')

        self.position_target = np.array([0.0, 0.0, 0.0])
        
        self.q = np.array([0.0, 0.0, 0.0])
        self.inverse_kinemetic_sol = np.array([0.0, 0.0, 0.0])
        self.foward_kinemetic_sol = np.array([0.0, 0.0, 0.0])

        self.test = np.array([0.0, 0.0, 0.0])
        
        self.get_pose = 0

        self.robot = rtb.DHRobot(
        [
            rtb.RevoluteMDH(d=0.2),
            rtb.RevoluteMDH(alpha = -pi/2, d = -0.12, offset = -pi/2),
            rtb.RevoluteMDH(a = 0.25, d = 0.1, offset = pi/2),
        ],
        tool = SE3( 0,-0.28, 0) @ SE3.RPY(pi/2,0,0) ,
        name = "Robot"
        )
        # self.robot.tool = SE3( 0,-0.28, 0) @ SE3.RPY(pi/2,0,0) 

    


    def position_target_callback(self,msg):
        self.position_target[0] = msg.pose.position.x
        self.position_target[1] = msg.pose.position.y
        self.position_target[2] = msg.pose.position.z
        self.get_logger().info(f' {self.position_target}')
        self.get_pose = 1
    def timer_callback(self):
        pass
        

    def foward_kinemetic_cal(self,q1,q2,q3):
        # L1 = 0.2
        # L2 = 0.25
        # L3 = 0.15
        # q = [0+q1,-pi/2+q2,pi/2+q3]
        # robot = rtb.DHRobot(
        # [
        # rtb.RevoluteMDH(a=0,alpha=0,d=L1),
        # rtb.RevoluteMDH(a=0,alpha=-pi/2,d=-0.12),
        # rtb.RevoluteMDH(a=L2,alpha=0,d=0.1),
        # ],
        # name = "Robot"
        # )
        # Q = [0.0,0.0,0.0]
        # robot.tool = SE3( 0,-0.28, 0) @ SE3.RPY(pi/2,0,0) 

        q = [q1,q2,q3]
        foward_kinemetic = self.robot.fkine(q)
        self.foward_kinemetic_sol = self.robot.fkine(q)

        msg =  PoseStamped()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "link_0"
        msg.pose.position.x = foward_kinemetic.t[0]
        msg.pose.position.y = foward_kinemetic.t[1]
        msg.pose.position.z = foward_kinemetic.t[2]
        self.end_effector_send.publish(msg)

    def inverse_kinemetic_cal(self,x,y,z):
        L1 = 0.2
        L2 = 0.25
        L3 = 0.15
        q = [0,-pi/2,pi/2]
        robot = rtb.DHRobot(
        [def mode_callback(self,msg:Int16):
        if msg.data == 1:
            self.ipk_mode()
        elif msg.data == 2:
            self.teleop_mode()
        elif msg.data == 3:
            self.auto_mode()
        rtb.RevoluteMDH(a=0,alpha=0,d=L1),
        rtb.RevoluteMDH(a=0,alpha=-pi/2,d=-0.12),
        rtb.RevoluteMDH(a=L2,alpha=0,d=0.1),
        ],
        tool = SE3( 0,-0.28, 0) @ SE3.RPY(pi/2,0,0) ,
        name = "Robot"
        )
        self.get_logger().info(f'{x,y,z}')
        # robot.tool = SE3( 0,-0.28, 0) @ SE3.RPY(pi/2,0,0) 
        self.inverse_kinemetic_sol = robot.ikine_LM(SE3(x,y,z),mask=[1,1,1,0,0,0]) 
        self.inverse_kinemetic_sol.q[0] += q[0]
        self.inverse_kinemetic_sol.q[1] += q[1]
        self.inverse_kinemetic_sol.q[2] += q[2] 

        
    def joint_states_callback(self,msg:JointState):
        self.joint[0] = msg.position[0]
        self.joint[1] = msg.position[1]
        self.joint[2] = msg.position[2]
        self.foward_kinemetic_cal(self.joint[0],self.joint[1],self.joint[2])

    def mode_callback(self,msg:Int16):
        if msg.data == 1:
            self.ipk_mode()
        elif msg.data == 2:
            self.teleop_mode()
        elif msg.data == 3:
            self.auto_mode()

    def ipk_mode(self):
        self.inverse_kinemetic_cal(0.0,0.0,0.0)

    def teleop_mode(self):
        pass

    def auto_mode(self):
        
        msg1 = Random.Request()
        msg1.request_target.data = True
        self.random_client.call_async(msg1)

        self.get_logger().info(f'{self.position_target}')
        self.inverse_kinemetic_cal(self.position_target[0],self.position_target[1],self.position_target[2])
        self.get_logger().info(f'{self.inverse_kinemetic_sol}')
        
        msg2 = JointState()
        msg2.header.stamp = self.get_clock().now().to_msg()
        self.q[0] = self.inverse_kinemetic_sol.q[0]
        self.q[1] = self.inverse_kinemetic_sol.q[1]
        self.q[2] = self.inverse_kinemetic_sol.q[2]
        for i in range(len(self.q)):
            msg2.position.append(self.q[i])
            msg2.name.append(self.name[i])
        self.joint_pub.publish(msg2)

        self.foward_kinemetic_cal(self.q[0],self.q[1],self.q[2])
        self.get_logger().info(f'{self.foward_kinemetic_sol}')
        

def main(args=None):
    rclpy.init(args=args)
    node = ControlNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()

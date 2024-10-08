#!/usr/bin/python3

from example_description.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Bool
from fun4_interfaces.srv import Mode


import roboticstoolbox as rtb
from spatialmath import SE3
from math import pi

class ControllerNode(Node):
    def __init__(self):
        super().__init__('controller_node')
        self.joint_sub = self.create_subscription(JointState, "/joint_states",self.joint_states_callback,1)
        self.end_effector_send = self.create_publisher(PoseStamped,'/end_effector',10)
        
        self.joint = [0.0,0.0,0.0]

        
    def dh_parameter(self,q1,q2,q3):
        L1 = 0.2
        L2 = 0.25
        L3 = 0.15
        q = [0+q1,-pi/2+q2,pi/2+q3]
        robot = rtb.DHRobot(
        [
        rtb.RevoluteMDH(a=0,alpha=0,d=L1),
        rtb.RevoluteMDH(a=0,alpha=-pi/2,d=-0.12),
        rtb.RevoluteMDH(a=L2,alpha=0,d=0.1),
        ],
        name = "Robot"
        )
        Q = [0.0,0.0,0.0]
        robot.tool = SE3.Trans(0.0, -(0.13+L3) ,0.0)
        foward_kinemetic = robot.fkine(q)

        msg =  PoseStamped()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "link_0"
        msg.pose.position.x = foward_kinemetic.t[0]
        msg.pose.position.y = foward_kinemetic.t[1]
        msg.pose.position.z = foward_kinemetic.t[2]
        self.end_effector_send.publish(msg)


    def joint_states_callback(self,msg:JointState):
        self.joint[0] = msg.position[0]
        self.joint[1] = msg.position[1]
        self.joint[2] = msg.position[2]
        self.dh_parameter(self.joint[0],self.joint[1],self.joint[2])
        

        

def main(args=None):
    rclpy.init(args=args)
    node = ControllerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()

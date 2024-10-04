#!/usr/bin/python3

from example_description.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PoseStamped,Twist
from std_msgs.msg import Int16,Bool,Float64MultiArray
from sensor_msgs.msg import JointState

from roboticstoolbox import DHRobot ,RevoluteMDH
import roboticstoolbox as rtb

from math import pi
from spatialmath import *

import numpy as np
import matplotlib.pyplot as plt

from fun4_interfaces.srv import Mode,Random

class ControlallNode(Node):
    def __init__(self):
        super().__init__('control_all') 
        self.T = np.array([[0, 0, 1, 0.28],
                    [1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 0, 1]])
        self.tool = SE3(self.T)
        self.dh_model = DHRobot([
            RevoluteMDH(a=0      , alpha=0       , d=0.2 , offset=0),
            RevoluteMDH(a=0      , alpha=-np.pi/2, d=0.12   , offset=-np.pi/2),
            RevoluteMDH(a=0.25   , alpha=0       , d=-0.1, offset=0),
        ], tool=self.tool,
        name="my_robot")

        self.end_effector_pub = self.create_publisher(PoseStamped, "/end_effector", 10)
        self.joint_pub = self.create_publisher(JointState, "/joint_states", 10)

        self.joint_sub = self.create_subscription(JointState, "/joint_states",self.joint_sub_callback, 10)
        self.target_sub = self.create_subscription(PoseStamped,'/target',self.position_target_callback,10)
        self.target_manual_sub = self.create_subscription(Float64MultiArray,'/target_mode1',self.position_target_manual_callback,10)

        self.random_client = self.create_client(Random,'/request_target')
        
        self.create_service(Mode,'/request_mode',self.request_mode_callback)

        self.dt = 1
        self.create_timer(self.dt, self.sim_loop)

        self.name = ["joint_1", "joint_2", "joint_3"]

        self.q_solution = np.array([0.0,0.0,0.0])
        self.q = np.array([0.0, 0.0, 0.0])
        self.position = np.array([0.0,0.0,0.0])
        self.positionend = np.array([0.0,0.0,0.0])
        self.position_target = np.array([0.0,0.0,0.0])
        self.position_target_manual = np.array([0.0,0.0,0.0])
        self.joint = np.array([0.0,0.0,0.0])

        self.mode = False

        self.target_manual_ok = False
        self.first = True



    def first_time(self):
        if self.first == True:
            msg1 = Random.Request()
            msg1.request_target.data = True
            self.random_client.call_async(msg1)
            self.first = False
    
    def position_target_manual_callback(self,msg:Float64MultiArray):
        self.position_target_manual[0] = msg.data[0]
        self.position_target_manual[1] = msg.data[1]
        self.position_target_manual[2] = msg.data[2]

        self.target_manual_ok = True

    def joint_sub_callback(self, msg :JointState):
        self.joint[0] = msg.position[0]
        self.joint[1] = msg.position[1]
        self.joint[2] = msg.position[2]

        self.forward_end([self.joint[0],self.joint[1],self.joint[2]])
        
        pose = PoseStamped()
        pose.header.stamp = self.get_clock().now().to_msg()
        pose.header.frame_id = "link_0"
        pose.pose.position.x = self.positionend[0]
        pose.pose.position.y = self.positionend[1]
        pose.pose.position.z = self.positionend[2]
        self.end_effector_pub.publish(pose)


    def sim_loop(self):
        self.first_time()
        if self.mode == 1:
            self.mode_ipk()
        elif self.mode == 2:
            pass
        else:
            self.mode_auto()

    def position_target_callback(self,msg):
        self.position_target[0] = msg.pose.position.x
        self.position_target[1] = msg.pose.position.y
        self.position_target[2] = msg.pose.position.z
        self.get_logger().info(f' {self.position_target}')
        return self.position_target

    def mode_auto(self):
        msg1 = Random.Request()
        msg1.request_target.data = True
        self.random_client.call_async(msg1)

        self.get_logger().info(f'{self.position_target}')
        self.inverse([self.position_target[0],self.position_target[1],self.position_target[2]])
        self.get_logger().info(f'{self.q_solution}')
        self.forward([self.q_solution.q[0],self.q_solution.q[1],self.q_solution.q[2]])
        self.get_logger().info(f'{self.position}')

        msg2 = JointState()
        msg2.header.stamp = self.get_clock().now().to_msg()
        self.q[0] = self.q_solution.q[0]
        self.q[1] = self.q_solution.q[1]
        self.q[2] = self.q_solution.q[2]
        for i in range(len(self.q)):
            msg2.position.append(self.q[i])
            msg2.name.append(self.name[i])
        self.joint_pub.publish(msg2)

    def mode_ipk(self):
        if self.target_manual_ok == True:
            self.inverse([self.position_target_manual[0],self.position_target_manual[1],self.position_target_manual[2]])
            self.get_logger().info(f'Inverse kinemetic is : {self.q_solution}')
            self.target_manual_ok = False
            if self.q_solution is None:
                pass
            elif self.q_solution != None:
                msg = JointState()
                msg.header.stamp = self.get_clock().now().to_msg()
                self.q[0] = self.q_solution.q[0]
                self.q[1] = self.q_solution.q[1]
                self.q[2] = self.q_solution.q[2]
                for i in range(len(self.q)):
                    msg.position.append(self.q[i])
                    msg.name.append(self.name[i])
                self.joint_pub.publish(msg)
        

    def forward(self, joint_angles):
        joint_angles = np.array(joint_angles)
        T = self.dh_model.fkine(joint_angles)
        self.position = T.t
        return self.position
    
    def forward_end(self, joint_angles):
        joint_angles = np.array(joint_angles)
        T = self.dh_model.fkine(joint_angles)
        self.positionend = T.t
        return self.positionend
    
    
    def inverse(self, target_position):
        target_transform = SE3(target_position[0], target_position[1], target_position[2])
        self.q_solution = self.dh_model.ikine_LM(target_transform,mask = [1,1,1,0,0,0])
        if self.q_solution is None:
            self.get_logger().warn("No valid solutions found.")
            return None
        else:
            fk_solution = self.dh_model.fkine(self.q_solution.q)
            error = fk_solution.t - target_position
            print(f"IK solution: {self.q_solution.q}, Error: {error}")
            return self.q_solution.q
        
    def jacobian(self, q, v):
        J = self.robot.jacobe(q)[:3]
        if np.linalg.det(J) != 0:
            J_inv= np.linalg.inv(J)
            dq_dt = J_inv @ np.transpose(v)
        else:
            dq_dt = [0, 0, 0]
        return dq_dt
    

    def request_mode_callback(self,request:Mode.Request , response:Mode.Response):
        if request.request_mode.data == 1:
            self.get_logger().info(f'Mode 1 IPK Mode')
            self.mode = 1
            response.response_mode.data = True
            return response
        elif request.request_mode.data == 2:
            self.get_logger().info(f'Mode 2 Teleop Mode')
            self.mode = 2
            response.response_mode.data = True
            return response
        elif request.request_mode.data == 3:
            self.get_logger().info(f'Mode 3 Auto Mode')
            self.mode = 3
            response.response_mode.data = True
            return response


    def plot_workspace(self):
        x = np.linspace(-0.52, 0.52, 80)
        y = np.linspace(-0.52, 0.52, 80)
        z = np.linspace(-0.32, 0.72, 80)
        X, Y, Z = np.meshgrid(x, y, z)
        r = 0.03
        phi, theta = np.mgrid[0:2*np.pi:15j, 0:np.pi:15j]
        non_x = r * np.outer(np.cos(phi), np.sin(theta))
        non_y = r * np.outer(np.sin(phi), np.sin(theta))
        non_z = r * np.outer(np.ones(np.size(phi)), np.cos(theta)) + 0.2
        condition1 = (X**2 + Y**2 + (Z - 0.2)**2) >= 0.03**2
        condition2 = (X**2 + Y**2 + (Z - 0.2)**2) <= 0.53**2
        region = condition1 & condition2
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(X[region], Y[region], Z[region], color='blue', s=1, alpha=0.1, label='Workspace')
        ax.plot_surface(non_x, non_y, non_z, color='red', alpha=0.5, label='Non-Workspace')

        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')

        plt.show()

def main(args=None):
    rclpy.init(args=args)
    node = ControlallNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()

#!/usr/bin/python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from math import pi,sqrt
from spatialmath import *
import roboticstoolbox as rtb
import numpy as np
from geometry_msgs.msg import PoseStamped,Twist
from std_msgs.msg import String
from robot_interface.srv import Random,Mode
import random

class ControllerNode(Node):
    def __init__(self):
        super().__init__('controller_node')
        self.endeffector_pub = self.create_publisher(PoseStamped,'/end_effector',10)
        self.joint_pub = self.create_publisher(JointState, "/joint_states", 10)
        self.sigularity_pub = self.create_publisher(String, "/singularity_notify", 10)
        self.create_subscription(PoseStamped,'/target',self.target_callback,10)
        self.create_subscription(Twist,'/cmd_vel',self.cmd_vel_callback,10)
        self.random_client = self.create_client(Random,'/random')
        self.create_service(Mode,'/mode',self.mode_callback)
        self.dt = 0.01 
        self.create_timer(self.dt, self.sim_loop)
        self.q = [0, 0, 0]
        self.cmd_vel = [0.0, 0.0, 0.0]
        self.name = ["joint_1", "joint_2", "joint_3"]
        self.target = np.array([0.0,0.0,0.0])
        self.robot = rtb.DHRobot(
            [
                rtb.RevoluteMDH(d = 0.2),
                rtb.RevoluteMDH(alpha = -pi/2 , d=-0.12 , offset = -pi/2),
                rtb.RevoluteMDH(a=0.25,d= 0.10),
            ],
            name = "RRR_Robot"
            )
        self.tool_frame = SE3( 0,-0.28, 0) @ SE3.RPY(pi/2,0,0) 
        self.robot.tool = self.tool_frame
        print(self.robot)
        print(self.robot.fkine(self.q))
        self.flag = 0
        self.mode = 1
        self.waittopic = 0
        self.velo = [0, 0, 0]
        self.q_d = [[[0], [0], [0]]]
        self.delta_q = [0,0,0]
        self.kp = 1.0
        self.use_theta = [0,0,0]

    def cmd_vel_callback(self,msg:Twist):
        self.velo[0] = msg.linear.x
        self.velo[1] = msg.linear.y
        self.velo[2] = msg.linear.z
        print(self.velo)

    def mode_callback(self,request:Mode.Request, response:Mode.Response):
        if request.mode.data == 1:
            target = request.point.data 
            new_pose = SE3(target[0],target[1],target[2])
            self.posi = self.robot.ik_LM(new_pose,mask=[1,1,1,0,0,0])
            self.q_sol_ik_LM, *_ = self.robot.ik_LM(new_pose,mask=[1,1,1,0,0,0])
            print(self.robot.fkine(self.q_sol_ik_LM))
            if self.posi[1] == 1:
                print('True')
                response.change.data = True
                response.solution.data = self.q_sol_ik_LM.tolist()
                self.flag = 1
            else:
                print('False')
                response.change.data = False
            return response
        if request.mode.data == 2:
            self.flag = 2
            if request.mode_tele.data == 2:
                self.mode = 2
            else:
                self.mode = 1
            response.change.data = True
            return response
        if request.mode.data == 3:#auto
            msg3 = Random.Request()
            msg3.randomreq.data = 1
            self.random_client.call_async(msg3)
            self.flag = 3
            response.change.data = True
            return response
        else:
            pass
        
    def target_callback(self,msg:PoseStamped):
        self.target[0] = msg.pose.position.x
        self.target[1] = msg.pose.position.y
        self.target[2] = msg.pose.position.z
        self.get_logger().info(f'respond {self.target}')
        new_pose = SE3(self.target[0],self.target[1],self.target[2])
        self.q_sol_ik_LM, *_ = self.robot.ik_LM(new_pose,mask=[1,1,1,0,0,0])
        print(self.robot.fkine(self.q_sol_ik_LM))
        self.waittopic = 1
              
    def sim_loop(self):
        now_pose = [self.robot.fkine(self.q).A[0][3],self.robot.fkine(self.q).A[1][3],self.robot.fkine(self.q).A[2][3]]
        # self.get_logger().info(f'{now_pose}')
        msg2 = PoseStamped()
        msg2.header.frame_id = 'link_0'
        msg2.pose.position.x = now_pose[0]
        msg2.pose.position.y = now_pose[1]
        msg2.pose.position.z = now_pose[2]
        self.endeffector_pub.publish(msg2)
        if self.flag == 1:
            msg = JointState()
            msg.header.stamp = self.get_clock().now().to_msg()
            self.delta_q[0] = self.q_sol_ik_LM[0] - self.q[0]
            self.delta_q[1] = self.q_sol_ik_LM[1] - self.q[1]
            self.delta_q[2] = self.q_sol_ik_LM[2] - self.q[2]
            self.q[0] = self.q[0] + (self.delta_q[0]* self.kp * self.dt)
            self.q[1] = self.q[1] + (self.delta_q[1]* self.kp * self.dt)
            self.q[2] = self.q[2] + (self.delta_q[2]* self.kp * self.dt)
            # self.get_logger().info(f'{self.delta_q}')
            # self.q[0] = self.q_sol_ik_LM[0]
            # self.q[1] = self.q_sol_ik_LM[1]
            # self.q[2] = self.q_sol_ik_LM[2]
            for i in range(len(self.q)):
                msg.position.append(self.q[i])
                msg.name.append(self.name[i])
            self.joint_pub.publish(msg)
            if abs(self.delta_q[0]) < 0.01 and abs(self.delta_q[1]) < 0.01  and abs(self.delta_q[2]) < 0.01:
                self.flag = 0
        if self.flag == 2:
            msg4 = String()
            if self.mode == 1:
                v = np.array([[self.velo[0]],[self.velo[1]],[self.velo[2]]])
                de_J = [self.robot.jacob0(self.q)[0],self.robot.jacob0(self.q)[1],self.robot.jacob0(self.q)[2]]
                de_J_tran = np.transpose(de_J)
                m = sqrt(np.linalg.det(de_J @ de_J_tran))
                inv_J = np.linalg.inv([de_J])
                self.q_d,*_ = inv_J @ v
                print(self.q_d)
                if m > 0.01:
                    msg4.data = 'All good'
                    self.sigularity_pub.publish(msg4)
                elif m < 0.01 and m > 0.005:
                    msg4.data = 'Near singularity pls stop'
                    self.sigularity_pub.publish(msg4)
                    # self.get_logger().info(f'Near singularity pls stop')
                else:
                    msg4.data = 'Near Singularity pls change mode or reverse direction'
                    self.sigularity_pub.publish(msg4)
                    temp_q = [0.0 ,0.0,0.0]
                    temp_q[0] = self.q[0]+(self.q_d[0][0] * self.dt)
                    temp_q[1] = self.q[1]+(self.q_d[0][0] * self.dt)
                    temp_q[2] = self.q[2]+(self.q_d[0][0] * self.dt)
                    de_J2 = [self.robot.jacob0(temp_q)[0],self.robot.jacob0(temp_q)[1],self.robot.jacob0(temp_q)[2]]
                    de_J_tran2 = np.transpose(de_J2)
                    m2 = sqrt(np.linalg.det(de_J2 @ de_J_tran2))
                    if m2 <= m:
                        self.q_d = [[0.0], [0.0], [0.0]]
                    # self.get_logger().info(f'Singularity pls reset')
                msg = JointState()
                msg.header.stamp = self.get_clock().now().to_msg()
                self.q[0] = self.q[0] + (self.q_d[0][0] * self.dt)
                self.q[1] = self.q[1] + (self.q_d[1][0] * self.dt)
                self.q[2] = self.q[2] + (self.q_d[2][0] * self.dt)
                for i in range(len(self.q)):
                    msg.position.append(self.q[i])
                    msg.name.append(self.name[i])
                self.joint_pub.publish(msg)
            else:
                v = np.array([[self.velo[0]],[self.velo[1]],[self.velo[2]]])
                de_J = [self.robot.jacobe(self.q)[0],self.robot.jacobe(self.q)[1],self.robot.jacobe(self.q)[2]]
                de_J_tran = np.transpose(de_J)
                m = sqrt(np.linalg.det(de_J @ de_J_tran))
                inv_J = np.linalg.inv([de_J])
                self.q_d,*_ = inv_J @ v
                print(self.q_d)
                if m > 0.01:
                    msg4.data = 'All good'
                    self.sigularity_pub.publish(msg4)
                elif m < 0.01 and m > 0.005:
                    msg4.data = 'Near singularity pls stop'
                    self.sigularity_pub.publish(msg4)
                    # self.get_logger().info(f'Near singularity pls stop')
                else:
                    msg4.data = 'Near Singularity pls change mode or reverse direction'
                    self.sigularity_pub.publish(msg4)
                    temp_q = [0.0 ,0.0,0.0]
                    temp_q[0] = self.q[0]+(self.q_d[0][0] * self.dt)
                    temp_q[1] = self.q[1]+(self.q_d[0][0] * self.dt)
                    temp_q[2] = self.q[2]+(self.q_d[0][0] * self.dt)
                    de_J2 = [self.robot.jacobe(temp_q)[0],self.robot.jacobe(temp_q)[1],self.robot.jacobe(temp_q)[2]]
                    de_J_tran2 = np.transpose(de_J2)
                    m2 = sqrt(np.linalg.det(de_J2 @ de_J_tran2))
                    if m2 <= m:
                        self.q_d = [[0.0], [0.0], [0.0]]
                    # msg4.data = 'Singularity pls reset'
                    # self.sigularity_pub.publish(msg4)
                    # self.q_d = [[0.0], [0.0], [0.0]]
                    # self.get_logger().info(f'Singularity pls reset')
                msg = JointState()
                msg.header.stamp = self.get_clock().now().to_msg()
                self.q[0] = self.q[0] + (self.q_d[0][0] * self.dt)
                self.q[1] = self.q[1] + (self.q_d[1][0] * self.dt)
                self.q[2] = self.q[2] + (self.q_d[2][0] * self.dt)
                for i in range(len(self.q)):
                    msg.position.append(self.q[i])
                    msg.name.append(self.name[i])
                self.joint_pub.publish(msg)
        if self.flag == 3 and self.waittopic == 1:
            msg2 = PoseStamped()
            msg2.header.frame_id = 'link_0'
            msg2.pose.position.x = self.target[0]
            msg2.pose.position.y = self.target[1]
            msg2.pose.position.z = self.target[2]
            self.endeffector_pub.publish(msg2)
            msg = JointState()
            msg.header.stamp = self.get_clock().now().to_msg()
            self.delta_q[0] = self.q_sol_ik_LM[0] - self.q[0]
            self.delta_q[1] = self.q_sol_ik_LM[1] - self.q[1]
            self.delta_q[2] = self.q_sol_ik_LM[2] - self.q[2]
            self.q[0] = self.q[0] + (self.delta_q[0]* self.kp * self.dt)
            self.q[1] = self.q[1] + (self.delta_q[1]* self.kp * self.dt)
            self.q[2] = self.q[2] + (self.delta_q[2]* self.kp * self.dt)
            # self.get_logger().info(f'{self.delta_q}')
            # self.q[0] = self.q_sol_ik_LM[0]
            # self.q[1] = self.q_sol_ik_LM[1]
            # self.q[2] = self.q_sol_ik_LM[2]
            # self.use_theta[0] = np.arctan2(np.sin(self.delta_q[0]), np.cos(self.delta_q[0]))
            # self.use_theta[1] = np.arctan2(np.sin(self.delta_q[1]), np.cos(self.delta_q[1]))
            # self.use_theta[2] = np.arctan2(np.sin(self.delta_q[2]), np.cos(self.delta_q[2]))
            for i in range(len(self.q)):
                msg.position.append(self.q[i])
                msg.name.append(self.name[i])
            self.joint_pub.publish(msg)
            if abs(self.delta_q[0]) < 0.01 and abs(self.delta_q[1]) < 0.01  and abs(self.delta_q[2]) < 0.01 :
                msg3 = Random.Request()
                msg3.randomreq.data = 1
                self.random_client.call_async(msg3)
                self.waittopic = 0
def main(args=None):
    rclpy.init(args=args)
    node = ControllerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
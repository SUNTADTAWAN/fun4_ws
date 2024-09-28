#!/usr/bin/python3

from example_description.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node
import numpy as np
from geometry_msgs.msg import PoseStamped

from std_msgs.msg import Bool,Int16,Float32MultiArray
from fun4_interfaces.srv import Mode

class RandomNode(Node):
    def __init__(self):
        super().__init__('ramdom_node')
        self.create_service(Mode,'/request_target',self.request_target_callback)
        # self.create_service(Mode,'/run',self.request_target_callback)

        self.q = [0.0,0.0,0.0]#define q
        self.target = [0.0,0.0,0.0]

        # self.target_send = self.create_publisher(PoseStamped,'/target',10)

    def request_target_callback(self,request:Mode.Request , response:Mode.Response):
        self.get_logger().info(f'{self.random_target()}')
        response.response_target.data = self.random_target()
    
        return response

    def random_target(self):
        self.target[0] = np.random.uniform(0.03,0.53)
        self.target[1] = np.random.uniform(0.03,0.53)
        self.target[2] = np.random.uniform(0.03,0.53)
        self.get_logger().info(f'{self.target}')
        return self.target
        # msg =  PoseStamped()
        # msg.header.stamp = self.get_clock().now().to_msg()
        # msg.header.frame_id = "link_0"
        # msg.pose.position.x = self.target[0]
        # msg.pose.position.y = self.target[1]
        # msg.pose.position.z = self.target[2]
        # self.target_send.publish(msg)

    # def request_target_callback(self, request, response):
    #     pass
        


def main(args=None):
    rclpy.init(args=args)
    node = RandomNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()

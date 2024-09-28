#!/usr/bin/python3

from example_description.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node
import numpy as np
from geometry_msgs.msg import PoseStamped



class RandomNode(Node):
    def __init__(self):
        super().__init__('ramdom_node')

        # self.create_service(Mode,'/run',self.request_target_callback)

        self.tim = 100.0/100
        self.create_timer(self.tim,self.random_target)

        self.q = [0.0,0.0,0.0]#define q
        self.target = [0.0,0.0,0.0]
        self.target_send = self.create_publisher(PoseStamped,'/target',10)

    def random_target(self):
        self.target[0] = np.random.uniform(0.03,0.53)
        self.target[1] = np.random.uniform(0.03,0.53)
        self.target[2] = np.random.uniform(0.03,0.53)

        msg =  PoseStamped()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "link_0"
        msg.pose.position.x = self.target[0]
        msg.pose.position.y = self.target[1]
        msg.pose.position.z = self.target[2]
        self.target_send.publish(msg)

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

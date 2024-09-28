#!/usr/bin/python3

from example_description.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String



class DummyNode(Node):
    def __init__(self):
        super().__init__('teleop_mode_node')
        self.create_subscription(Twist,'/end_effector',self.teleop_callback,10)
        self.singularity_send = self.create_publisher(String,'/singularity',10)

    def teleop_callback(self):
        
        pass

def main(args=None):
    rclpy.init(args=args)
    node = DummyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()

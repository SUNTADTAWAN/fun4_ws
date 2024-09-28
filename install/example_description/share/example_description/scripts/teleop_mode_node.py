#!/usr/bin/python3

from example_description.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String

from std_msgs.msg import Bool,Int16
from fun4_interfaces.srv import Mode


class DummyNode(Node):
    def __init__(self):
        super().__init__('teleop_mode_node')
        self.create_subscription(Twist,'/end_effector',self.teleop_callback,10)
        self.singularity_send = self.create_publisher(String,'/singularity',10)

        self.create_service(Mode,'/request_mode',self.request_mode_callback)
    
    def request_Mode_callback(self,request:Mode.Request , response:Mode.Response):
        if request.request_mode.data:
            if request.request_mode.data == 2:
                response.response_mode.data = True
                self.get_logger().info(response.response_mode.data)
                return response
            

def main(args=None):
    rclpy.init(args=args)
    node = DummyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()

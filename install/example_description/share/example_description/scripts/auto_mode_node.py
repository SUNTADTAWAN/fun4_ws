#!/usr/bin/python3

from example_description.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool,Int16,Float32MultiArray
from fun4_interfaces.srv import Mode


class DummyNode(Node):
    def __init__(self):
        super().__init__('auto_mode_node')
        self.create_service(Mode,'/request_mode',self.request_Mode_callback)
        self.get_target_client = self.create_client(Mode,'/request_target')

        self.position_request = [0.0,0.0,0.0]

    def request_Mode_callback(self,request:Mode.Request , response:Mode.Response):
        if request.request_mode.data == 3:
            response.response_mode.data = True
            self.get_logger().info(f'True')

            self.position_request = Mode.Request.request_target
            self.get_target_client.call_async(self.position_request)

            return response
        



            
def main(args=None):
    rclpy.init(args=args)
    node = DummyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()

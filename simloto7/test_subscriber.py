import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Result(Node):
    def __init__(self):
        super().__init__("result")
        self.pub = self.create_subscription(String, "simloto7", self.cb, 10)
        
    def cb(self, msg):
        self.get_logger().info(msg.data)


def main():
    rclpy.init()
    node = Result()
    rclpy.spin(node)


# SPDX-FileCopyrightText: 2024 Itsuki Terasawa
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Test_Subscriber(Node):
    def __init__(self):
        super().__init__("test_subscriber")
        self.pub = self.create_subscription(String, "loto7", self.cb, 10)
        
    def cb(self, msg):
        self.get_logger().info(msg.data)


def main():
    rclpy.init()
    node = Test_Subscriber()
    rclpy.spin(node)


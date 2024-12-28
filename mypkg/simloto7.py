import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import numpy as np


rng = np.random.default_rng()


class loto7(Node):
    def __init__(self):
        super().__init__("loto7")
        self.pub = self.create_publisher(String, "loto7", 10)
        self.num_of_trials = 10000
        self.n = 0
        self.total_cost = 0
        self.total_num = 0
        self.earnings = 0
        self.earnings_and_expenses = 0
        self.recovery_rate = 0
        self.num_of_firstprize = 0
        self.create_timer(1.0, self.cb)

    def cb(self):
        for i in range(self.num_of_trials):
            self.n = rng.integers(10295472)
            if self.n == 0:
                self.earnings += 600000000
                self.num_of_firstprize += 1
            elif 0 < self.n <= 14:
                self.earnings += 7300000
            elif 14 < self.n <= 210:
                self.earnings += 730000
            elif 210 < self.n <= 9345:
                self.earnings += 9100
            elif 9345 < self.n <= 151445:
                self.earnings += 1400
            elif 151445 < self.n <= 393995:
                self.earnings += 1000
        self.total_cost += 300 * self.num_of_trials
        self.total_num += self.num_of_trials
        self.earnings_and_expenses = self.earnings - self.total_cost
        self.recovery_rate = round(float(self.earnings / self.total_cost * 100), 2)
        msg = String()
        msg.data = "購入金額: " + str(self.total_cost) + "円, 購入口数: " + str(self.total_num) + "枚, 当選金額: " + str(self.earnings) + "円, 収支: " + str(self.earnings_and_expenses) + "円, 回収率: " + str(self.recovery_rate) + "%, 1等当選回数: " + str(self.num_of_firstprize) + "回"
        self.pub.publish(msg)


def main():
    rclpy.init()
    node = loto7()
    rclpy.spin(node)

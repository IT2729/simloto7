import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import numpy as np


rng = np.random.default_rng()


class SimLoto7(Node):
    def __init__(self):
        super().__init__("simloto7")
        self.pub = self.create_publisher(String, "simloto7", 10)

        self.declare_parameter('num_of_trials', 10000)
        self.declare_parameter('price', 300)
        self.declare_parameter('total_num', 10295472)
        self.declare_parameter('num_of_first_prize', 1)
        self.declare_parameter('num_of_second_prize', 14)
        self.declare_parameter('num_of_third_prize', 196)
        self.declare_parameter('num_of_fourth_prize', 9135)
        self.declare_parameter('num_of_fifth_prize', 142100)
        self.declare_parameter('num_of_sixth_prize', 242550)
        self.declare_parameter('num_of_seventh_prize', 0)
        self.declare_parameter('num_of_eighth_prize', 0)
        self.declare_parameter('num_of_ninth_prize', 0)
        self.declare_parameter('prize_money_of_first', 600000000)
        self.declare_parameter('prize_money_of_second', 7300000)
        self.declare_parameter('prize_money_of_third', 730000)
        self.declare_parameter('prize_money_of_fourth', 9100)
        self.declare_parameter('prize_money_of_fifth', 1400)
        self.declare_parameter('prize_money_of_sixth', 1000)
        self.declare_parameter('prize_money_of_seventh', 0)
        self.declare_parameter('prize_money_of_eighth', 0)
        self.declare_parameter('prize_money_of_ninth', 0)

        self.num_of_trials = self.get_parameter('num_of_trials').get_parameter_value().integer_value
        self.price = self.get_parameter('price').get_parameter_value().integer_value
        self.total_num = self.get_parameter('total_num').get_parameter_value().integer_value
        self.num_of_first_prize = self.get_parameter('num_of_first_prize').get_parameter_value().integer_value
        self.num_of_second_prize = self.get_parameter('num_of_second_prize').get_parameter_value().integer_value
        self.num_of_third_prize = self.get_parameter('num_of_third_prize').get_parameter_value().integer_value
        self.num_of_fourth_prize = self.get_parameter('num_of_fourth_prize').get_parameter_value().integer_value
        self.num_of_fifth_prize = self.get_parameter('num_of_fifth_prize').get_parameter_value().integer_value
        self.num_of_sixth_prize = self.get_parameter('num_of_sixth_prize').get_parameter_value().integer_value
        self.num_of_seventh_prize = self.get_parameter('num_of_seventh_prize').get_parameter_value().integer_value
        self.num_of_eighth_prize = self.get_parameter('num_of_eighth_prize').get_parameter_value().integer_value
        self.num_of_ninth_prize = self.get_parameter('num_of_ninth_prize').get_parameter_value().integer_value
        self.prize_money_of_first = self.get_parameter('prize_money_of_first').get_parameter_value().integer_value
        self.prize_money_of_second = self.get_parameter('prize_money_of_second').get_parameter_value().integer_value
        self.prize_money_of_third = self.get_parameter('prize_money_of_third').get_parameter_value().integer_value
        self.prize_money_of_fourth = self.get_parameter('prize_money_of_fourth').get_parameter_value().integer_value
        self.prize_money_of_fifth = self.get_parameter('prize_money_of_fifth').get_parameter_value().integer_value
        self.prize_money_of_sixth = self.get_parameter('prize_money_of_sixth').get_parameter_value().integer_value
        self.prize_money_of_seventh = self.get_parameter('prize_money_of_seventh').get_parameter_value().integer_value
        self.prize_money_of_eighth = self.get_parameter('prize_money_of_eighth').get_parameter_value().integer_value
        self.prize_money_of_ninth = self.get_parameter('prize_money_of_ninth').get_parameter_value().integer_value
        self.n = 0
        self.total_cost = 0
        self.total_num_of_trials = 0
        self.earnings = 0
        self.earnings_and_expenses = 0
        self.recovery_rate = 0
        self.num_of_first_prize_winnings = 0

        self.create_timer(1.0, self.cb)

    def cb(self):
        for i in range(self.num_of_trials):
            self.n = rng.integers(self.total_num)
            if 0 <= self.n <= self.num_of_first_prize - 1:
                self.earnings += self.prize_money_of_first
                self.num_of_first_prize_winnings += 1

            elif self.num_of_first_prize - 1 < self.n <= self.num_of_first_prize + self.num_of_second_prize - 1:
                self.earnings += self.prize_money_of_second

            elif self.num_of_first_prize + self.num_of_second_prize - 1 < self.n <= self.num_of_first_prize + self.num_of_second_prize + self.num_of_third_prize - 1:
                self.earnings += self.prize_money_of_third

            elif self.num_of_first_prize + self.num_of_second_prize + self.num_of_third_prize - 1 < self.n <= self.num_of_first_prize + self.num_of_second_prize + self.num_of_third_prize + self.num_of_fourth_prize - 1:
                self.earnings += self.prize_money_of_fourth

            elif self.num_of_first_prize + self.num_of_second_prize + self.num_of_third_prize + self.num_of_fourth_prize - 1 < self.n <= self.num_of_first_prize + self.num_of_second_prize + self.num_of_third_prize + self.num_of_fourth_prize + self.num_of_fifth_prize - 1:
                self.earnings += self.prize_money_of_fifth

            elif self.num_of_first_prize + self.num_of_second_prize + self.num_of_third_prize + self.num_of_fourth_prize + self.num_of_fifth_prize - 1 < self.n <= self.num_of_first_prize + self.num_of_second_prize + self.num_of_third_prize + self.num_of_fourth_prize + self.num_of_fifth_prize + self.num_of_sixth_prize - 1:
                self.earnings += self.prize_money_of_sixth

            elif self.num_of_first_prize + self.num_of_second_prize + self.num_of_third_prize + self.num_of_fourth_prize + self.num_of_fifth_prize + self.num_of_sixth_prize - 1 < self.n <= self.num_of_first_prize + self.num_of_second_prize + self.num_of_third_prize + self.num_of_fourth_prize + self.num_of_fifth_prize + self.num_of_sixth_prize + self.num_of_seventh_prize - 1:
                self.earnings += self.prize_money_of_seventh

            elif self.num_of_first_prize + self.num_of_second_prize + self.num_of_third_prize + self.num_of_fourth_prize + self.num_of_fifth_prize + self.num_of_sixth_prize + self.num_of_seventh_prize - 1 < self.n <= self.num_of_first_prize + self.num_of_second_prize + self.num_of_third_prize + self.num_of_fourth_prize + self.num_of_fifth_prize + self.num_of_sixth_prize + self.num_of_seventh_prize + self.num_of_eighth_prize - 1:
                self.earnings += self.prize_money_of_eighth

            elif self.num_of_first_prize + self.num_of_second_prize + self.num_of_third_prize + self.num_of_fourth_prize + self.num_of_fifth_prize + self.num_of_sixth_prize + self.num_of_seventh_prize + self.num_of_eighth_prize - 1 < self.n <= self.num_of_first_prize + self.num_of_second_prize + self.num_of_third_prize + self.num_of_fourth_prize + self.num_of_fifth_prize + self.num_of_sixth_prize + self.num_of_seventh_prize + self.num_of_eighth_prize + self.num_of_ninth_prize - 1:
                self.earnings += self.prize_money_of_ninth
                
        self.total_cost += self.price * self.num_of_trials
        self.total_num_of_trials += self.num_of_trials
        self.earnings_and_expenses = self.earnings - self.total_cost
        self.recovery_rate = round(float(self.earnings / self.total_cost * 100), 2)

        msg = String()
        msg.data = "購入金額: " + str(self.total_cost) + "円, 購入口数: " + str(self.total_num_of_trials) + "枚, 当選金額: " + str(self.earnings) + "円, 収支: " + str(self.earnings_and_expenses) + "円, 回収率: " + str(self.recovery_rate) + "%, 1等当選回数: " + str(self.num_of_first_prize_winnings) + "回"
        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = SimLoto7()
    rclpy.spin(node)

# simloto7
<a href="https://github.com/IT2729/simloto7_ros2/actions/workflows/test.yml"><img src="https://github.com/IT2729/simloto7_ros2/actions/workflows/test.yml/badge.svg" alt="Test status"></a>
<a href="https://github.com/IT2729/simloto7_ros2/tree/main?tab=BSD-3-Clause-1-ov-file"><img alt="GitHub License" src="https://img.shields.io/github/license/IT2729/simloto7_ros2"></a>

## Description
LOTO7をシミュレートし、結果をパブリッシュするROS2パッケージです。

## Requirement
- ROS 2 Jazzy Jalisco
- Python 3.12 or later
- Pythonモジュール
    - NumPy 2.1.3 or later

## Nodes
### <a href="https://github.com/IT2729/simloto7_ros2/blob/main/simloto7/simloto7.py">simloto7</a>
LOTO7を指定された回数分シミュレートして結果をパブリッシュするノードです。メッセージ内容は購入金額、購入口数、当選金額、収支、回収率、1等当選回数の6項目です。デフォルトの当選金額は理論値を基にしています。

#### Subscribed topic
- loto7
    - LOTO7シミュレート結果

#### <a href="https://github.com/IT2729/simloto7_ros2/blob/main/config/params.yaml">Parameters</a>

|Name                    | Description              | Type | Default   |
|------------------------|--------------------------|------|-----------|
| num_of_trials          | メッセージごとの試行回数 | int  | 10000     |
| price                  | 一口の価格               | int  | 300       |
| total_num              | 全通り買う場合の数       | int  | 10295472  |
| num_of_first_prize     | 1等が当選する場合の数    | int  | 1         |
| num_of_second_prize    | 2等が当選する場合の数    | int  | 14        |
| num_of_third_prize     | 3等が当選する場合の数    | int  | 196       |
| num_of_fourth_prize    | 4等が当選する場合の数    | int  | 9135      |
| num_of_fifth_prize     | 5等が当選する場合の数    | int  | 142100    |
| num_of_sixth_prize     | 6等が当選する場合の数    | int  | 242550    |
| num_of_seventh_prize   | 7等が当選する場合の数    | int  | 0         |
| num_of_eighth_prize    | 8等が当選する場合の数    | int  | 0         |
| num_of_ninth_prize     | 9等が当選する場合の数    | int  | 0         |
| prize_money_of_first   | 1等当選金額              | int  | 600000000 |
| prize_money_of_second  | 2等当選金額              | int  | 7300000   |
| prize_money_of_third   | 3等当選金額              | int  | 730000    |
| prize_money_of_fourth  | 4等当選金額              | int  | 9100      |
| prize_money_of_fifth   | 5等当選金額              | int  | 1400      |
| prize_money_of_sixth   | 6等当選金額              | int  | 1000      |
| prize_money_of_seventh | 7等当選金額              | int  | 0         |
| prize_money_of_eighth  | 8等当選金額              | int  | 0         |
| prize_money_of_ninth   | 9等当選金額              | int  | 0         |

### <a href="https://github.com/IT2729/simloto7_ros2/blob/main/simloto7/test_subscriber.py">test_subscriber</a>
テスト用ノードです。

## Usage
以下を入力することで実行できます。
```
ros2 run simloto7 simloto7
```

また実行内容は別ターミナルで以下を入力することで確認できます。
```
ros2 topic echo /loto7
```

- Usage Example

## About Github Actions

## License

## Copyright

# simloto7
<a href="https://github.com/IT2729/simloto7_ros2/actions/workflows/test.yml"><img src="https://github.com/IT2729/simloto7_ros2/actions/workflows/test.yml/badge.svg" alt="Test status"></a>
<a href="https://github.com/IT2729/simloto7_ros2/tree/main?tab=BSD-3-Clause-1-ov-file"><img alt="GitHub License" src="https://img.shields.io/github/license/IT2729/simloto7_ros2"></a>

## Description
<a href="https://www.takarakuji-official.jp/kuji/loto/loto7/">LOTO7</a>をシミュレートし、結果をパブリッシュするROS2パッケージです。

## Requirement
- ROS 2 Jazzy Jalisco
- Python 3.12 or later
- Pythonモジュール
    - NumPy 2.1.3 or later

## Nodes
### simloto7
LOTO7を指定された回数分シミュレートして結果をパブリッシュするノードです。メッセージ内容は購入金額、購入口数、当選金額、収支、回収率、1等当選回数の6項目です。デフォルトの当選金額は理論値を基にしています。

#### Subscribed topic
- loto7
    - LOTO7シミュレート結果

#### Parameters

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

### test_subscriber
テスト用ノードです。

## Usage
simloto7は以下を入力することで実行できます。
```
ros2 run simloto7 simloto7
```

また実行内容は別ターミナルで以下を入力することで確認できます。
```
ros2 topic echo /loto7
```

- Usage Example
```
$ ros2 topic echo /loto7
data: '購入金額: 3000000円, 購入口数: 10000枚, 当選金額: 595200円, 収支: -2404800円, 回収率: 19.84％, 1等当選回数: 0回'
---
data: '購入金額: 6000000円, 購入口数: 20000枚, 当選金額: 1169200円, 収支: -4830800円, 回収率: 19.49％, 1等当選回数: 0回'
---
data: '購入金額: 9000000円, 購入口数: 30000枚, 当選金額: 1653200円, 収支: -7346800円, 回収率: 18.37％, 1等当選回数: 0回'
---
data: '購入金額: 12000000円, 購入口数: 40000枚, 当選金額: 2250000円, 収支: -9750000円, 回収率: 18.75％, 1等当選回数: 0回'
---
data: '購入金額: 15000000円, 購入口数: 50000枚, 当選金額: 2733800円, 収支: -12266200円, 回収率: 18.23％, 1等当選回数: 0回'
---
data: '購入金額: 18000000円, 購入口数: 60000枚, 当選金額: 3258500円, 収支: -14741500円, 回収率: 18.1％, 1等当選回数: 0回'
---
data: '購入金額: 21000000円, 購入口数: 70000枚, 当選金額: 3802100円, 収支: -17197900円, 回収率: 18.11％, 1等当選回数: 0回'
---
data: '購入金額: 24000000円, 購入口数: 80000枚, 当選金額: 4311100円, 収支: -19688900円, 回収率: 17.96％, 1等当選回数: 0回'
---
data: '購入金額: 27000000円, 購入口数: 90000枚, 当選金額: 4783300円, 収支: -22216700円, 回収率: 17.72％, 1等当選回数: 0回'
---
data: '購入金額: 30000000円, 購入口数: 100000枚, 当選金額: 5245100円, 収支: -24754900円, 回収率: 17.48％, 1等当選回数: 0回'
---
```

## About Github Actions
- <a href="https://github.com/IT2729/simloto7_ros2/blob/main/.github/workflows/test.yml">test</a>

| Purrose     | OS           | Language | Language Ver.     | Checkout Ver.     | Program   |
|-------------|--------------|----------|-------------------|-------------------|-----------|
| For testing | Ubuntu 22.04 | Python   | 3.12              | v4                | <a href="https://github.com/IT2729/simloto7_ros2/blob/main/test/test.bash">test.bash</a> |

## License
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを、本人の許可を得て自身の著作としたものです.
    - <a href="https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024">ryuichiueda/slides_marp robosys2024</a>

## Copyright
- © 2024 Itsuki Terasawa

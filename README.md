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
<table width="800">
  <thead>
    <tr>
      <th scope="col">Name</th>
      <th scope="col">Description</th>
      <th scope="col">Type</th>
      <th scope="col">Default</th>
    </tr>
  </thead>
  </tbody>
    <tr>
      <td width="30%">num_of_trials</td>
      <td width="40%">メッセージごとの試行回数</td>
      <td width="10%">int</td>
      <td width="20%">10000</td>
    </tr>
    <tr>
      <td>price</td>
      <td>一口の価格</td>
      <td>int</td>
      <td>300</td>
    </tr>
    <tr>
      <td>total_num</td>
      <td>全通り買う場合の数</td>
      <td>int</td>
      <td>10295472</td>
    </tr>
    <tr>
      <td>num_of_first_prize</td>
      <td>1等が当選する場合の数</td>
      <td>int</td>
      <td>1</td>
    </tr>
    <tr>
      <td>num_of_second_prize</td>
      <td>2等が当選する場合の数</td>
      <td>int</td>
      <td>14</td>
    </tr>
    <tr>
      <td>num_of_third_prize</td>
      <td>3等が当選する場合の数</td>
      <td>int</td>
      <td>196</td>
    </tr>
    <tr>
      <td>num_of_fourth_prize</td>
      <td>4等が当選する場合の数</td>
      <td>int</td>
      <td>9135</td>
    </tr>
    <tr>
      <td>num_of_fifth_prize</td>
      <td>5等が当選する場合の数</td>
      <td>int</td>
      <td>142100</td>
    </tr>
    <tr>
      <td>num_of_sixth_prize</td>
      <td>6等が当選する場合の数</td>
      <td>int</td>
      <td>242550</td>
    </tr>
    <tr>
      <td>num_of_seventh_prize</td>
      <td>7等が当選する場合の数</td>
      <td>int</td>
      <td>0</td>
    </tr>
    <tr>
      <td>num_of_eighth_prize</td>
      <td>8等が当選する場合の数</td>
      <td>int</td>
      <td>0</td>
    </tr>
    <tr>
      <td>num_of_ninth_prize</td>
      <td>9等が当選する場合の数</td>
      <td>int</td>
      <td>0</td>
    </tr>
    <tr>
      <td>prize_money_of_first</td>
      <td>1等当選金額</td>
      <td>int</td>
      <td>600000000</td>
    </tr>
    <tr>
      <td>prize_money_of_second</td>
      <td>2等当選金額</td>
      <td>int</td>
      <td>7300000</td>
    </tr>
    <tr>
      <td>prize_money_of_third</td>
      <td>3等当選金額</td>
      <td>int</td>
      <td>730000</td>
    </tr>
    <tr>
      <td>prize_money_of_fourth</td>
      <td>4等当選金額</td>
      <td>int</td>
      <td>9100</td>
    </tr>
    <tr>
      <td>prize_money_of_fifth</td>
      <td>5等当選金額</td>
      <td>int</td>
      <td>1400</td>
    </tr>
    <tr>
      <td>prize_money_of_sixth</td>
      <td>6等当選金額</td>
      <td>int</td>
      <td>1000</td>
    </tr>
    <tr>
      <td>prize_money_of_seventh</td>
      <td>7等当選金額</td>
      <td>int</td>
      <td>0</td>
    </tr>
    <tr>
      <td>prize_money_of_eighth</td>
      <td>8等当選金額</td>
      <td>int</td>
      <td>0</td>
    </tr>
    <tr>
      <td>prize_money_of_ninth</td>
      <td>9等当選金額</td>
      <td>int</td>
      <td>0</td>
    </tr>
  </tbody>
</table>

### <a href="https://github.com/IT2729/simloto7_ros2/blob/main/simloto7/test_subscriber.py">test_subscriber</a>
テスト用ノード

## Usage

## About Github Actions

## License

## Copyright

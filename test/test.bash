#!/bin/bash

error(){
	echo AN ERROR HAS OCCURRED IN TEST$t_num
	res=1
}

res=0

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch simloto7 test.launch.py > /tmp/mypkg.log

# 出力行数確認(test1)
t_num=1
out=$(cat /tmp/mypkg.log | grep "購入口数: 90000枚")
[ "${out}" = "" ] && error

# 出力内容確認1(test2)
t_num=2
out=$(sed -n 5p /tmp/mypkg.log | awk '{print $5}')
[ "${out}" = "購入金額:" ] || error

# エラーがなければOKを表示
[ "${res}" = 0 ] && echo OK

# 終了ステータスを返して終了
exit ${res}

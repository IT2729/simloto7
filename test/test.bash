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

# 出力内容確認2(test3)
t_num=3
out=$(sed -n 5p /tmp/mypkg.log | awk '{print $6}')
[ "${out}" = "3000000円," ] || error

# 出力内容確認3(test4)
t_num=4
out=$(sed -n 5p /tmp/mypkg.log | awk '{print $7}')
[ "${out}" = "購入口数:" ] || error

# 出力内容確認4(test5)
t_num=5
out=$(sed -n 5p /tmp/mypkg.log | awk '{print $8}')
[ "${out}" = "10000枚," ] || error

# 出力内容確認5(test6)
t_num=6
out=$(sed -n 5p /tmp/mypkg.log | awk '{print $9}')
[ "${out}" = "当選金額:" ] || error

# 出力内容確認6(test7)
t_num=7
out=$(sed -n 5p /tmp/mypkg.log | awk '{print $10}')
earnings=$(echo ${out%円,})
if [ $(($earnings % 100)) != 0 ]; then
	error
fi

# 出力内容確認7(test8)
t_num=8
out=$(sed -n 5p /tmp/mypkg.log | awk '{print $11}')
[ "${out}" = "収支:" ] || error

# 出力内容確認8(test9)
t_num=9
out=$(sed -n 5p /tmp/mypkg.log | awk '{print $12}')
earnings_and_expenses=$(echo ${out%円,})
if [ $(($earnings_and_expenses % 100)) != 0 ]; then
	error
fi

# 出力内容確認9(test10)
t_num=10
out=$(sed -n 5p /tmp/mypkg.log | awk '{print $13}')
[ "${out}" = "回収率:" ] || error

# 出力内容確認10(test11)
t_num=11
out=$(sed -n 5p /tmp/mypkg.log | awk '{print $14}')
recovery_rate=$(echo ${out%％,})
out=$(echo ${out} | grep '％,')
[ "${out}" = "" ] && error

# 出力内容確認11(test12)
t_num=12
out=$(sed -n 5p /tmp/mypkg.log | awk '{print $15}')
[ "${out}" = "1等当選回数:" ] || error

# エラーがなければOKを表示
[ "${res}" = 0 ] && echo OK

# 終了ステータスを返して終了
exit ${res}

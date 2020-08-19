#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/5/24   13:49
# @Author　 : mazm
# @ File　　  :test1.py
# @Software  :PyCharm

# __author__ = "Gao Zhengjie"
# __date__ = "2018/1/5"
# __Desc__ = 在命令行中实现进度条功能

# import time
#
# count_down = 10  # 设置倒计时时间，单位：秒
# interval = 1  # 设置屏幕刷新的间隔时间，单位：秒
# for i in range(0, int(count_down/interval)+1):
#     print("\r"+"▇"*i+" "+str(i*10)+"%", end="")
#     time.sleep(interval)
# print("\n加载完毕")

# __author__ = "Gao Zhengjie"
# __date__ = "2018/1/5"
# __Desc__ = 在一行中不断刷新倒计时

# import time
#
# count_down = 10  # 设置倒计时时间，单位：秒
# for i in range(count_down, 0, -1):
#     msg = u"\r系统将在 " + str(i) + "秒 内自动退出"
#     print(msg, end="")
#     time.sleep(1)
# end_msg = "结束" + "  "*(len(msg)-len("结束"))  # 如果单纯只用“结束”二字，无法完全覆盖之前的内容
# print(u"\r"+end_msg)

# __author__ = "Gao Zhengjie"
# __date__ = "2018/1/5"
# __Desc__ = 在一行中不断刷新转圈

import time

count_down = 10  # 设置倒计时时间，单位：秒
interval = 0.25  # 设置屏幕刷新的间隔时间，单位：秒
for i in range(0, int(count_down/interval)):
    ch_list = ["\\", "|", "/", "-"]
    index = i % 4
    msg = "\r程序运行中 " + ch_list[index]
    print(msg, end="")
    time.sleep(interval)
print(u"\r结束" + "  "*len(msg))
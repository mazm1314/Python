#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/5/14   16:55
# @Author　 : mazm
# @ File　　  :time.py
# @Software  :PyCharm

import time as t
# 查看该库中的所有方法
# print(dir(t))

import  time

print('休眠二秒打印出hello world,开始倒计时...')
time.sleep(2)
print('hello world')

#获取时间戳(1970年开始计时的)
print('获取时间戳:',time.time())

print('返回当前日期的字符串格式:\n',time.ctime())

print('时间戳转为字符串:\n',time.ctime(time.time()))

print('时间戳转为struct_time格式:\n',time.gmtime(time.time()))

time_gmtime=time.gmtime(time.time())
print('查看struct_time格式的显示年月日时分秒结果:\n',str(time_gmtime.tm_year)+'-'+str(time_gmtime.tm_mon)+'-'+str(time_gmtime.tm_mday)+' '+str(time_gmtime.tm_hour)+':'+str(time_gmtime.tm_min)+':'+str(time_gmtime.tm_sec))

print('时间戳转为struct_time,但是返回本地时间:\n',time.localtime(time.time()))

print('获取当前时间并且进行格式化:',time.strftime('%y-%m-%d %X',time.localtime()))

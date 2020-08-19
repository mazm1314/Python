#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/5/15   10:05
# @Author　 : mazm
# @ File　　  :sys.py
# @Software  :PyCharm
'''
sys
md5加密解密
'''
import sys

print(sys.argv)
# if sys.argv[1]=='sleep':
#     print('去睡觉')
# else:
#     print('无所谓')

# print(dir(sys))

print('获取python解释程序的版本信息:', sys.version)
print('获取最大的int值:', sys.maxsize)
print('获取操作系统平台名称:', sys.platform)

'''
1、标准库：E:\worksoftware\python\Lib
2、第三方库：E:\worksoftware\python\Lib\site-packages
3、自定义的库：
'''
print('返回模块的搜索路劲:\n')
for item in sys.path:
	print(item)

print('模拟进度条的实现:\n')
for i in range(10):
	sys.stdout.write('#')
	import time
	time.sleep(0.3)

print('\n读取屏幕的输入:\n')
val = sys.stdin.readline()[:-1]
print('屏幕输入的内容为:', val)
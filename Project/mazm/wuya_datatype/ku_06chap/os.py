#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/5/14   17:01
# @Author　 : mazm
# @ File　　  :os.py
# @Software  :PyCharm

import os
# print(dir(os))

# 获取当前文件的目录
# print(os.uname())

# 创建文件夹
# dira='e:/log'
# os.mkdir(dira)
# os.rmdir('e:/log')

# 修改目录名称
# os.rename('e:/log','e:/logs')

# 获取当前工作目录路径
# print(os.getcwd())

# 获取当前工作目录路径
# print(os.path.abspath('.'))

# 当前文件所在的目录
# current_work_dir = os.path.dirname(__file__)
# print(current_work_dir)
#
# f=open(os.path.join(current_work_dir,'time.py'),'r')
# print(f.read())

print('获取当前的工作目录：',os.getcwd())
print('返回当前目录：',os.curdir)
print('获取当前目录的父目录字符串名:',os.pardir)
# print('获取目录下的所有文件夹和文件:')
# for item in os.listdir('e:/'):
# 	print(item)

print('获取文件/目录信息:',os.stat('e:/'))
print('当前操作系统:',os.name)
# print('获取系统环境变量:',os.environ)
print('返回绝对路劲:',os.path.abspath('e:/worksoftware'))
print('对文件夹进行分割:',os.path.split('e:/worksoftware'))
print('获取path的目录:',os.path.dirname('e:/worksoftware'))
print('返回path目录的最后文件名:',os.path.basename('c:/'))
print('判断目录是否存在:',os.path.exists('c:/'))
print('判断是否是绝对路劲:',os.path.isabs('c:/'))
print('判断是否是文件:',os.path.isfile('c:/'))
print('判断是否是目录:',os.path.isdir('c:/'))
# print u'多个路劲进行组合:',os.path.join()
print('最后存取时间:',os.path.getatime('c:/'))
print('最后修改时间:',os.path.getmtime('c:/'))
#获取到目录： D:\git\Python\FullStack\Day5
print('获取当前路劲:', os.path.abspath(os.path.dirname(__file__)))
#到当前的项目目录下
print('获取当前路劲下的上一级目录:', os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print('对文件进行拼接:',os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'Data-Driver'))
#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/7/3   15:40
# @Author　 : mazm
# @ File　　  :alltest.py
# @Software  :PyCharm

import os
import unittest
import HTMLTestRunner
import time

# 获取testcase包下所有以test开头的文件
def allTest():
	suite=unittest.TestLoader().discover(
		start_dir=os.path.dirname(__file__),#获取当前文件夹
		pattern='test_*.py',#定义以什么开头
		top_level_dir=None
	)
	return suite

def getNowTime():
	return time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))

def run():
	fp=os.path.join(os.path.dirname(os.path.dirname(__file__)),'report',getNowTime()+'testReport.html')
	# print(type(fp))
	HTMLTestRunner.HTMLTestRunner(
		stream=open(fp,'wb'),
		title='自动化测试报告',
		description='自动化测试报告详细信息').run(allTest())

if __name__ == '__main__':
    run()

# run()
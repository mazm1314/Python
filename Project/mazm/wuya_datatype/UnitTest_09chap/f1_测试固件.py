#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/5/25   15:04
# @Author　 : mazm
# @ File　　  :unitTest.py
# @Software  :PyCharm
'''
2、测试固件
    1、setup&teardown

verbosity的讲解：verbosity是一个选项,表示测试结果的信息复杂度，有三个值
	1、0：(静默模式): 你只能获得总的测试用例数和总的结果 比如 总共100个 失败20 成功80
	2、1：(默认模式): 非常类似静默模式 只是在每个成功的用例前面有个“.”  每个失败的用例前面有个 “F”
	3、2：(详细模式):测试结果会显示每个测试用例的所有相关的信息
'''

import unittest
class f1(unittest.TestCase):

	# 测试固件
	def setUp(self):
		print('我已经做好准备')

	# 测试固件
	def tearDown(self):
		print('已处理')

	#   鼠标放在每个函数上，可以单独执行
	def test1(self):
		# self.assert_(1,'1')
		print('test')

	def test2(self):
		# self.assertEqual(1,2)
		print('test1')

	def test3(self):
		print('test2')


if __name__=='__name__':
	unittest.main(verbosity=2)


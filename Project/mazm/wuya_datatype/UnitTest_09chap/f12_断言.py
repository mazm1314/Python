#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/7/2   20:59
# @Author　 : mazm
# @ File　　  :f12_断言.py
# @Software  :PyCharm

import  unittest
from init import *


class BaiduLink(Init):

	def test_baidu_news(self):
		if self.driver.title=='百度一下你就知道':
			print('pass')
		else:
			print('fail')

	def test_baidu_news(self):
		try:
			self.assertEqual(self.driver.title,'百度一下你就知道')
		except Exception as e:
			print('fail info:{0}'.format(e.args))

	# def test_baidu_login(self):
	# 	so=self.driver.find_element_by_id('kw')
	# 	self.assertTrue(so.is_enabled())
	#
	# def test_baidu_tille(self):
	# 	self.assertIn('百度',self.driver.title)

if __name__ == '__main__':
	unittest.main(verbosity=2)

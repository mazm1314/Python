#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/7/2   20:42
# @Author　 : mazm
# @ File　　  :f9_优化测试套件.py
# @Software  :PyCharm

import  unittest
from init import *

class BaiduLink(Init):  #继承Init类即可

	def test_baidu_news(self):
		self.driver.find_element_by_link_text('新闻').click()

	def test_002(self):
		self.driver.find_element_by_link_text('地图').click()

	@staticmethod
	def suite():
		suite = unittest.TestSuite(unittest.makeSuite(BaiduLink))
		return suite

if __name__ == '__main__':
	unittest.TextTestRunner(verbosity=2).run(BaiduLink.suite())
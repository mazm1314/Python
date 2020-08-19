#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/7/2   20:10
# @Author　 : mazm
# @ File　　  :f5.py
# @Software  :PyCharm
'''
测试套件1的讲解:用例最好按照数字进行用例设计并且加注释

'''

import unittest
from selenium import webdriver


class BaiduTest(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Chrome()
		cls.driver.maximize_window()
		cls.driver.implicitly_wait(30)  # 隐式等待
		cls.driver.get('http://www.baidu.com')

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

	'''百度首页连接测试'''
	def test_baidu_mcp(self):
		'''测试首页学术的链接'''
		self.driver.find_element_by_link_text('学术').click()
		self.driver.back()

	def test_baidu_map(self):
		'''测试首页hao123的链接'''
		self.driver.find_element_by_link_text('hao123').click()
		# self.driver.back()
		self.driver.refresh()

	def test_baidu_mbp(self):
		'''测试首页地图的链接'''
		self.driver.find_element_by_link_text('地图').click()
		# self.driver.back()
		self.driver.refresh()


if __name__ == '__main__':
	suite=unittest.TestSuite()
	# addTest可以有顺序的执行---但是还是不对，所以还是后面用数字描述 test_baidu_001类似
	suite.addTest(BaiduTest('test_baidu_map'))
	suite.addTest(BaiduTest('test_baidu_mcp'))
	suite.addTest(BaiduTest('test_baidu_mbp'))
	unittest.TextTestRunner(verbosity=2).run(suite)

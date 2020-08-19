#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/7/3   15:14
# @Author　 : mazm
# @ File　　  :test_Baidu_link.py
# @Software  :PyCharm
import unittest
from selenium import webdriver

class test_Baidu_link(unittest.TestCase):

	def setUp(self):
		self.driver=webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.implicitly_wait(30)
		self.driver.get('http://www.baidu.com')

	def tearDown(self):
		self.driver.quit()

	def test_baidu_news(self):
		'''首页:点击新闻是否可正常的跳转'''
		self.driver.find_element_by_link_text('新闻').click()
		self.driver.refresh()
		self.assertEqual(self.driver.current_url, 'http://news.baidu.com/')

	def test_baidu_map(self):
		'''首页:点击地图是否可正常的跳转'''
		self.driver.find_element_by_link_text('地图').click()
		self.assertEqual(self.driver.current_url, 'https://map.baidu.com/')


if __name__ == '__main__':
    unittest.main(verbosity=2)
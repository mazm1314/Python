#!/usr/bin/env python 
#-*-coding:utf-8-*-

#author:wuya

import  unittest
from selenium import  webdriver

class Init(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.implicitly_wait(30)
		self.driver.get('http://www.baidu.com')

	def tearDown(self):
		self.driver.quit()

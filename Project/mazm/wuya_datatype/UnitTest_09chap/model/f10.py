#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/7/2   20:43
# @Author　 : mazm
# @ File　　  :f10_抽离f9中固件.py
# @Software  :PyCharm

import  unittest
from init import *


class BaiduSo(Init):  #继承Init类即可
	def test_baidu_news(self):
		self.driver.find_element_by_id('kw').send_keys('webdriver')

if __name__ == '__main__':
    unittest.main(verbosity=2)
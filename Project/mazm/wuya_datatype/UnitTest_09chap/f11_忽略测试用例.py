#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/7/2   20:55
# @Author　 : mazm
# @ File　　  :f11_忽略测试用例.py
# @Software  :PyCharm

from init import *

def add(a,b):
	return a-b

class BaiduLink(Init):
	# 第一种方法  @unittest.skip
	@unittest.skip('该功能已经取消，忽略该测试用例的执行')
	def test_baidu_news(self):
		self.driver.find_element_by_link_text('新闻').click()

	def test_002(self):
		self.driver.find_element_by_link_text('地图').click()

	# 第二种方法（期望让他失败）@unittest.expectedFailure
	@unittest.expectedFailure
	def test_003(self):
		self.assertEqual(add(3-2),1)


if __name__ == '__main__':
	unittest.main(verbosity=2)
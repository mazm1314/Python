#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/5/29   15:46
# @Author　 : mazm
# @ File　　  :f3.py
# @Software  :PyCharm
'''
执行顺序：按照ASCII的值的大小执行

test_001  先执行
test_002   后执行

test_baidu_map    先执行
test_baidu_mbp  后执行
'''



import  unittest
from selenium import  webdriver

class F2(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver=webdriver.Chrome()
		cls.driver.maximize_window()
		cls.driver.implicitly_wait(30)  #隐式等待
		cls.driver.get('http://www.baidu.com')


	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

	def test_baidu_mcp(self):
		self.driver.find_element_by_link_text('学术').click()
		self.driver.back()

	def test_baidu_map(self):
		self.driver.find_element_by_link_text('hao123').click()
		# self.driver.back()
		self.driver.refresh()

	def test_baidu_mbp(self):
		self.driver.find_element_by_link_text('地图').click()
		# self.driver.back()
		self.driver.refresh()

if __name__ == '__main__':
    unittest.main(verbosity=2)
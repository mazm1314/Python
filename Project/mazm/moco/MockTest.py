#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/7/2   11:15
# @Author　 : mazm
# @ File　　  :MockTest.py
# @Software  :PyCharm

from client_mock import *

import unittest
from unittest import  mock

class MockTest(unittest.TestCase):

	def test_fail_send(self):
		fail_code=mock.Mock(return_value='404')  #模拟返回值
		send_mazm=fail_code       #mock模拟了send_mazm()这个函数
		self.assertEqual(visit_mazm(),'404')


	def test_success_send(self):
		success_code=mock.Mock(return_value='200')  #模拟返回值
		send_mazm=success_code       #mock模拟了send_mazm()这个函数
		self.assertEqual(visit_mazm(),'200')


if __name__ == '__main__':
    unittest.main(verbosity=2)

# cmd命令运行：python -m unittest -v MockTest.MockTest
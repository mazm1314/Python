#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/7/2   10:57
# @Author　 : mazm
# @ File　　  :client_mock_test.py
# @Software  :PyCharm

from moco.client_mock import *
import unittest
from unittest import mock

class MazmTest(unittest.TestCase):
	def test_success(self):
		success_mazm=mock.Mock(return_value='200')
		send_mazm=success_mazm
		self.assertEqual(visit_mazm(),send_mazm())


if __name__ == '__main__':
    unittest.main()
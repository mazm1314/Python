#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/7/2   20:19
# @Author　 : mazm
# @ File　　  :f6.py
# @Software  :PyCharm
'''
测试套件2讲解：按照测试套件类讲解
解决一个类中有多个用例时，避免一个一个添加

'''


import  unittest

class F6(unittest.TestCase):
	def test_user_001(self):
		'''添加用户'''
		print('add')

	def test_user_002(self):
		'''删除用户'''
		print('del')

if __name__ == '__main__':
    suite=unittest.TestSuite()
    # suite.addTest('test_user_bbb')
    # suite.addTest('test_user_aaa')
    # 解决一个类中有多个用例时，避免一个一个添加
    suite.addTest(F6)
    unittest.TextTestRunner(verbosity=2).run(suite)
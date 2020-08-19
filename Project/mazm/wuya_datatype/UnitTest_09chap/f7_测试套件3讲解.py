#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/7/2   20:34
# @Author　 : mazm
# @ File　　  :f7_测试套件3讲解.py
# @Software  :PyCharm
'''
按照测试类执行（makesuite）
解决一个类中有多个用例的时候

问题：如果一个文件中有多个类呢？

'''
import  unittest

class F7(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_001(self):
		pass

	def test_002(self):
		pass

if __name__ == '__main__':
    suite=unittest.TestSuite(unittest.makeSuite(F7))
    unittest.TextTestRunner(verbosity=2).run(suite)

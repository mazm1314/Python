#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/6/24   19:37
# @Author　 : mazm
# @ File　　  :f1.py
# @Software  :PyCharm

import pytest

def test_001():
	assert 1==2

def test_002():
	assert 1==1


def add_test():#不执行，必须以test开头
	pass

class Test_f1: #类名以Test开头，并且T要大写
	def test_003(self):
		pass


# if __name__ == '__main__':
#     pytest.main(['-v','f1.py'])  #必须指定相应的测试模块

if __name__ == '__main__':
    pytest.main(['-v']) #此时要把f1.py的名称命名为:包含test

#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/6/24   20:05
# @Author　 : mazm
# @ File　　  :断言部分.py
# @Software  :PyCharm
import pytest

'''
1、==：内容与类型必须同时满足
2、in：后者包含前者
3、is：前后两个值相等
'''

def add(a,b):
	return a+b

def test_add_001():
	assert add(1,2)==3

def test_add_002():
	assert add(1,2)==2

def test_in_003():
	assert '测试' in '测试实战'
str1='admin'
str2='admin'

def test_is_004():
	assert str1 is str2

if __name__ == '__main__':
    pytest.main(['-v','断言部分.py'])
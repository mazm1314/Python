#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/6/24   20:14
# @Author　 : mazm
# @ File　　  :常用命令.py
# @Software  :PyCharm

'''
-v:  输出详细的信息  pytest -v
-s:   输出测试函数或者测试方法里面的print()里面的内容--主要用于调试  pytest -v -s
-k:按照分类执行测试点：pytest -v -k "ui or mazm" 常用命令_test.py
-m: 进行分组(分组不需要双引号)  pytest -v -m ui 常用命令_test.py
-x:执行失败后，后面的不会继续执行
--maxfail:执行失败的最大次数
	pytest -v --maxfail=1 常用命令_test.py
--tb=no :  关闭信息
--tb=short: 只输出assert的错误信息：多行展示  pytest -v --maxfail=1 常用命令_test.py --tb=short
--tb=line :一行展示所有错误信息
--ff:遇到错误继续执行

--duration=0:测试函数执行速度
'''

import pytest

@pytest.mark.ui
def test_add_003():
	print('把我打印出来')

@pytest.mark.mazm
def test_add_001():
	assert 1==2


@pytest.mark.hhh
def test_add_002():
	assert 1==1


#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/6/24   20:50
# @Author　 : mazm
# @ File　　  :webdriver实战_test.py
# @Software  :PyCharm


# pytest -v webdriver实战_test.py --driver Chrome


from selenium import webdriver
import pytest

driver=webdriver.chrome()

def test_baidu(selenium):
	selenium.get('www.baidu.com')
	assert selenium.title=='百度一下，你就知道'


if __name__ == '__main__':
    pytest.main(['-v'])


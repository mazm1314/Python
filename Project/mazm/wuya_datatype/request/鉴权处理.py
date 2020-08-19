#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/6/10   19:32
# @Author　 : mazm
# @ File　　  :鉴权处理.py
# @Software  :PyCharm

'''

'''
import  requests
from   requests.auth   import  HTTPBasicAuth


r=requests.get(
	# 查看用户的书籍信息
	url='http://127.0.0.1:5000/v1/api/books',
	auth=HTTPBasicAuth('admin','admin'))
print(r.text)
#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/5/18   19:11
# @Author　 : mazm
# @ File　　  :md5加密.py
# @Software  :PyCharm
'''
对请求参数做ascill吗的排序
做url encode编码：name=maazm&age=18&sex=girl
做md5--》sign
'''

from  urllib import parse
import  hashlib

def md5(**kwargs):
	dict2 = dict(sorted(kwargs.items()), key=lambda item: item[0])
	datas = parse.urlencode(dict2)
	request = hashlib.md5()
	request.update(datas.encode('utf-8'))
	return request.hexdigest()

sign=md5(name='mazm',age='18')
print(sign)
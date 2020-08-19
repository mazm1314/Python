#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/6/15   18:22
# @Author　 : mazm
# @ File　　  :请求方法的封装.py
# @Software  :PyCharm


'''
请求方法
请求地址
方法，地址 **kwargs
'''

import requests

class Method:
	def get(self, url, **kwargs):
		try:
			return requests.get(url=url, **kwargs)
		except BaseException as e:
			return e.args[0]

	def post(self, url, **kwargs):
		try:
			return requests.post(url=url, **kwargs)
		except BaseException as e:
			return e.args[0]

obj=Method()
url='http://aps.kp.ziroom.com/#/appManager/appBuildTask'
r=obj.get(url)
print(r.status_code)


'''第二种封装的思路'''
class Requests:
	def request(self,url,method='get',**kwargs):
		if method=='get':
			return requests.request(url=url,method=method,**kwargs)
		elif method=='post':
			return requests.request(url=url,method=method,**kwargs)

	def get(self,url,**kwargs):
		return self.request(url=url,**kwargs)

	def post(self,url,**kwargs):
		return self.request(url=url,method='post',**kwargs)
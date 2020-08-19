#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/6/24   10:31
# @Author　 : mazm
# @ File　　  :method.py
# @Software  :PyCharm
'''封装了request中的请求方法'''
import requests

class Requests:

	def request(self,url,method='get',**kwargs):
		if method=='get':
			return requests.request(url=url,method=method,**kwargs)
		elif method=='post':
			return requests.request(url=url,method=method,**kwargs)
		elif method=='put':
			return requests.request(url=url,method=method,**kwargs)
		elif method=='delete':
			return requests.request(url=url,method=method,**kwargs)

	def get(self,url,**kwargs):
		return self.request(url=url,**kwargs)

	def post(self,url,**kwargs):
		return self.request(url=url,method='post',**kwargs)

	def put(self,url,**kwargs):
		return self.request(url=url,method='put',**kwargs)

	def delete(self,url,**kwargs):
		return self.request(url=url,method='delete',**kwargs)

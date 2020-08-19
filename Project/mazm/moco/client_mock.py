#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/7/2   10:54
# @Author　 : mazm
# @ File　　  :client_mock.py
# @Software  :PyCharm


import requests
import shutil

def send_mazm(url):
	r=requests.get(url)
	return r.status_code


def visit_mazm():
	return send_mazm('http://www.mazm.com/')


class Remove():
	def rmdir(self,path='E:\log'):
		r=shutil.rmtree(path)
		if r==None:
			return 'success'
		else:
			return 'fail'

	def exit_get_rmdir(self):
		return self.rmdir()
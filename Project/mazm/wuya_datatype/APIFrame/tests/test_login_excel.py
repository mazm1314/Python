#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/6/27   20:25
# @Author　 : mazm
# @ File　　  :test_login_excel.py
# @Software  :PyCharm
'''

import json
import pytest
from APIFrame.utils.OperationExcel import operationExcel
from APIFrame.base.method import Requests
from APIFrame.commons.public import *

'''

# 面向对象的测试方案
#
# 1、测试从excel中读取文件并做请求，且请求数据维护在yaml文件中
# 2、并将结果写入到指定文件中：data\\login_write文件下


'''

class Testlogin():
	excel=operationExcel()
	obj=Requests()

	def result(self,r,row):
		assert r.status_code ==200
		# 将结果序列化，把dict-->str
		assert self.excel.getExcres(row=row) in  json.dumps(r.json())

	def test_login000(self):
		# 获取登陆的信息
		r=self.obj.post(url=self.excel.getUrl(2),data=self.excel.getJson(2),headers=eval(self.excel.getHeader(2)))
		self.result(r=r,row=2)

	def test_login001(self):
		# 将结果写到login_write中
		r=self.obj.post(url=self.excel.getUrl(3),data=self.excel.getJson(3),headers=eval(self.excel.getHeader(3)))
		# 将结果写到data\\login_write文件下
		writeContent(str(r.json()['resp']))




if __name__ == '__main__':
    pytest.main(['-v','-s'])


'''


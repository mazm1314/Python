#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/6/28   18:58
# @Author　 : mazm
# @ File　　  :Test_login_token.py
# @Software  :PyCharm


from APIFrame.utils.OperationExcel import *
from APIFrame.base.method import Requests
# from commons.public import filePath
import pytest
import json

execl=operationExcel()
obj=Requests()

@pytest.mark.parametrize('datas',execl.run())
def test_login(datas):

	# 对请求参数做:反序列化的处理
	params = datas[Excelinfo.params]
	if len(str(params).strip()) == 0:
		pass
	elif len(str(params).strip()) >= 0:
		params = json.loads(params)

	# 对请求头做:反序列化的处理
	header = datas[Excelinfo.headers]
	if len(str(header).strip()) == 0:
		pass
	elif len(str(header).strip()) >= 0:
		# excel中的请求必须是双引号，不然会报错:json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes
		header = json.loads(header)

		'''
		如果后续的接口需要token的值；
		1、我们先获取所有前置测试点的测试用例
		2、执行前置测试点获取他的结果信息
		3、拿他的结果信息替换对应测试点的变量
		'''
	# 	执行前置条件关联的测试点
	r = obj.post(
		url=execl.case_pre('login01')[Excelinfo.caseUrl],
		headers=json.loads(execl.case_pre('login01')[Excelinfo.headers]),
		data=json.loads(execl.case_pre('login01')[Excelinfo.params])
	)
	token = r.json()['resp']['token']

	# 替换被关联测试点中请求头信息的变量
	replce = execl.rep_params(token)

	status_code=int(datas[Excelinfo.statusCode])


	'''以下是测试用例开始执行'''
	if datas[Excelinfo.method] == 'get' and len(datas[Excelinfo.casePre]) > 0:
		r=obj.get(
			url=replce
		)
		print(r.json())
		assert r.status_code==status_code

	elif datas[Excelinfo.method] == 'get' and len(datas[Excelinfo.casePre]) == 0 :
		r = obj.get(
			url=datas[Excelinfo.caseUrl]
		)
		print(r.json())
		assert r.status_code == status_code

	elif datas[Excelinfo.method] == 'post':
		r=obj.post(
			url=datas[Excelinfo.caseUrl],
			headers=header,
			data=params
		)
		print(r.json())
		assert r.status_code == status_code

	elif datas[Excelinfo.method] == 'put':
		r=obj.put(
			url=datas[Excelinfo.caseUrl],
			headers=header,
			data=params
		)
		print(r.json())
		assert r.status_code == status_code

	elif datas[Excelinfo.method] == 'delete':
		r=obj.delete(
			url=datas[Excelinfo.caseUrl],
			headers=header,
			data=params
		)
		print(r.json())
		assert r.status_code == status_code

if __name__ == '__main__':
    pytest.main(['-v','-s',"--alluredir","./report/result"])
    import subprocess
    subprocess.call('allure generate report/result/ -o report/html --clean', shell=True)
    subprocess.call('allure open -h 127.0.0.1 -p  8088 ./report/html', shell=True)



#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/6/27   18:23
# @Author　 : mazm
# @ File　　  :OperationExcel.py
# @Software  :PyCharm
'''将excel和yaml文件链接起来
因为请求数据可变，维护在yaml文件中，通过excel的值和yaml文件的key将两者联系起来
'''

import xlrd
import json
from APIFrame.commons.public import filePath
from APIFrame.utils.OperationYAML import Operationyaml

class Excelinfo():

	caseID = "用例号"
	caseName = "用例名称"
	casePre = "前置条件"
	caseUrl = "请求链接"
	params = "请求参数"
	method = "请求方式"
	headers = "请求头"
	expect = "期望结果"
	true = "期望结果"
	isRun = "是否运行"
	statusCode = "状态码"

	# excel_ID=0
	# excel_name=1
	# excel_url=2
	# excel_data=3
	# excel_method=4
	# excel_headers=5
	# excel_exc_res=6
	# excel_tru_res=7
	# excel_result=8
	#
	# @property
	# def getID(self):
	# 	return self.excel_ID
	#
	# def getUrl(self):
	# 	return self.excel_url
	#
	# def getName(self):
	# 	return self.excel_name
	#
	# def getData(self):
	# 	return self.excel_data
	#
	# def getMethod(self):
	# 	return self.excel_method
	#
	# def getHeader(self):
	# 	return self.excel_headers
	#
	# def getExcres(self):
	# 	return self.excel_exc_res
	#
	# def getTrueres(self):
	# 	return self.excel_tru_res
	#
	# def getResult(self):
	# 	return self.excel_result


class operationExcel:

	# def getsheet(self):
	# 	login_mazm=xlrd.open_workbook(filePath('data','mazm.xls'))
	# 	return login_mazm.sheet_by_index(0)

	def getsheet(self):
		api=xlrd.open_workbook(filePath('data','api.xls'))
		return api.sheet_by_index(0)

	# @property   # 方法可以像属性一样访问。
	def getDatas(self):
		'''获取所有行的数据'''
		datas=list()
		title=self.getsheet().row_values(0)
		#忽略首行
		for item in range(1,self.getsheet().nrows):  #获取总行数
			row_values=self.getsheet().row_values(item)
			datas.append(dict(zip(title,row_values)))
		return datas

	def run(self):
		'''获取可执行的用例'''
		run_list=list()
		for item in self.getDatas():
			isrun=item[Excelinfo.isRun]
			if isrun == 'y':
				run_list.append(item)
			else:
				pass
		return run_list

	# def params(self):
	# 	'''对请求参数的空处理，并对不为空的进行序列化'''
	# 	list_params=[]
	# 	for items in self.run():
	# 		params=items[Excelinfo.params]
	# 		if len(str(params).strip()) == 0:pass
	# 		elif len(str(params).strip()) >= 0:
	# 			#excel中的请求必须是双引号，不然会报错
	# 			param_dict=json.loads(params)
	# 			return

	def case_list(self):
		'''获取到excel中所有的的测试用例'''
		cases=list()
		for item in self.getDatas():
			cases.append(item)
		return cases


	def case_pre(self,casePrev):
		'''
		根据关联条件找到需要关联的前置测试用例
		:param casePrev:前置测试条件
		:return:
		'''
		for items in self.case_list():
			if casePrev in items.values():
				return items
		return None


	def rep_params(self,repalce):
		'''
		替换请求参数需要登陆接口返回的token
		:param repalce:替换的参数
		:return:将结果返回
		'''
		for item in self.run():
			url_rep=item[Excelinfo.caseUrl]
			method=item[Excelinfo.method]
			if method=='get' and '{token}' in url_rep :
				rep_params=str(url_rep).replace('{token}',repalce)
				return rep_params


if __name__ == '__main__':
    obj=operationExcel()
    # print(obj.rep_params('hh'))
    for item in obj.run():
        print(len(item[Excelinfo.casePre]))

    # print(obj.case_pre('login01')[Excelinfo.caseUrl])
    # print(obj.rep_params('gg'))




	# @property
	# def getRow(self):
	# 	'''获取总行数'''
	# 	return self.getsheet().nrows
	#
	# @property
	# def getCols(self):
	# 	'''获取总列数'''
	# 	return self.getsheet().ncols
	#
	# def getvaleue(self,row,col):
	# 	'''获取具体位置的数据'''
	# 	return self.getsheet().cell_value(row,col)
	#
	# def getID(self,row):
	# 	return self.getvaleue(row=row,col=Excelinfo().getID)
	#
	# def getUrl(self,row):
	# 	return self.getvaleue(row=row,col=Excelinfo().getUrl())
	#
	# def getName(self,row):
	# 	return self.getvaleue(row=row,col=Excelinfo().getName())
	#
	# '''从yaml文件中获取请求参数'''
	# def getJson(self,row):
	# 	return self.dictYmal()[self.getData(row=row)]
	#
	# '''获取excel中的请求数据'''
	# def getData(self,row):
	# 	return self.getvaleue(row=row, col=Excelinfo().getData())
	#
	# def getHeader(self,row):
	# 	return self.getvaleue(row=row,col=Excelinfo().getHeader())
	#
	# def getExcres(self,row):
	# 	return self.getvaleue(row=row,col=Excelinfo().getExcres())
	#
	# def getTrueres(self,row):
	# 	return self.getvaleue(row=row,col=Excelinfo().getTrueres())
	#
	# def getResult(self,row):
	# 	return self.getvaleue(row=row,col=Excelinfo().getResult())


# if __name__ == '__main__':
#     obj=operationExcel()
#     # print(obj.getData(2))
#     # print(obj.getJson(2))
#     print(obj.getHeader(2))
#     # print(obj.getvaleue(2,1))


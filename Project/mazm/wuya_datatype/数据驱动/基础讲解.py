#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/6/15   18:47
# @Author　 : mazm
# @ File　　  :基础讲解.py
# @Software  :PyCharm

'''
需要安装：

https://pypi.python.org/pypi  官网下载包，然后到路径下面安装：python setup.py install
常用的库是 python-excel 系列：

       xlrd、xlwt、xlutils、openpyxl

xlrd － 读取 Excel 文件  缺点：会清空之前文件中的内容

xlwt － 写入 Excel 文件

xlutils － 操作 Excel 文件的实用工具，如复制、分割、筛选等

openpyxl  － 操作xlsx后缀的excel，实践发现 xlrd、xlwt、xlutils 可以读写操作elsx文件，但是实际保存后打不开，修改后缀为xls后方可正常打开，而程序是完成了正常的读写操作，只是人为不能正常打开文件，所以这里要增加一个新的模块。。


'''

import xlrd
import os
from xlutils.copy import  copy

def base_dir(filename=None):
	return os.path.join(os.path.dirname(__file__),filename)

'''excel文件的操作'''
# work=xlrd.open_workbook(base_dir('D:\Desktop\工作文件\mazm.xls'))
# sheet=work.sheet_by_index(0)
# #查看多少行
# print(sheet.nrows)
# #获取单元格的内容
# print(sheet.cell_value(1,1))


'''excel文件内容的修改'''
work=xlrd.open_workbook(base_dir('D:\Desktop\工作文件\mazm.xls'))
old_content=copy(work)
ws=old_content.get_sheet(0)
ws.write(1,1,'正常登陆222')
old_content.save(base_dir('D:\Desktop\工作文件\mazm.xls'))

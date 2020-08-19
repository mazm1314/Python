#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/6/24   17:38
# @Author　 : mazm
# @ File　　  :public.py
# @Software  :PyCharm

# os.path.dirname(__file__)  获取去掉文件名的文件目录
# os.path.dirname(os.path.dirname(__file__))   获取去掉文件名的上一层级的文件目录
#os.path.dirname(os.path.dirname(os.path.dirname(__file__)))   获取去掉文件名的上上一层级的文件目录
# os.path.join()拼接文件目录

import os

'''改文件封装了对指定文件下的文件的读写操作'''

def filePath(fileDir='config',fileName='login.yaml'):
	'''
	:param fileDir: 目录
	:param fileName: 文件名称
	:return:
	'''
	return os.path.join(
		os.path.dirname(os.path.dirname(__file__)),fileDir,fileName)

def writeContent(content):
	with open(filePath(fileDir='data',fileName='login_write.xls'),'w') as f:
		f.write(str(content))

def readContent():
	with open(filePath(fileDir='data',fileName='login_write.xls'), 'r') as f:
		return f.read()







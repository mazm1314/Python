#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/6/20   13:41
# @Author　 : mazm
# @ File　　  :csv读操作.py
# @Software  :PyCharm

import csv

# def readCsv():
# 	with open('D:\Desktop\工作文件\mazm.csv','r') as f:
# 		reader=csv.reader(f)  # 以列表的形式读取
# 		next(reader)
# 		db=[item for item in reader]
# 		print(db)
#
# res=readCsv()
# print(type(res))

def readCsv():
	with open('D:\Desktop\工作文件\mazm.csv','r') as f:
		reader=csv.DictReader(f) #以字典的形式读取
		for item in reader:
			print(item['url'])

readCsv()


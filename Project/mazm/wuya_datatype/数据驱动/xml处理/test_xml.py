#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/6/25   21:06
# @Author　 : mazm
# @ File　　  :test_xml.py
# @Software  :PyCharm

# 解决问题：
# 引入包报错：
# 将python下的dom放到pycharm的xml夹下：
# from
# E:\worksoftware\python\Lib\xml
# to
# E:\worksoftware\pycharm\PyCharm Community Edition 2020.1\plugins\python-ce\helpers\typeshed\stdlib\2and3\xml


import xml.dom.minidom
import os

def getxml(value=None):
	# 获取单节点的数据内容
	xmlfile=xml.dom.minidom.parse('data.xml')
	db=xmlfile.documentElement
	itemlist=db.getElementsByTagName(value)
	item=itemlist[0]
	return item.firstChild.data

print(getxml('admin'))

def getxmluser(parent='WuYA',child=None):
	# 获取单节点的数据内容
	xmlfile=xml.dom.minidom.parse('data.xml')
	db=xmlfile.documentElement
	itemlist=db.getElementsByTagName(parent)
	item=itemlist[0]
	return item.getAttribute(child)

# print(getxmluser('WuYA','nick')) #错误的代码
print(getxmluser(child='age'))
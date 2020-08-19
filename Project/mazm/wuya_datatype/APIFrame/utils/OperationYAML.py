#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/6/24   17:58
# @Author　 : mazm
# @ File　　  :OperationYAML.py
# @Software  :PyCharm
'''该文件主要是对一些可以存放在yaml文件中的用例进行操作'''


import yaml
from APIFrame.commons.public import filePath

class Operationyaml():
	'''读取Yaml文件中的内容'''
	def readYaml(self):
		with open(filePath(),'r',encoding='utf-8') as f:
			return list(yaml.safe_load_all(f))

	'''以字典的形式读取文件中的内容'''
	def dictYmal(self,fileDir='config',fileName='excel_config.yaml'):
		with open(filePath(fileDir=fileDir,fileName=fileName),'r',encoding='utf-8') as f:
			return yaml.safe_load(f)



if __name__ == '__main__':
    obj=Operationyaml()
    print(obj.dictYmal())
    # for items in obj.readYaml():
	#     print(items)


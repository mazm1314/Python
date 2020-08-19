#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/5/23   22:51
# @Author　 : mazm
# @ File　　  :factory.py
# @Software  :PyCharm

'''__doc__:打印出类的注释'''

# class Person(object):
# 	'''对人的定义'''
#
# 	def info(self,username,password):
# 		'''
# 		获取用户的信息
# 		:param username:用户名
# 		:param password:密码
# 		'''
# 		pass
#
# print(Person.__doc__)   #打印出类的注释


'''__call__:对象创建时直接返回__call__的内容,使用该方法可以模拟静态方法'''

# class P1(object):
# 	def __new__(cls, *args, **kwargs):
# 		print('call方法')
# p=P1()

'''
__str__:对象代表的含义，返回一个字符串,通过它可以把对象和字符串关联起来，方便某些程序的实现,
该字符串表示某个类,实现了__str__后，可以直接使用print语句输出对象,也可以通过函数str来触发__str__的执行

1.对象的意思
2.返回一个字符串，字符串和对象关联起来-->该字符串表示某个类
'''

# class Son(object):
# 	'''我是一个类'''
# 	def __str__(self):
# 		return self.__doc__
# s=Son()
# print(s.__str__())  #一般不调用内置方法打印结果
# print(str(s))

# class Factory(object):
# 	def createFruit(self,fruit):
# 		if fruit=='apple':
# 			return Apple()
# 		elif fruit=='banana':
# 			return Banana()
#
# class Fruit(object):
# 	def __str__(self):
# 		return 'fruit'
#
# class Apple(Fruit):
# 	def __str__(self):
# 		return 'apple'
#
# class Banana(Fruit):
# 	def __str__(self):
# 		return 'banana'
#
# if __name__ == '__main__':
#     factory=Factory()
#     print(factory.createFruit('apple'))
#     print(factory.createFruit('banana'))

from appium import  webdriver
from selenium import  webdriver
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.common.by import  By

class Factory(object):
	def createWebDdriver(self,webDdriver):
		if webDdriver=='web':
			return WebUI(self.driver)
		elif webDdriver=='app':
			return AppUI(self.driver)

class WebDdriver(object):
	def __init__(self,driver):
		self.driver=driver

	def __str__(self):
		return 'webDdriver'

	def findElement(self,*loc):
		try:
			return self.driver.find_element(*loc)
		except NoSuchElementException as e:
			print('Error details :%s'%(e.args[0]))

	def findsElement(self,*loc):
		try:
			return self.driver.find_elements(*loc)

		except NoSuchElementException as e:
			print('Error details :%s'%(e.args[0]))


class WebUI(WebDdriver):
	def __str__(self):
		return 'WEB UI'

class AppUI(WebDdriver):
	def __str__(self):
		return 'App UI'



















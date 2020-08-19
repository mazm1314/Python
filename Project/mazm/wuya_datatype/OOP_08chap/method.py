#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/5/22   17:15
# @Author　 : mazm
# @ File　　  :method.py
# @Software  :PyCharm

'''普通方法'''
# class Person(object):
# 	def conn(self,user,passwd,host,port):
# 		pass
#
# 	def f1(self,*args,**kwargs):
# 		pass
#
# 	def info(self):
# 		print('我是普通方法')
# per=Person()
# per.conn('root','root','locallhost','3306')
# per.f1()
# per.f1('as')
# per.f1(name="mazm")

'''
特性方法:
标识：@property
这个方法不能有形式参数
'''

# class Person(object):
# 	@property    #特性方法的标识
# 	def getUserID(self):
# 		pass
#
# per=Person()
# per.getUserID  #调用是不能有形式参数

'''
静态方法：直接使用类名来进行调用，它属于类
对象也可以调用静态方法，但是一般不建议这样做--为什么：多次一举
标识：@staticmethod

'''
# class MySQL(object):
# 	@staticmethod
# 	def conn(user): #静态方法没有self这个参数
# 		pass
#
# MySQL.conn('wuya')   #直接调用，不用实例化
# per=MySQL()   #对象也可以调用静态方法
# per.conn('wuya')

'''
类方法：直接使用类来进行调用，属于类
标识：@classmethod

'''
class Person(object):
	@classmethod
	def conn(cls):
		pass


'''
属于类：
     类属性
     静态方法
     类方法
属于对象：
       实例属性
       普通方法
       特性方法
'''
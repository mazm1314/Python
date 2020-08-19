#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/5/11   19:15
# @Author　 : mazm
# @ File　　  :decorator.py
# @Software  :PyCharm

import functools

'''
装饰器：
1、为什么要用装饰器？装饰器的作用就是为已经存在的函数或对象添加额外的功能

2、装饰器功能总结点：
  a、自动执行outer函数并且将其下面的函数名f1当作参数来传递；
  b、将outer函数的返回值(变量或者是函数)，重新赋值给f1；
  c、一旦结合装饰器后,调用f1其实执行的是log函数内部,原来的f1被覆盖；
  d、一旦这个函数被装饰器装饰之后，被装饰的函数重新赋值成装饰器的内层函数
  
3、被装饰器装饰的函数，一般分为二种情况；
	a、一种是没有返回值，对于一个函数来说，函数中没有return，那么函数的返回值就是None
	b、函数有返回值，那么装饰器就获取原函数的返回值
'''

'''
# 1、不用装饰器进行函数增加功能
def log():
	print('我是日志')

def f1():
	print('函数f1')
	log()
f1()
'''

'''
# 1、使用装饰器，
# 2、并且函数没有返回值:函数中没有return，那么函数的返回值就是None
# 3、没有参数的装饰器

def outer(func): #func值的是函数f1，也就是装饰器装饰的函数
	@functools.wraps(func)  #第一种解决函数名被更改的方法
	def log():
		print('我是日志')
		func()
	return log

@outer
def f1(): #函数作为装饰器的参数
	print('函数f1')
resu=f1()
print('函数中没有函数返回值：',resu)
'''

'''
# 1、使用装饰器，
# 2、并且函数有返回值:函数中有return，装饰器就获取原函数的返回值
# 3、没有参数的装饰器

def outer(func): #func值的是函数f1，也就是装饰器装饰的函数
	@functools.wraps(func)  #第一种解决函数名被更改的方法
	def log():
		print('我是日志')
		res=func()
		return res
	return log

@outer
def f1(): #函数作为装饰器的参数
	return '函数f1'

resu=f1()
print('函数中没有函数返回值：',resu)

'''
# 1、使用装饰器，
# 3、有参数的装饰器

def outer(func): #func值的是函数f1，也就是装饰器装饰的函数
	@functools.wraps(func)  #第一种解决函数名被更改的方法
	def log(*args,**kwargs):
		print('我是日志')
		res=func(*args,**kwargs)
		return res
	return log

@outer
def f1(a,b,c): #函数作为装饰器的参数
	print('和为:',a+b+c)
	# return a+b+c

resu=f1(1,2,3)
print('函数中没有函数返回值：',resu)






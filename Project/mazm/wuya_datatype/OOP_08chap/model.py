#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/5/21   18:54
# @Author　 : mazm
# @ File　　  :model.py
# @Software  :PyCharm
'''类：类是由一系列属性和方法组成'''

'''
对象的创建--->就是类实例化的过程
三个特性：
1.对象的句柄-->区分不同的对象
f2=F1()
f1=F1()
print id(f1)  #内存的地址不一样
print id(f2)  #内存的地址不一样
2.属性:
     共有属性:public
           类属性(共有的属性分离出来):它属于类，也属于对象,建议使用类调用
           实例属性:它只属于对象
           局部变量
           
     私有属性:privite
3.方法
'''


'''类属性和实例属性的案例代码'''
# class Person(object):
# 	# 类属性
# 	gontong='中国'
# 	def __init__(self,name,age):
# 		# 实例属性
# 		self.name=name
# 		self.age=age
# 		# 局部变量
# 		zone='空间'
# 	def getName(self):
# 		return self.name
# 	def getAge(self):
# 		return self.age
# 	def setName(self,name):
# 		self.name=name
# 	def setAge(self,age):
# 		self.age=age
# 	def info(self):
# 		return 'name:{0},age:{1}，来自于:{2}'.format(self.getName(),self.getAge(),self.gontong)
#
# per=Person('test',17)
# print(per.gontong)
# print(Person.gontong)



#
# per=Person('mazm',18)
# per1=Person('mazm1',19)
# per2=Person('test',78) #要传默认值
# # 给该对象设置值
# per2.setAge(23)
# per2.setName('hhh')
# print(per.getAge(),per.getName())
# print(per1.getAge(),per1.getName())
# print(per2.getAge(),per2.getName())
# print(per.info())
# print(per1.info())
# print(per2.info())

'''动态参数在类中的应用'''
# class Person(object):
# 	def __init__(self,*args,**kwargs):
# 		self.args=args
# 		self.kwargs=kwargs
#
# 	def info(self):
# 		print('信息:',self.args)
#
# per=Person('mazm',18,'djj')
# per.info()

'''
首先一个类，不管是否写了构造函数，它都是有构造函数的
一个类，可以有多个构造函数,建议一个类只有一个构造函数
构造函数
1.初始化属性
'''
# class Person1():
# 	def __init__(self,name,age):
# 		'''初始化属性'''
# 		self.name=name
# 		self.age=age
#
# 	def __init__(self,addresss):
# 		self.address=addresss
#
# per=Person1('s')
# # print(per)

'''析构函数：
有三种方法时的执行顺序：
对象实例化-->构造函数-->对象调用方法-->代码跳转到具体的方法
-->执行方法的代码块-->最后执行析构函数
'''
class Person(object):
	def __init__(self):
		print('我是构造函数')

	def __del__(self):   #相当于异常中的finally，最后始终要被执行
		print('我是析构函数')

	def info(self):
		print('我是方法')

per=Person()
per.info()
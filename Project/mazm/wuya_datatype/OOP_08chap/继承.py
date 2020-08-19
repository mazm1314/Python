#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/5/22   18:02
# @Author　 : mazm
# @ File　　  :继承.py
# @Software  :PyCharm
'''
继承：重用已经存在的数据和行为，减少代码的重复编写
子类继承父类所有的实例变量和方法
'''

'''类属性的继承'''
# class Person(object):
# 	china='地球'
#
# class UsaPerson(Person):
# 	pass
#
# per=UsaPerson()
# per.china

'''实例属性的继承和继承的两种写法'''

# class Fruit(object):
# 	def __init__(self,name):
# 		self.name=name
#
# class Apple(Fruit):
# 	def __init__(self,name,ping,color):
# 		# super(Apple,self).__init__(name)   #java里面用这个关键字，不经常用
# 		Fruit.__init__(self,name)  #建议用这种
# 		self.ping=ping
# 		self.color=color
# 	def info(self):
# 		print('水果名称是：{0}，品牌为：{1}，颜色为：{2}'.format(self.name,self.ping,self.color))
#
#
# apple=Apple('苹果','红富士','红色')
# apple.info()

'''
方法的继承:
1.子类为什么重写父类的方法:子类有自己的特性
当子类重写了父类的方法后，对子类进行实例化后，子类调用的方法（父类，子类都存在），执行的方法是子类的方法


单个类继承的原则：
1.从上到下：子类继承了父类，但是子类没有重写父类的方法，那么子类实例化后，调用的方法是直接调用父类当中的方法
2.从下到上的原则:子类继承了父类，但是子类重写父类的方法，那么子类实例化后，调用的方法是子类当中的方法(子类优先考虑自己类的方法)

'''
#
# class Fruit(object):
# 	def eat(self,name):
# 		self.name=name
# 		# print('{0}水果可以吃的'.format(self.name))
#
# class Apple(Fruit):
# 	def __init__(self,color):
# 		self.color=color
#
# 	def eat(self): #子类重写父类的方法
# 		print('当颜色为{0}的时候是可以吃的'.format(self.color))
#
# class UsaApple(Apple):
# 	def eat(self):
# 		print('我是美国的苹果')
#
#
# # apple=Apple('红色')
# # apple.eat()
#
# usaapp=UsaApple('颜色')#因为父类有他的构造方法
# usaapp.eat()

'''
多个类的继承，从左到右的原则,如果最左没有子类调用的方法，没有就向右继续查找
'''

# class Person(object):
# 	def eat(self):
# 		print('人要吃饭')
# class Mom(Person):
# 	def eat(self):
# 		print('喜欢吃菜')
#
# class Father(Person):
# 	pass
# 	# def eat(self):
# 	# 	print('喜欢吃水果')
#
# class Son(Father,Mom): #多个类的继承，从左到右的原则
# 		pass
#
# # class Son(Person, Mom):  # 不能这样写，以为person是mom的父类，错乱了
# # 	pass
#
# son=Son()
# son.eat()


class A(object):
	def show(self):
		print('A')

class B(A):
	pass

class C(A):
	def show(self):
		print('C')

class D(B,C):
	pass

d=D()
d.show()






















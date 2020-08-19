# 自定义函数
# 语法：关键字：def
#     def 函数名(参数列表)：
#     代码块

# def peint_message():
#     #注释
#     print("这是我的第一个函数")
#
# # 调用函数
# peint_message()
'''

# 函数的三个概念：面向对象，面向过程，函数式编程
# 面向对象--class
# 面向过程--def   函数式   有return关键字
# 函数式编程--def   函数式   无return关键字
# return的作用：调用函数的时候，会返回一个结果，这个结果值，拿到之后，做进一步的处理(1:存在一个变量中，2：直接打印输出函数)
'''

# def add():
#     print(2+2)
#
# def add_1():
#     return 3+3
#
# add()
# result=add_1()
# print(add_1())
# print("函数调用return返回为：",result)

'''
# return关键字：
# 返回0个参数，返回none
# 返回1个参数  就是object
# 返回多个参数:会返回一个tuple：元组
# 注意：return【表达式】结束函数，选择性的返回一个值给调用方，不带表达式的return相当于返回none
'''

# 利用for循环，range()函数，编写任意整数序列的求和函数
# def add():
#     count = 0
#     for i in range(1, 192, 2):
#         count += i
#     return count,333
# print("求和结果为：",add())
#
username = input("请输入用户名：\n")
password = input("请输入密码:\n")

def login():
	if username =='mazm' and password =='mazm':
		return 'hjshhdsdsghgds'
	else:
		return '请您登陆系统'

def profile(token):
	if token=='hjshhdsdsghgds':
		print("欢迎来到我的世界")
	else:
		print("请输入正确的账户密码")
profile(login())

# python之函数位置参数,或者叫形式参数  添加参数，参数化
# 如果是位置参数：按顺序赋值，也可以不按顺序赋值，可以指定
# def print_message(a,b):
#     print(a)
#     print(b)
#
# print_message(a="hello",b="python")#实参

# python之函数默认参数：
# 1、带有默认值的参数，必须放在位置参数的后边，否则报：SyntaxError: non-default argument follows default argument

# def greet(name,content="下午好"):#默认参数
#     print(name+content)
# greet(name="mazm")

# python之函数动态参数
# 把这个数据，转成了元组
# *args数据类型是元组，**kwargs数据类型是字典

# def add(*args):
#     print(args)
#     print("参数的类型",type(args))
#     count=0
#     for item in args:
#         count+=item
#     return count
#
# result=add(1,2,3,4,5,6,7,8)
# print(result)

# def f1(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# f1(1,2,{'name':'mazm'},name='hello',age=13,sex='boy')

# ''''''
# 需求
# 1、对请求的参数进行ASCII排序
# 2、排序后，对请求参数进行MD5的加密
# '''''''

# def data(**kwargs):
#     return dict(sorted(kwargs.items(),key=lambda item:item[0]))
# dict1={'name':'mazm','age':'18','sex':'girl'}
# # print(data(**dict1))
# result=data(**dict1)
# print(result)



# 位置参数和动态参数的结合使用,位置参数放在动态参数的前面
# 如果默认值放在动态参数的前面，就不会生效，要放在后面
# def greet(*args,content="早上好"):
#     name=""
#     for item in args:
#         name+=item
#         name+=","
#     print(name,content)
# greet("早上好1","huahau","lili","minmin")

# 关键字参数：**kwargs      ----字典类型
# 位置参数和关键字参数的结合使用，位置参数必须放在关键字参数前
# def mam_info(age=18,**kwargs):
#     print("kwargs",kwargs)
#     print(type(kwargs))
#
# mam_info(name="huahua",class1="3class",course="jsdhj")

'''
# 函数作用于
# 全局作用域：全局变量
# 局部作用域：针对局部
'''

# name='全局作用'
# def f():
# 	global name  #将该变量设置为全部变量
# 	name='局部作用'
# 	print(name)
# f() #先找局部的变量，再找父级变量

# def f():
# 	name='我是父函数的值'
# 	def f1():
# 		name='我是子函数的值'
# 		print(name)
# 	return f1()
# f()

'''
内部函数lambda:左边是形式参数,右边是条件
内部函数map:对同一个函数增加同等迭代的数据
内部函数filter:对一个列表进行过滤
'''

# login=lambda username,password:print('登陆成功') if username=='mazm' and password=='mazm' else print('登陆错误')
# login('mazm','mazm')

# str='hajhsjsdhj'
# print(len(str))
# print(min(str))
# print(max(str))

# list1=[1,4,5,7,3,9,8,3]
# print(list(filter(lambda a:a>1,list1)))

'''
装饰器
1、函数可以当做一个变量
2、函数的参数也可以是函数
3、函数式可以嵌套的
'''

# def f():
# 	print('hello')
#
# def f2(a):
# 	return a
#
# f2(f())



# 类与对象：关键字：class  类里面一般包含，属性以及函数
# 语法：
# class 类名：
#     属性
#     函数

# class BoyFriend:
#     def __init__(self,height,money,name):#初始化函数，在实例化的时候一定要传参数
#         self.height=height
#         self.money=money
#         self.name=name
#     # 属性
#     height=175
#     money=20000
#     name="mazm"
#
#     # 函数
#     def cooking(self):
#         print("打印self:",self)
#         print(self.money,"会做饭") #实例化的函数可以调用类方法
#
#     @classmethod
#     def hiking(cls):
#         print("喜欢户外运动")
#
#     def swimming(self,name):
#         print("{0}喜欢游泳".format(name)+self.height)
#         self.swimming()
#
#     @staticmethod
#     def coding():
#         print("喜欢写代码")

# 怎么来调用类里面的属性和函数，----通过实例、对象
# 创建实例：类名()
# 调用方法：实例.方法
# 调用属性：实例.属性
# bf=BoyFriend()
# bf.coding()
# bf.cooking()
#
# print("打印实例本身",bf)
# print(bf.name)
# print(bf.height)

# 类与对象的self的关键字：self就是实例本身，打印出来就是内存地址
# 类与对象的类函数：函数参数为：cls
#   1：类函数/类方法 @classmethod；加了注释，可以通过类名直接调用（不需要实例化）
#         1-1：什么时候定义为类函数：1、类方法和类属性没有实际的关系；2、有初始化函数的时候
# BoyFriend.hiking()
#   2：实例函数/方法；有self关键字的函数就是实例函数，必须要通过实例调用该函数
#         2-1：也可以先实例化后再调用方法
# BoyFriend().swimming("hhh")
#   3：静态函数/静态方法：@staticmethod
#         3-1：可以不传任何参数,可以通过类.函数调用，也可以通过实例化调用
# BoyFriend.coding()


# 类方法 实例方法 静态方法
# 1、都可以被实例调用
# 2、只有静态方法以及类方法，可以通过类名.函数名()；
# 3、静态方法和类方法，不能调用类属性

# 函数的相互调用
# 类与对象的初始化函数
# bff=BoyFriend(1,2,3)
# print(bff.name)

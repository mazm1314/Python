#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/5/11   19:15
# @Author　 : mazm
# @ File　　  :decorator.py
# @Software  :PyCharm

'''
内部函数的讲解
'''

# 1、abs()，该内置函数的作用是绝对值，不管数字是负数还是正数，结果都是正数
'''
a=-2323.3445
print(a)
print(abs(a))
'''

# 2、bytes()，把字符串转为bytes，见设置一个原始字符串，转为bytes，并且编码是utf-8
'''
b='python语言'
print(type(b))   #<class 'str'>
byte=bytes(b,encoding='utf-8')
print('将str转换为byte：',type(byte))  #<class 'bytes'>
str=str(byte,encoding='utf-8')
print('将byte转换为str：',type(str))  #<class 'str'>
'''

# 3、chr()把数字转换为字母,---表示ascii码对应的字符他的输入时数字，可以用十进制，也可以用十六进制。
# 4、ord()把字母转换为数字-返回对应字符的ascii码（只能是a-z,A-Z）
'''
print(chr(65))
print(ord('A'))
'''

# 5、eval()字符串转换成表达式并获取结果
# 6、compile()是把字符串编译成python代码，再由函数eval()，exec()执行
# 7、dir()可以快速的查看对象提供了那些方法，如查看列表的方法
# 8、help()顾名思义查看帮助，如查看列表的备帮助
'''
e=[1,2,3,4]
print(help(e))
'''
# 9、divmod()是整除求余，如97除以10,整除是9，余数是7
# 10、isinstance()判断对象是否是某个类的实例
# 11、filter()函数是过滤，如从列表中过滤出xx来
'''
list1=[1,2,3,4,5,6,7,8,9,0]
def f():
	li=[]
	for item in list1:
		if item>2:
			li.append(item)
	print(li)
f()
'''
# 使用函数简化一下
'''
list1=[1,2,3,4,5,6,7,8,9,0]

def f1(a):
	if a>2:
		return True
res=filter(f1,list1)
print(list(res))
'''
# 结合匿名函数lambda函数后，实现的过程更加简单
'''
list1=[1,2,3,4,5,6,7,8,9,0]
res=filter(lambda a:a>2,list1)
print(list(res))
'''

# 12、map()函数可以实现迭代的增加，如有列表[0,1,2,3,4,5,6,7,8,9]，都加10
'''
map1=[1,2,3,4,5,6,7,8,9,0]
def f2(a):
	return a+100
result=map(f2,map1)
print(list(result))
'''
# 结合lambda函数，实现的代码更加精简
map1=[1,2,3,4,5,6,7,8,9,0]
result=map(lambda a:a+100,map1)
print(type(result))
print(list(result))

# 13、globals()代表所有的全局变量,locbals()代表所有的局部变量

# 14、max()获取最大值，min()获取最小值，sum()获取和
'''
s=[1,2,3,5,6,7,4,3]
print(max(s))
print(min(s))
print(sum(s))
'''

# 15、type()查看类型

#author mazm

# str->list

str='9.3'
str_list=str.split('.')  #str->list
print(str_list)
list_str='.'.join(str_list) #list->str
print(list_str)
print(type(list_str))

# dict->list

dict1={'name':'mazm','age':18}
dict_list=list(dict1.keys()) # dict->list
print(dict_list)
list_dict=dict(enumerate(dict_list))  #list->dict
print(list_dict)


# number 之间的相互转换

# int <=> float
var1 = 1;
print(type(var1)) #<class 'int'>

res1 = float(var1)
print(res1) #1.0
print(type(res1)) #<class 'float'>

res2 = int(res1)
print(res2) #1
print(type(res2)) #<class 'int'>

# int or float <=> String
var = 1
res = str(var)
print(type(res)) #<class 'str'>

res = float(res)
print(type(res)) #<class 'float'>

# math 使用
import math
var = math.pi
print(var) #3.141592653589793...


res = math.radians(180)# 将角度值转换乘弧度值3.141592653589793 即180度 对应 math.pi
print(res) #3.141592653589793...

res = math.degrees(math.pi) #将弧度转换成角度
print(res) #180.0

res = math.pow(1,2) # 等价于x 的 y 次方
print(res) # 1.0
print(type(res)) # <class 'float'>

res = math.ceil(2.3) # ceil 天花板取值，往上取
print(res)  #3

res = math.floor(2.3) # floor 往下取值
print(res) #2


# 字符串 => 字典  也可以使用json

var = "{'a':20,'b':40}"
print(type(var)) #<class 'str'>
res = eval(var)
print(res) #{'a': 20, 'b': 40}
print(type(res)) #<class 'dict'>

# 字典=> 字典字符串 也可以使用json
var = {'a':20,'b':40}
res = str(var)
print(type(res)) #<class 'str'>
print(res) #{'a': 20, 'b': 40}

#字符串 => 列表  指定分割符号就行

#列表 => 字符串
var = [ 'a','b','c','d'] #要求列表里面都是str类型
res = '-'.join(var)
print(res) #a-b-c-d
print(type(res)) #<class 'str'>

# 列表 => 字典
lst1 = ['k1','k2','k3']
lst2 = [1,2]
rest = zip(lst1,lst2) # 拉锁函数
print(res)#<zip object at 0x0000020C194B76C8>
print(type(rest)) #<class 'zip'>
res = dict(rest)
print(res)  #{'k2': 2, 'k1': 1}
print(type(res)) #<class 'dict'>
#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/5/19   18:51
# @Author　 : mazm
# @ File　　  :file.py
# @Software  :PyCharm
'''
对文件的操作
open()函数的参数
1、要操作的文件名称
2、以什么样的方式操作文件：
r:只读模式
w:只写模式【不可读，不存在就创建，存在就清空内容】
x:只写模式【不可读，不存在就创建，存在就报错】
a:增加模式【可读，不存在就创建，存在只增加内容】
"+"表示可以同时读写某个文件，具体为：
r+：读写
w+：写读
x+：写读
a+：写读
3、
'''
import json
'''
只写的模式操作文件
二次操作可以覆盖之前的内容
'''
# r=open('file.json','w',encoding="utf-8")
# temp={
# 	'name':'mazm',
# 	'age':18,
# 	'sex':'girl'
# }
# # r.writelines(temp)
#
# temp_str=json.dumps(temp)  #序列化一下
# r.write(temp_str)
# # r.writelines(temp_str)
# r.close()

'''只读模式来操作文件'''
# f=open('file.json','r',encoding="utf-8")
# read=f.read()  #文件中的内容全部读取出来. 弊端: 占内存. 如果文件过大.容易导致内存崩溃
# read1=f.read(10)  #--->只读取文件中的某些字符，
# read1=f.readline()#一次读取一行数据, 注意: readline()结尾, 注意每次读取出来的数据都会有一
# 个\n 所以呢. 需要我们使用strip()方法来去掉\n或者空格
# read1=f.readlines()#将每一行形成一个元素, 放到一个列表中. 将所有的内容都读取出来. 所以
# 也是. 容易出现内存崩溃的问题.不推荐使用

# f.close()
# print(read1)

'''文件追加，不覆盖之前的内容'''
# f1=open('file.json','a',encoding="utf-8")
# f1.write('追加内容1')
# f1.close()

'''以字节的模式读取文件'''
# f2=open('file.json','rb'，encoding="utf-8")
# read2=f2.read()
# f2.close()
# print(read2)
'''
推荐使用循环读取
:. 这种方式是组好的. 每次读取一行内容.不会产生内存溢出的问题.
'''
# f=open('../testFile/file2.txt','r',encoding='utf-8')
# for i in f:
# 	f.close()
# 	print(i)

'''
1. seek(n) 光标移动到n位置, 注意, 移动的单位是byte. 所以如果是UTF-8的中文部分要
是3的倍数.
通常我们使用seek都是移动到开头或者结尾.
移动到开头: seek(0)
移动到结尾: seek(0,2) seek的第二个参数表示的是从哪个位置进行偏移, 默认是0, 表
示开头, 1表示当前位置, 2表示结尾
'''
f = open("../testFile/file2.txt", "r+", encoding="utf-8")
f.seek(0) # 光标移动到开头
content = f.read() # 读取内容, 此时光标移动到结尾
print(content)
f.seek(0) # 再次将光标移动到开头
f.seek(0, 2) # 将光标移动到结尾
content2 = f.read() # 读取内容. 什么都没有
print(content2)
f.seek(0) # 移动到开头
f.write("张国荣") # 写入信息. 此时光标在9 中文3 * 3个 = 9
f.flush()
f.close()

'''
文件上下文关系的处理
推荐使用相对路径
'''

# with open('../testFile/file2.txt', 'w', encoding="utf-8") as f:
# 	f.write('wuya')
	# f.close()  #这里不需要写这个，上下文会自动关闭，上下文处理只关注对文件的操作上面，优点：会解决由于没有关闭导致出现的问题

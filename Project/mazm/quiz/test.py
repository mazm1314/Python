#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/6/30   16:22
# @Author　 : mazm
# @ File　　  :test.py
# @Software  :PyCharm
'''
# 统计在一个队列中的数字，有多少个正数，多少个负数，如[1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
list1=[1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
list2=0
lis3=0
for items in list1:
	if items >0:
		list2+=1
	elif items<0:
		lis3+=1

print('大于0的个数',list2)
print('大于0的个数',lis3)
'''

'''
# 字符串 “axbyczdj”，如果得到结果“abcd”

str='axbyczdj'
print(str[::2])
'''

'''
# 已知一个字符串为“hello_world_yoyo”, 如何得到一个队列 [“hello”,”world”,”yoyo”]

str='hello_world_yoyo'
list1=str.split('_')
print(list1)

'''

'''
# 已知一个数字为1，如何输出“0001”
a=1
print('%04d'%a)
'''

'''
# 已知一个队列,如： [1, 3, 5, 7], 如何把第一个数字，放到第三个位置，得到：[3, 5, 1, 7]

a=[1, 3, 5, 7]
a.insert(3,a[0])
print(a[1:])
'''

'''
# 已知 a = 9, b = 8,如何交换a和b的值，得到a的值为8,b的值为9

a=9
b=8
# a, b = b, a# 第一种方法
c=a
a=b
b=c
print(a)
print(b)
'''

# 打印出100-999所有的”水仙花数”，所谓”水仙花数”是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个”水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。


# 已知一个队列[1, 3, 6, 9, 7, 3, 4, 6]
# 按从小到大排序
# 按从大到小排序
# 去除重复数字
a=[1, 3, 6, 9, 7, 3, 4, 6]
a.sort()
print(a)

a.sort(reverse=True)
print(a)

b = list(set(a))
print(b)



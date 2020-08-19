#if循环语句
# a=-8
# if a>=10:
#     print("我是大于10的数字哦")
# elif a<0:
#     print("我是负数哦")
# else:
#     print("我是其他")


#while循环语句
# 空数据，空元组，空列表，空字典，空字符串都是false，
# 非空的都是true
# 利用break和continue结束死循环

# b=7
# while b>0:
#     print("{0}.是大于0的数字".format(b))
#     b-=1
# 利用while做到1-100的整数相加？
# a=0
# sum=0
# while a<=100:
#     sum=sum + a
#     a+=1
#     print(a)
#
# print("1-100相加等于{0}".format(sum))


# for循环可以遍历任何序列的项目，eg元组，字符串、列表、字典、或者其他指定的数据范围，
# 通过遍历的对象控制循环的次数，遍历完毕就循环完毕
# for循环的次数跟in后的元素个数有关
# for item in itrable :
#     do something
#  item:元素
#  itrable:集合

# string='mazm'
# tuple=(1,2,"3")
# list=[(1,2),3,"mazm1"]
# dict={"mazm3":"1",'sdj':"2",('sjdj',1,1):3}
# # 打印出字典的值
# for item in dict.values() :
#     print("我是谁:",item)

# range函数：(m,n,k) m开始，n结尾，k步长，，取头不取尾     只传一个值，开头默认是0，步长默认是1
# range函数作用，生成一个整数序列
# 做到1-100的整数相加
# sum=0
# for n in range(0,101):
#     sum+=n
#     n+=1
#     print(n)
# print(sum)
#
str=range(2,10,2)
print(list(str))

# 倒叙输出
s=[1,7,5,4,9,3,5]
for i in range(6,-1,-1):  # 6 是下表
    print(s[i])
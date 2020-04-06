#数据类型：元组，列表
# Python常见的数据类型：数字、字符串、元组、列表、字典

# 1:元组的标志();关键字：tuple
# 2:元组只有一个数据的时候，在数据后边加一个,
# 3:元组里面的数据，可以是任何类型
# 4:元组取值，是根据索引取值，也分为正序和反序
# 5:元组切片：同字符串
# 6:元组的值，一旦确定，就无法更改！删除修改都不行
# 7:判断元素  in   not in
tuple_1=(1,)
tuple_2=(1,0.02,"mazm",'mazm11',(12,1,1))
print(tuple_2[2])#正序
print(tuple_2[-3])#反序
str=tuple_2[0:5:2]  #切片
print(str)
print(type(tuple_2))

print(0.02 in tuple_2)  #判断元素

# 列表：在python里面使用率最高；
# 1：标志 []  关键字 list
# 2：a=[] 空列表
# 3：里面的数据元素可以是任何类型
# 4:取值：根据索引取值，列表名[索引值]--正序、反序
# 5:列表的切片：同字符串 列表名[m:n:k]
# 6:判断元素  in   not in 成员运算符

a=[]
print(a)
print(type(a))
a=[1,2.12,"lemo",'eewe',(1,2,3),[3,4,5]]
print(a[4])
# 如何取列表中某个列表的值
print(a[-1][-1])

# 列表：内建函数

# 新增操作：
# 1）列表名.append()，加元素到列表的最后面,缺点：每次只能添加一个元素
# 2）列表名.insert(),加元素到指定位置
# 3）列表名.extend(),列表末尾一次性追加另一个序列中的多个值。
a.append("殖民")
a.append((2,1,1))
print(a)

a.insert(0,"first")
a.insert(-1,"end")#在原数组最后加
print(a)

list1=[1,2,3]
list2=["a","b","c"]
list1.extend(list2)
print("在list1后面拼接list2",list1)

# 修改列表：重新赋值
a[0]="修改第一位数字"
print(a)

b=[1,2.12,"lemo",'eewe',(1,2,3),[3,4,5]]
# 删除元素
# 1):列表名.pop():删除列表的最后一个元素
b.pop()
b.pop()
print(b)
# 2):列表名.pop(index):删除列表中指定的元素
b.pop(0)
print(b)

# 其他操作
c=[2,3,4,1,8,5,3,2,9,5]
# c.sort() #排序
# c.reverse()  #顺序倒置
# c.clear()   #清空元素
print(c)
d=c.copy()
print(d)
#数据类型：元组
# Python常见的数据类型：数字、字符串、元组、列表、字典

# 1:元组的标志();关键字：tuple
# 2:元组只有一个数据的时候，在数据后边加一个,
# 3:元组里面的数据，可以是任何类型
# 4:元组取值，是根据索引取值，也分为正序和反序
# 5:元组切片：同字符串
# 6:元组的值，一旦确定，就无法更改！删除修改都不行
# 7:判断元素  in   not in
tuple_1=(1,)
tuple_2=(1,[1,2],0.02,"mazm",'mazm11',(12,1,1))
print(dir(tuple_2))
tuple_2[1][0]=13 #修改元组中列表的值
print(tuple_2)
# 元组取值
print(tuple_2[2])#正序
print(tuple_2[-3])#反序
str=tuple_2[0:5:2]  #切片
print(str)
print(type(tuple_2))

print(0.02 in tuple_2)  #判断元素


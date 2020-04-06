# 1:标志：{}   关键字 dict
# # 2:a={} 空字典
# 3：字典的数据存储的格式是key:value  键值对
# 4:字典里面的value可以是任何类型的数据
# 5：取值方式，根据key取值，字典名[key]
# 6:新增：字典名[new_key]  new_key在当前字典不存在
# 7：修改：字典名[old_key]=value  old_key在当前字典存在
# 8:删除：pop(old_key)

a={'name':'mazm','age':'18','english':'88'}
print(type(a))
print(a)

print(a['name'])   #取值

a['sex']='girl'  #新增
print(a)
a['english']=99   #修改
print(a)

a.pop('age')
print(a)
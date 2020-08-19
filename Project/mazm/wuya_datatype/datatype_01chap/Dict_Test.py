#数据类型：字典
# 1:标志：{}   关键字 dict
# # 2:a={} 空字典
# 3：字典的数据存储的格式是key:value  键值对
# 4:字典里面的value可以是任何类型的数据
# 5：取值方式，根据key取值，字典名[key]
# 6:新增：字典名[new_key]  new_key在当前字典不存在
# 7：修改：字典名[old_key]=value  old_key在当前字典存在
# 8:删除：pop(old_key)

a={'name':'mazm','age':'18','english':'88'}
print(dir(a))
print(type(a))
print(a)

print(a['name'])   #取值

a['sex']='girl'  #新增
print(a)
a['english']=99   #修改
print(a)

a.pop('age')
print(a)

# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

dict_01={"name":"mazm","age":"25","yuwen":"78","shuxue":"89","english":"99"}
dict_02={"name":"mazm1","age":"25","yuwen":"88","shuxue":"87","english":"100"}
# 字典排序：根据key的值得ASCII的值得大小进行排序
print(sorted(dict_02.items(),key=lambda item:item[0]))
# dir1=dict_01.clear()

# dict_03=dict_02.copy()
# dict_03=dict.fromkeys(dict_02)
# dict_03=dict_02.get("age1","hahah")
# dict_03=dict_02.items()
# dict_03=dict_02.keys()
# dict_03=dict_02.setdefault("hh","moren")
# dict_03=str(dict_01)
# dict_03=len(dict_02)

# dict_01.update(dict_02)  #更新01的值为02的值
# print(dict_01)

# dict_03=type(dict_02)  #查看类型
# print(dict_03)


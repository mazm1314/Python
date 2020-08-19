#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/5/17   16:24
# @Author　 : mazm
# @ File　　  :Serialization_data.py
# @Software  :PyCharm

import json
import requests

'''
json库
go python,php 之间通过api进行交互，api中以json字符串交换

序列化：把python的数据类型（字典）转换为str的数据类型     json.dumps()
反序列化：把str的类型转换为python的数据类型（字典）   json.loads()
3、总的来说，不管字典、列表、元组都是和str进行转换，之间的相互转化就是序列化和反序列化

dumps对象序列化为bytes对象
loads从bytes对象反序列化。

'''
url='http://wx-new.kt.ziroom.com/hd/join/join-detail'
request1={"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiJkOWQyNzRlOC03MGZhLWYyOTUtYTVhMS1kODI1Njg0MmZlOGMiLCJ0eXBlIjo1LCJsZW5ndGgiOjEwMDgwLCJ0b2tlbiI6ImUwZDg4ZDFmLWE3OTctNDg3Yi05OTA5LTNmOTE0MWU1YjMwMSIsImNyZWF0ZVRpbWUiOjE1ODk3MDE5MzAxODl9._deEz7czC6IHz6CvERKBFaD5YOGIf7dv3tW1u5VK4b4",
"activity_code": "hy2019","ver": "2020"}

reponse1={"status":"success","error_code":0,"error_message":"","data":{"join_id":"4pwd34","status":"10","phone":"138****5304","help_number":"4","need_number":"4","reward_time":"2020-04-26 14:37:43","secret":"","avatar":"https://10.16.34.48/group1/M00/15/E5/ChAiMF1TbdWAXcsgAABSbIQnt8o464.jpg","cert_status":"20","university":"把电话回电话","name":"唐小妹","failure_reason":"","from_type":6,"check_type":2,"can_promoter":1,"is_year":"2020","is_promoter":1,"alumnus":1}}
# post1=requests.post(url,request1)
# print(post1.text)
# print(type(post1.text))

dict1={'admin':'adimin','pass':'admin'}
# 字典的序列化--str是双引号
dict_str=json.dumps(dict1)
print('字典序列化后的信息结果',dict_str,type(dict_str))
# 字典的反序列化--dict是单引号
str_dict=json.loads(dict_str)
print('字典反序列化后的信息结果',str_dict,type(str_dict))

'''
列表的序列化：把python的数据类型（列表）转换为str的数据类型
列表的反序列化：把str的类型转换为python的数据类型（列表）
'''

import json
list1=['admin','mazm','boke']

list_str=json.dumps(list1)
print('列表序列化后的信息结果',list_str,type(list_str))
str_list=json.loads(list_str)
print('列表反序列化后的信息结果',str_list,type(str_list))




'''
列表的序列化：把python的数据类型（元组）转换为str的数据类型
列表的反序列化：把str的类型转换为python的数据类型（列表）---这里转换为了列表
'''

import json
tuple1=(1,2,3)

tuple_str=json.dumps(tuple1)
print('元组序列化后的信息结果',tuple_str,type(tuple_str))
str_tuple=json.loads(tuple_str)
print('元组反序列化后的信息结果',str_tuple,type(str_tuple))
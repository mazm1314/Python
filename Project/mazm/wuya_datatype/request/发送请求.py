#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/6/5   16:03
# @Author　 : mazm
# @ File　　  :发送请求.py
# @Software  :PyCharm
'''
request
aiohttp  一步请求
'''

import requests
import json

# url='https://yx1.ziroom.com/promotion/channel/get-ds-info'
# data={'token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiI5Y2ZjZTUxZi0zZWRkLTQ1ODMtYTc5NC1mYTliYjRhYWIxYTIiLCJ0eXBlIjo1LCJsZW5ndGgiOjEwMDgwLCJ0b2tlbiI6IjhmZTI2ZWFkLTQ3NDgtNGU5OS1hMGU4LTM5ZDZjZDUwNGJjMSIsImNyZWF0ZVRpbWUiOjE1OTEzNDQ2NTYyMTl9.gXSRs3EUD8Iy8d53fmoYsvXiO3ZK71n_Lemylx7CeKU'}
# #   有些后台严格限制了请求头必须要带，不带的话会导致400
# headers={'Connection':'keep-alive','Accept':'application/json, text/plain, */*'}
# school=requests.post(url,data=data,headers=headers)
# print('基本文本的数据:\n',school.text)
# print('请求的链接:\n',school.url)
# print('状态码:',school.status_code)
# print(':\n',school.raw)
# print('二进制的内容:\n',school.content)
# print('cookies:',school.cookies)
# print('字符编码:',school.encoding)
# print('请求头:\n',school.headers)
# print('json形式:\n',school.json())

'''
request的Parmas的参数详情
'''

# url='http://paladin.t.ziroom.com/api/rentunit/detail'
# parms={'invHouseCode':'60321290'}
# r=requests.get(
# 	url=url,
# 	params=parms)
# print(r.url)
# # print(r.json())
# # print(r.content.decode('utf-8'))  #解决返回乱码的问题
# print(json.dumps(r.json(),indent=True,ensure_ascii=False))

'''
request的json的参数详情
json和data 的区别：
	application/x-www-form-urlencoded    使用data的形式
	application/json   json格式的字符串数据类型-->字符串
	
'''
'''
data:
只能使用data，不能使用json
'''
data={'mobileCode':'13487659846','userID':''}
headers={'Content-Type':'application/x-www-form-urlencoded'}
r=requests.post(
	url='http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx/getMobileCodeInfo',
	data=data,
	headers=headers)
print(r.text)

'''
json:
1、满足的要求：application/json-->json格式的字符串数据类型
2、请求参数必须是字典
但是2必须在1的条件下才可以
'''



'''
复杂的请求参数处理：请求数据：data套data
url:www.wuya.com
data={'name':'wuya','age':18,'data':[{''}]}
'''
datas={'name':'wuya','age':18,'data':[{'address':'xian'}]}

data1={'name':'wuya','age':18,'data':'books'}
headers={'content-type':'application'}
#--->json格式的字符串-->str

datas['data']=json.dumps(datas['data'])
r=requests.post(url='',json=datas,headers=headers)












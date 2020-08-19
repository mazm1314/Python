#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/6/8   19:13
# @Author　 : mazm
# @ File　　  :session会话对象.py
# @Software  :PyCharm
'''
一、session会话对象介绍：
　　会话对象让你能够跨请求保持某些参数，它也会在同一个session实例发出的所有请求之间保持cookie。
二、步骤

1.对session对象进行一次实例化
2.进行登陆操作，返回一个session对象
3.返回的对象去发送get或者post等方法的请求（这样的话，省去了cookie的处理，不需要再读取cookie了）

'''


import  requests



def login(url='https://www.680.com/inc_vk/login.asp'):
	s=requests.Session()  # 1.对session对象进行一次实例化
	params={'yz':0,'yzm':"","uid":"13484545195","pwd":"asd888",
	        "lgs":0,"callback":"jsonp1580910280481","rnd":"0.2264766513954488"}
	headers={
		'content-type':"application/x-www-form-urlencoded",
		'user-agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
		"Referer":"https://www.680.com/login.html"
	}
	r=s.get(url=url,params=params,headers=headers)
	return s  #2.进行登陆操作，返回一个session对象

def profile():
	r=login().get(   #3.返回的对象去发送get或者post等方法的请求（这样的话，省去了cookie的处理，不需要再读取cookie了）
		url='https://user.680.com/financelist.aspx')
	print(r.text)

profile()
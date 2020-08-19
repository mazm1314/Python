#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/6/5   20:31
# @Author　 : mazm
# @ File　　  :session的处理思路.py
# @Software  :PyCharm
import requests
'''
1、发送登录请求
2、登录成功后，把sessionID的信息返回给客户端
3、客户端再次发送请求，需要在请求头里面(cookie)带上返回的sessionID
'''
def login(url='https://www.680.com/inc_vk/login.asp'):
	params={'yz':0,'yzm':"","uid":"13484545195","pwd":"asd888",
	        "lgs":0,"callback":"jsonp1580910280481","rnd":"0.2264766513954488"}
	headers={
		'content-type':"application/x-www-form-urlencoded",
		'user-agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
		"Referer":"https://www.680.com/login.html"
	}
	r=requests.post(url=url,params=params,headers=headers)
	return r.cookies


def profile():
	r=requests.get(
		url='https://user.680.com/financelist.aspx',cookies=login())
	print(r.text)

profile()



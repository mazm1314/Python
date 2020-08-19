#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/6/10   20:33
# @Author　 : mazm
# @ File　　  :文件上传.py
# @Software  :PyCharm

import  requests


def login():
	# 获取验证码
	login_url = "https://tpassport.ziroom.com/login/v2"
	login_data = {'phone': '18810911959', 'password': 'a53c9868827ee7df457110549547fbb0'}
	# 以下的headers一个值都不能缺少
	login_heders = {
		'Accept': 'application/json',
		'Client-Version': '6.5.10',
		'Sys': 'app',
		'Request-Id': '1327D8F2:1587296579'
	}
	login_rep = requests.post(login_url, data=login_data, headers=login_heders)
	return login_rep.json()['resp']['token']

def profile():
	pro_url='http://wx-new.kt.ziroom.com/hd/user/cert-upload'
	pro_data={'activity_code':'hy2019','token':login()}
	pro_headers={'Content-Type':'multipart/form-data'}
	file={'file':('1.jpg',open('D:/1.jpg',''rb'))}
	r=requests.post(url=pro_url,data=pro_data,headers=pro_headers,files=file)
	print(r.text)

profile()




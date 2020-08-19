#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/5/17   15:43
# @Author　 : mazm
# @ File　　  :Serialization_file.py
# @Software  :PyCharm

import  json

'''
1、模拟登陆
2、模拟登陆成功显示登录成功后的用户账号
3、模拟注册
'''

def typeUsername():
	username=input('请输入账号：\n')
	return username

def typePassword():
	password=input('请输入账号密码：\n')
	return password

def regetist(username,password):
	'''
	实现注册的功能
	:parameter username:注册系统的账号
	:parameter password:注册系统的密码
	'''
	temp=username+'|'+password
	json.dump(temp,open('login.json','w'))

def login(username,password):
	'''
	登录
	:parameter username:登录系统的账号
	:parameter password:登录系统的账号密码
	'''
	f=str(json.load(open('login.json','r')))
	list1= f.split('|')
	if list1[0] == username and list1[1] == password:
		return True
	else:
		return False

def info(username,password):
	'''
	系统登陆后的用户信息页面
	:parameter username:登录系统的账号
	:parameter password:登录系统的账号密码
	'''
	f = str(json.load(open('login.json', 'r')))
	list1=f.split('|')
	r=login(username,password)
	if r:
		print('恭喜{0}进入到系统'.format(list1[0]))

	else:
		print('Sorry，很遗憾，登录失败，请检查您的账号是否正确？')

def exit():
	'''退出系统'''
	import  sys
	sys.exit(1)

def main():
	'''主函数'''
	while True:
		try:
			t=int(input('1、注册 2、登录 3、退出系统\n'))
			# #如果是float类型的处理
			# if isinstance(t,float):
			# 	t=int(t)
			# #字符串类型的处理
			# elif isinstance(t,str):
			# 	#判断字符串是否大于1位，如果是，取出第一位，并且把字母转为数字
			# 	if len(t)==1:
			# 		t=ord(t)
			# 	else:
			# 		t=int(ord(list(t)[0]))
		except  Exception as e:
			print(e.args)
		else:
			if t==1:
				username =typeUsername()
				password =typePassword()
				regetist(username,password)
			elif t==2:
				username = typeUsername()
				password =typePassword()
				login(username,password)
				info(username, password)
			elif t==3:
				exit()
			else:
				print('输入错误，请继续输入，请输入1，或者2，或者3')
		finally:pass

if __name__ == '__main__':
    main()

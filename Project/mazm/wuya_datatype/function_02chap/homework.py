#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/5/12   18:15
# @Author　 : mazm
# @ File　　  :homework.py
# @Software  :PyCharm

'''
以装饰器来实现用户登录的部分，在一个后台登录中，不管用户想做什么，前提是都必须得登录才可以的
假设后台后台分别有订单模块，先看不使用装饰器来实现这个过程
'''
import sys
'''
LOGIN_USER = {"is_login": False}

def admin():
	# 后台管理系统
	if LOGIN_USER['is_login']:
		print('欢迎%s访问无涯后台管理系统' % LOGIN_USER['current_user'])
	else:
		print('请先登录系统，谢谢！')


def login(username, password):
	if username == 'admin' and password == 'admin':
		LOGIN_USER['is_login'] = True
		LOGIN_USER['current_user'] = username
		admin()
	else:
		print('用户名或者密码错误')


def order():
	if LOGIN_USER['is_login']:
		print('欢迎%s访问无涯后台管理系统' % LOGIN_USER['current_user'])
	else:
		print('请先登录系统，谢谢！')

def main():
	while True:
		f=input('1、后台管理系统 2、查看订单 3、登录 4、退出系统\n')
		if f=='1':
			admin()
		elif f=='2':
			order()
		elif f=='3':
			username = input('请输入用户名:\n')
			password = input('请输入密码:\n')
			login(username, password)
		elif f == '4':
			sys.exit(1)
main()

'''

# 使用装饰器
import sys

LOGIN_USER = {"is_login": False}


def wuya(func):
	def inner():
		if LOGIN_USER['is_login']:
			r = func()
			return r
		else:
			print('请先登录系统，谢谢！')

	return inner


def f1():
	print('欢迎%s访问无涯后台管理系统' % LOGIN_USER['current_user'])


@wuya
def admin():
	'''后台管理系统'''
	f1()


def login(username, password):
	if username == 'admin' and password == 'admin':
		LOGIN_USER['is_login'] = True
		LOGIN_USER['current_user'] = username
		admin()
	else:
		print('用户名或者密码错误')


@wuya
def order():
	f1()


def main():
	while True:
		f = input('1、后台管理系统 2、查看订单 3、登录 4、退出系统\n')
		if f == '1':
			admin()
		elif f == '2':
			order()
		elif f == '3':
			username = input('请输入用户名:\n')
			password = input('请输入密码:\n')
			login(username, password)
		elif f == '4':
			sys.exit(1)


main()


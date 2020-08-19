#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/5/23   22:19
# @Author　 : mazm
# @ File　　  :login.py
# @Software  :PyCharm

import json
import sys

class login(object):
	def __init__(self,username,passwd):
		self.username=username
		self.passwd=passwd

	def getUsername(self):
		return self.username

	def setUsername(self,username):
		self.username=username

	def getPasswd(self):
		return self.passwd

	def setPasswd(self,passwd):
		self.passwd=passwd

	def register(self):
		'''注册功能的实现'''
		temp = self.username + '|' + self.passwd
		json.dump(temp, open('login', 'w'))
		print('账号已注册成功,请开始登录')

	def login(self):
		f=str(json.load(open('login','r')))
		list1=f.split("|")
		if list1[0]==self.username and list1[1]==self.passwd :
			return True
		else:
			return False

	def userInfo(self):
		f = str(json.load(open('login', 'r')))
		list1 = f.split('|')
		r = self.login()
		if r:
			print('恭喜{0}进入到系统'.format(list1[0]))

		else:
			print('Sorry，很遗憾，登录失败，请检查您的账号是否正确？')

	def exit(self):
		sys.exit(1)


login=login('mazm','mazm')
# login.register()
# login.login()

def main():
	'''主函数'''
	while True:
		try:
			t = int(input('1、注册 2、登录 3、退出系统\n'))
		except  Exception as e:
			print(e.args)
		else:
			if t == 1:
				login.register()
			elif t == 2:
				login.userInfo()
			elif t == 3:
				login.exit()
			else:
				print('输入错误，请继续输入，请输入1，或者2，或者3')
		finally:
			pass

if __name__ == '__main__':
    main()
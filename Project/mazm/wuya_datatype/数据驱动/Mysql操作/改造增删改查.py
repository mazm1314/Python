#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/6/17   20:42
# @Author　 : mazm
# @ File　　  :改造增删改查.py
# @Software  :PyCharm
import pymysql

class  Mysqlconn():
	def coon(self):
		con=pymysql.connect(
		host='127.0.0.1',
		# port='3306',
		username='root',
		password='root',
		db='test'
		)
		return con
	def getont(self,sql,params):
		cur=self.coon().cursor()
		data=cur.execute(sql,params)
		res=cur.fetchone()
		return res

def checkindentity(username,password):
	opra=Mysqlconn()
	sql = 'select * from user where username=%s and password=%s'
	params = (username,password)
	return opra.getont(sql=sql,params=params)


def info():
	username=input('请输入用户名:')
	password=input('请输入密码：')
	check=checkindentity(username,password)
	if check:
		print('登录成功,昵称:{0}'.format(username))
	else:print('登录失败')

if __name__=='__main__':
	info()





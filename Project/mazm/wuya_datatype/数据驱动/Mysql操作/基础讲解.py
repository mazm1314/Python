#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/6/16   18:46
# @Author　 : mazm
# @ File　　  :基础讲解.py
# @Software  :PyCharm

'''
安装
pymysql,
clientmysql----用来对数据库进行增删改查，，
https://pypi.org/project/mysqlclient/#files--官方下载再安装
然后到路径下面安装：python setup.py install
'''

import pymysql
#查询
'''
def connectMysql():
	try:
		conn=pymysql.connect(
			host='127.0.0.1',
			user='root',
			passwd='root',
			db='test'
		)
	except Exception as e:
		return e.args
	else:
		cur=conn.cursor()
		# 单个查询
		# sql="select * from user where id=%s"
		# params=(2)
		# cur.execute(sql,params)
		# # sql = "select * from user"
		# # cur.execute(sql)
		# data=cur.fetchone()
		# print(data)
		
		#批量查询
		sql='select * from user'
		cur.execute(sql)
		data=cur.fetchall()
		# 输出方式1
		for item in data:
			print(item)
		# 输出方式2--列表推导式
		db=[item for item in data]
		print(db)
	finally:
		cur.close()
		conn.close()

print(connectMysql())
'''


# insert
'''
def insertMysql():
	try:
		conn=pymysql.connect(
			host='127.0.0.1',
			user='root',
			passwd='root',
			db='test'
		)
	except Exception as e:
		return e.args
	else:
		cur=conn.cursor()
		sql='insert into user values (%s,%s,%s,%s,%s)'
		# 单个插入
		# params=(3,'33','girl','90','34')
		# cur.execute(sql,params)
		params=[
			(4, '33', '87', 'boy', '34'),
			(5, '33', '78', 'boy', '34')
		]
		cur.executemany(sql,params)
		conn.commit()
	finally:
		cur.close()
		conn.close()

insertMysql()
'''

# 删除
def deleteMysql():
	try:
		conn=pymysql.connect(
			host='127.0.0.1',
			user='root',
			passwd='root',
			db='test'
		)
	except Exception as e:
		return e.args
	else:
		cur=conn.cursor()
		sql='delete from user where id=%s'
		params=(3,)
		cur.execute(sql,params)
		conn.commit()
	finally:
		cur.close()
		conn.close()


deleteMysql()
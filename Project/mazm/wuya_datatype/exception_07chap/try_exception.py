#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/5/18   19:26
# @Author　 : mazm
# @ File　　  :try_exception.py
# @Software  :PyCharm
'''


'''

def div(a,b):
	return a/b

'''
try--expect的执行步骤：
1.try代码执行正常，就不会执行expect的代码
2.只有try代码执行异常,就会执行expect的代码
'''

# try:
# 	div(1, 0)
# except KeyError as e:
# 	print e.args
# except ValueError as e:
# 	print e.args
# except ZeroDivisionError as e:
# 	print e.args
# except WindowsError as e:
# 	print e.args
# except EOFError as e:
# 	print e.args

''''分母为0的情况'''
# try:
# 	div(1, 0)
# except Exception as e:
# 	print e.args

'''分母为字符串的情况'''
# try:
# 	div(1, 'sar')
# except Exception as e:
# 	print e.args


'''分母为字符串的情况'''
# try:
# 	div('aaa', {'name':'wuya'})
# except Exception as e:
# 	print e.args

'''分母为字符串的情况'''
# try:
# 	div(1, {'name':'wuya'})
# except Exception as e:
# 	print e.args

'''
try--expect-- else --finalyy:
1.先执行try，如果执行通过，就执行else代码,最后执行finally
2.如果try执行失败,就直接执行执行finally
'''

try:
	div(1,0)
except Exception as e:
	print(e.args)
	raise('我是执行失败了')
else:
	print('pass')
finally:
	print('finally')
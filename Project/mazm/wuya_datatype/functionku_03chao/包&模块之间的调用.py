#author mazm
'''
模块与模块之间的调用方法
1、直接一层一层调用：import 模块
2、from 模块 import 类，函数，变量
3、from 模块 import *(使用这个)
'''


# 调用模块
from model1 import *


# # 调用模块中的变量
# a=model1.index2
# print(a)
# # 调用模块中的函数
# model1.index()
# # 调用类中的函数：先实例化，
# model1.f1().hello()

index()
per=f1().hello()
a=index2
print(a)

'''
包与包之间的调用方法
3、from 包.模块 import *(使用这个)
'''

from function_02chap.Hanshu_test import *
login()

#author mazm
'''
反射就是一种基于字符串的事件驱动！
根据字符串的形式去某个模块中寻找东西---》getattr()
根据字符串的形式去某个模块中判断东西是否存在---》hasattr()
根据字符串的形式去某个模块中设置东西---》setattr()
根据字符串的形式去某个模块中删除东西---》delattr()
'''

# 1、通过__import__的形式导入模块，并赋值给字符串
# 2、通过字符串的形式去模块中寻找指定的函数，并执行
# index=__import__('model1')
#
# index.login()
# index.logout()

import model1

'''
通过getattr的方式，来实现如上的实现过程
1、获取函数
2、获取变量
3、获取类中方法：#通过getattr()来获取类中方法并执行该方法，思路是首先需要类进行实例化，然后再依据getattr()进行
'''
# f=getattr(model1,'login')
# f1=getattr(model1,'logout')
# f()
# f1()
#
# parm=getattr(model1,'django')
# print('model1模块中的变量值为:{0}'.format(parm))
#
#
# obj=model1.Person()
# class1=getattr(obj,'info')
# class1()

'''
通过hasattr的方式，判断属性是否存在，比如判断类中是否存在一个方法，存在返回的是true，不存在返回的是flase
'''
#变量
# mazm=hasattr(model1,'django')
# mazm1=hasattr(model1,'mazm')
# print(mazm)   #true  存在
# print(mazm1)  #False  不存在
#
# #函数
# mazm2=hasattr(model1,'logout')
# print(mazm2)   #true  存在

'''
setattr是设置属性在模块中的内容，下面我们来实现在类中设置一个属性
1
'''

# 设置变量值
# setparm=setattr(model1,'django','我是修改后的model的值')
# print(model1.django)
# 新建一个函数

# obj=hasattr(model1,'newobj') #先判断是否有函数
# print(obj)
#
# setattr(model1,'newobj','我是新建的函数')  #新建一个函数
# objnew=hasattr(model1,'newobj')  #判断是否有新建的函数
# print(objnew)
# grtnew=getattr(model1,'newobj')  #获取新函数的值
# print(grtnew)

# 先判断再设置
# if hasattr(model1,'newobj')==False:
# 	setattr(model1, 'newobj', '我是新建的函数')  # 新建一个函数
# 	objnew = hasattr(model1, 'newobj')  # 判断是否有新建的函数
# 	print('我已经创建好了',objnew)
# else:
# 	print('已经存在了呢')




'''
delattr是删除模块中的东西：类，属性，函数
'''

# delattr(model1,'newobj')
# delnew=hasattr(model1,'newobj')
# print(delnew)

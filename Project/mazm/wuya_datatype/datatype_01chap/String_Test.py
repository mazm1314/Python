#author mazm
#数据类型：字符串

# Python常见的数据类型：数字、字符串、元组()、列表[]、字典{}
# 一旦你创建了变量，然后赋值，就会存储在python的内存里面
# 同名的参数变量会覆盖
# 命名的规范：字符  下划线 数字组成，不能以数字开头，都是小写字母

# p=int(input("你叫什么名字\n"))
# if p==1:
# 	print("nid")
# elif p==2:
# 	print("34")
# else:
# 	print("232")
mazm='mazm'
mazm2='mazm,yangyy'
# 查看字符串的所有方法
print(dir(mazm))
# 查看字符串以什么开始和结尾
print(mazm.startswith('m'))
print(mazm.endswith('m'))
# 替换字符串
mazm1=mazm.replace('ma','maz')
print(mazm1)
# 查看索引
print(mazm.find('z'))
# 判断是否是数字
print(mazm.isdigit())
# 字符分割,会把字符串转换为列表[],
print(mazm2.split(','))

#   字符串--格式化输出：%
# 1、输出整数：%d
# 2、输出浮点数：%f
# 3、指定输出小数点位数：%.2f （2是位数）
# 4、输出字符串：%s
# 5、字符串截取：%.2s 保留2个长度的字符串
age=24
name1="小敏在学习哦"
score=98.3444
# 1、第一种格式化输出
print(str(age)+"年龄的"+name1)
print(age,"年龄的",name1)
print("考了%.2f成绩的%d年龄的%.5s"%(score,age,name1))

# 2、格式化输出 format:{}中的索引引用后续的参数
print("考了{}成绩的{}年龄的{}".format(score,age,name1))
print("考了{0}成绩的{1}年龄的{1}".format(score,age,name1))
# {}不指定时按照顺序取值
# {}指定时按照顺序取值

name='mazm'
age=18
print('我的名字是%s,我今年%d岁了'%(name,age))
print('我的名字是{0},我今年{1}岁了'.format(name,age))#最重要
print('我的名字是{name},我今年{age}岁了'.format(name=name,age=age))





# 2、Python变量---字符串（成对的双引号和单引号）
# 字符串：
a="mazm"
b='mazm1'
# 字符串的取值:缺点：只能取单个字符
print(a)
# 正序访问：mazm 0 1 2 3  字符串是由一个一个字符组成，可以根据索引（从0开始），取单个的字符
print(a[2])
# 反序访问：mazm  -4 -3 -2 -1
print(a[-2])
print(type(a))
print(type(b))

# 处理字符串的特殊字符 \n \t \r
# 方式：1、转义：加r/R,2、加\
c="mazm\rhello" # 此处被换行
d=r"mazmhe\nllo"
e="mazmhe\\nllo"
print("c内容是："+c)
print("d内容是："+d)
print("e内容是："+e)

# 字符串的运算：+（拼接字符串） *（重复输出）
print(e+d) #拼接
print(d*3)   #重复输出 3次

#判断元素是否在字符串中  in   not in（成员运算符）
print("a" in d)

#不同数据类型之间如何拼接：转换成相同的
q=1
w="hello world"
print(str(q)+w)

# 字符串的切片运用：提取字符串中的子字符串  格式：[start:end:step]
res=w[0:5:1]  # k=1  取 0 1 2 3 4   取左不去右，n-1（=5-1=4）结束取值
res=w[0:5:2]  # k=2  取 0 2 4 6 8  4结束取值：hlo
res=w[0:5]  #k=1  取默认值
res=w[:]  #从头取到尾
res=w[1:] #从1默认取完所有值
# 去除所有偶数位，不包含0   取完的话结束位是长度+1
res=w[2:12:2]
print(len(w))
print(res)

# 字符串的内建函数
str="Hello"
# 1：字符串的大小写切换  upper()   lower()
print("转换为大写："+str.upper())
print("转换为小写："+str.lower())
# 2：查找字符串   find(),如果包含，返回索引值，如果不包含，返回-1
str2=str.find("22")
print("查找的结果:{}".format(str2))
# 3:字符串的替换：replace(),,可以指定替换次数
str3=str.replace("l","@")
str4=str.replace("l","@",1)
print("替换后的结果:{}".format(str3))
print("替换后的结果:{}".format(str4))
# 4:字符串的切割：split()
str5=str.split("l")  #返回列表类型的数据，但是元素类型还是字符串
print("切割后的结果:{}".format(str5))
# 5：字符串头尾的处理  strip()
strr="@h@ello@@"
str6=strr.strip("@")
print("处理后的结果:{}".format(str6))
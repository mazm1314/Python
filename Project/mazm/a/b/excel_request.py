# # 以excel驱动用例
# 准备工作
# 1：pandas依赖处理Excel的xlrd模块，所以我们需要提前安装这个，安装命令是：pip install xlrd
# 2:安装pandas模块还需要一定的编码环境，所以我们自己在安装的时候，确保你的电脑有这些环境：Net.4 、VC-Compiler以及winsdk_web，如果大家没有这些软件~可以咨询我们的辅导员索要相关安装工具。
# 3:步骤1和2 准备好了之后，我们就可以开始安装pandas了，安装命令是：pip install pandas
# 读取Excel中的用例
# https://www.cnblogs.com/liulinghua90/p/9935642.html
import pandas as pd
import xlrd
from a.b.def_request import Request
# 路径前面加r转义，
url=r'D:\Desktop\工作文件\mazm.xlsx'
df=pd.read_excel(url)
test_data=df.values
xls=xlrd.open_workbook(url)
print(df.values)#嵌套列表的数据
print("读取sheet的名称：",xls.sheet_names())
# 拿出我们需要的那个excel的那个sheet
worksheet=xls.sheet_by_name('活动接口')

for item in test_data:
    print("目前正在执行的用例是{0}:{1}".format(item[0],item[1]))
    Request().request_method(item[2],eval(item[3]),item[4])
    print(type(item[3]))#已经转换为字符串
    print(type(eval(item[3])))#用eval()函数将字符串转为字典
    # print('http的请求结果为{0}'.format(res))
测试结果可以放在哪里：
1、yaml--->tavern
2、excel
3、json
4、单元测试框架：pytest=unittest


注意注意：
cmd中运行pytest运行时，引入包的from APIFrame.base.method import *的路径要包含在
E:\worksoftware\pycharm\Project\mazm\wuya_datatype\APIFrame>
目录中，不能大于目录的最低层


测试报告：
allureframework   ---针对python中的pytest和testng作报告呈现

安装： pip install allure-pytest
生成：pytest.main(['-v','-s',"--alluredir","./report/result"])

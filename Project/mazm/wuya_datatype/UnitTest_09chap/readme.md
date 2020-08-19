pip install html-testRunner  美化测试报告 python3需要从官网上下载下来放到python的安装目录lib下
pip install uniitest



uniittest内容
1、uniittest介绍
2、测试固件
    1、setup&teardown
    2、setupclass & teardownclass
    3、程序执行的顺序
    4、测试用例的编写样式
3、测试执行
4、构建测试套件
    1、用例按照顺序执行（addtest）
    2、测试用例执行的详解
    3、按照测试类执行（makesuite）
    4、加载测试类（testloader）
    5、按照测试模块来执行
    6、优化测试套件
5、分离测试固件（模块化的应用）
6、测试断言
    assertEqual(a,b)
    assertTrue(x)
    assertIn(a,b)
    测试断言注意的事项：1、不正确的使用if  2、不正确的使用异常
7、批量执行测试用例（discover）
    1、获取所有测试用例
    2、discover方法的解读
8、生成测试报告
    2、python3生成的测试报告
    3、测试报告的注意事项
    4、新增当前时间
9、uniittest的缺陷
10、coverage的应用


金字塔：
UI测试
集成测试
单元测试



代码覆盖率的讲解部分：
pip install coverage  代码覆盖率统计
命令行执行：coverage run xxx.py
该文件中执行：
   1、coverage run testCase\alltest.py
   2、coverage html     #会在文件夹下生成一个htmlcov
然后查看  index.html


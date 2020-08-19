api:
1、单个api的验证
    a-功能：
    b-安全：sign  cookies  ip白名单
    c-性能:
2、外部API的验证----设计mock
    a-淘宝
    b-支付--》回调场景：支付成功后，没有回调成功，还是在待支付的状态
    c-物流
    mock模拟---》
3、全链路的质量保障与覆盖
    a-复杂性：
    b-数据怎么解决
    c-业务关联性--》动态参数的解决
    d-业务覆盖
        d1:独立性
        d2:关联性


tavern简介
tavern 是用于HTTP ，MQTT或者其他协议的基于pytest的高级API测试框架 Tavern

tavern优势
轻量级 直接结合pytest就可以使用 即使不会代码也可以使用 容易编写 方便阅读 可读性比较好

为什么要使用tavern测试？
测试全业务覆盖的API使用自动化脚本测试 会更加利于维护和复用 但如果只是测试 一两个API 再写一个脚本 需要配置那么多的文件 这显然就不那么合适了 所以这时候 用tavern用于测试单个API是很好的选择

使用tavern 需要使用yaml文件 所以需要以下的环境准备

准备工作
pip install pyyaml
pip install pytest==4.5.0
pip install tavern==0.34.0
pip install pytest-html


yaml规范：

在yaml文件中使用关键字的介绍：

test_name ： 这个是给当前测试用例起一个名字
stages: 在这个关键字内的内容就是请求内容
name： 这个还是说明一下这个接口的作用
request: 请求
url: 请求的url
method: 请求的方法(大写)
data: 请求参数
response: 响应断言

语法规则：
1-大小写区分
2-缩进表达层级关系，尽量使用空格，不要使用tab键
3-可以注释，注释使用#
4-支持的数据格式：对象键值对，数组


执行时：到文件的目录下；
1、pytest -v xxx.tavern.yaml   #注意文件后缀是两个
2、pytest -v xxx.tavern.yaml --html=info.html


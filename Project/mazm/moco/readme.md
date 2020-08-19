moco地址：https://github.com/dreamhead/moco
api文档地址：
https://github.com/dreamhead/moco/blob/master/moco-doc/apis.md
启动命令：
java -jar moco-runner-0.12.0-standalone.jar http -p 12306 -c foo.json

moco只关注服务器的配置，也就是客户端与服务端，或者更加具体的说就是请求和响应。

mock在Python3.3之前是第三方的库，在Pyhton3.3版本之后是标准库，只需要导入就可以使用了.
Pyhton3.3版本之前引入方式是：
import mock 
Pyhton3.3版本之后引入方式是：
from unittest import  mock 

Mock的意义：Mocks能够让我们模拟那些在单元测试中不可用或太笨重的资源
Mock是Python中一个用于支持单元测试的库，它的主要功能是使用mock对象替代掉指定的Python对象，以达到模拟对象的行为。Mock它可以替换Python对象。

现实情况：
1、环境由于客观原因导致无法搭建
2、搭建的服务器需要的值需要大量的工作才可以  



www.wuya.com
200
404
500
400
401
403


案例：
1、测试一个网站
2、测试C盘所有的文件

mock中使用patch或者patch.object的目的是为了控制mock的范围,模拟的类或者模拟的函数
，使用 with语句范围内nock一个对象。


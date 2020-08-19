安装：pip install pytest
pip install pytest-selenium
使用webdriver先得安装驱动：
    1、打开浏览器,在地址栏输入chrome://version/便可以查看到谷歌当前的版本号
    2、http://chromedriver.storage.googleapis.com/index.html
    3、还差最后一步,只需要把它放到下面两个路径下即可!
        一个是在C盘的路径下,具体的位置:C:\Program Files (x86)\Google\Chrome\Application
        python安装的目录下,

命令行执行：pytest -v f1.py

到对应测试用例的目录下：E:\worksoftware\pycharm\Project\mazm\wuya_datatype\pytest_10chap

pytest的测试框架中，他的搜索规则是：

在一个被执行的目录下，寻找以test开头或者以test结尾的测试模块，然后执行里面以test开头的测试方法或者测试函数

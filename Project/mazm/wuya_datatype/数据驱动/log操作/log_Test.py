#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/6/25   22:00
# @Author　 : mazm
# @ File　　  :log_Test.py
# @Software  :PyCharm

import  logging
from selenium import  webdriver
import  unittest




def log(log_content):
    # 定义文件
    logFile = logging.FileHandler('log.md', 'a',encoding='utf-8')
    # log格式
    fmt = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s')
    logFile.setFormatter(fmt)

    # 定义日志
    logger1 = logging.Logger('', level=logging.DEBUG)
    logger1.addHandler(logFile)
    logger1.info(log_content)

class test_Ui(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        log('初始化浏览器')

    def test_001(self):
        log('开始测试')
        pass

    def tearDown(self):
        log('测试结束')
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
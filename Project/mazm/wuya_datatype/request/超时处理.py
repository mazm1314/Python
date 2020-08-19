#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/6/5   18:53
# @Author　 : mazm
# @ File　　  :超时处理.py
# @Software  :PyCharm

'''

固定时间---》time

不加延迟，接口超时会报：readTimeout
'''


import requests

# 0.6s以内一直保持等待
r=requests.get('http://httpbin.org/get',timeout=0.6)

print('接口的请求时间为:\n',r.elapsed.total_seconds())
print(r.text)
#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/5/17   15:43
# @Author　 : mazm
# @ File　　  :Serialization_file.py
# @Software  :PyCharm
import requests
import json
'''
文件的序列化和反序列化

dump对象序列化到文件对象，就是存入到文件。
load对象反序列化，从文件读取数据.

'''

url='http://wx-new.kt.ziroom.com/hd/join/join-detail'
request1={"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiJkOWQyNzRlOC03MGZhLWYyOTUtYTVhMS1kODI1Njg0MmZlOGMiLCJ0eXBlIjo1LCJsZW5ndGgiOjEwMDgwLCJ0b2tlbiI6ImUwZDg4ZDFmLWE3OTctNDg3Yi05OTA5LTNmOTE0MWU1YjMwMSIsImNyZWF0ZVRpbWUiOjE1ODk3MDE5MzAxODl9._deEz7czC6IHz6CvERKBFaD5YOGIf7dv3tW1u5VK4b4",
"activity_code": "hy2019","ver": "2020"}

post1=requests.post(url,request1)
# print(post1.text)

# 把文件进行序列化----》就是把服务器的响应数据写到文件中
# json.dump(post1.text,open('haiyan.json','w'))#当前文件下

# 对文件的反序列化:读取文件的内容
res=json.load(open('haiyan.json','r'))
print(res,type(res))

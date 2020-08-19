import requests
# from wuya_datatype.request.token的处理.login import token

from wuya_datatype.request.token的处理.login import *
# 0押金参与详情页
detail_url='http://wx-new.kt.ziroom.com/hd/join/join-detail'
detail_params={'token':login(),'activity_code':'releaseYz1'}

detail_rep=requests.get(detail_url,params=detail_params)
print("detail接口详情页耗时共计:\t",detail_rep.elapsed.total_seconds())

print("查看请求头:\n",detail_rep.request.headers)
print('查看请求的数据：\n',detail_rep.json()['data'])



import requests
import request
import json

# 获取验证码
login_url="https://tpassport.ziroom.com/login/v2"
login_data={'phone':'18810911959','password':'a53c9868827ee7df457110549547fbb0'}
# 以下的headers一个值都不能缺少
login_heders={
    'Accept': 'application/json',
    'Client-Version': '6.5.10',
    'Sys': 'app',
    'Request-Id': '1327D8F2:1587296579'
}
# verify参数设置
# 1、Requests的请求默认verify=True
# 2、如果你将 verify设置为 False，Requests 也能忽略对 SSL 证书的验证

def login():
    login_rep=requests.post(login_url,data=login_data,headers=login_heders)
    return login_rep.json()['resp']['token']


# 利用python去做接口测试：
# 1、安装request模块  :File->Settings->Project Interpreter
# 2、如何确认已经安装好
import requests
import request
# 3、完成HTTP get校园大使认证补偿 请求
# 4、完成HTTP post 请求

# 查看接口返回的具体信息：
# 1、查看text的结果
# 2、查看json结果
# 3、头部、cookie，状态码

# get请求
url='http://persona-api.kt.ziroom.com/api/public/groups/wangk16'
res_get=requests.get(url)

print("get的请求头：",res_get.request.headers)
print("get的响应结果：",res_get)
print("get的响应状态码：",res_get.status_code)
print("get的响应报文：",res_get.content)
print("get的响应头：",res_get.headers)
print("get的响应json结果：",res_get.json())
print("get的响应cookies：",res_get.cookies)

# post请求
URl='http://activity.inside.t.ziroom.com/survey/survey/select-user'
data={"uid":"6e025a92-af81-4aab-bb15-294de11636ca","sign":"9bcc33185ee88c90324e6ef4d9c644da","timestamp":"1586673759","appid":"600011"}
# 给请求添加请求头
headers={'Server': 'nginx', 'Date': 'Sun, 12 Apr 2020 06:58:45 GMT','name':'mazm'}
res_post=requests.post(URl,data=data,headers=headers)

print("post的请求头：",res_post.request.headers)
print(data)
print("post的响应结果：",res_post)
print("post的响应状态码：",res_post.status_code)
print("post的响应报文：",res_post.content)
print("post的响应头：",res_post.headers)
print("post的响应json结果：",res_post.json())
print("post的响应cookies：",res_post.cookies)


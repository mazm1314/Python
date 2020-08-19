import requests
import json

# HTTP请求类型
# get类型
r1 = requests.get('https://github.com/timeline.json')
# post类型
r2= requests.post("http://m.ctrip.com/post")
# put类型
r3 = requests.put("http://m.ctrip.com/put")
# delete类型
r4= requests.delete("http://m.ctrip.com/delete")
# head类型
r5= requests.head("http://m.ctrip.com/head")
# options类型
r6= requests.options("http://m.ctrip.com/get")

# 获取响应内容
print(r1.content)  # 以字节的方式去显示，中文显示为字符
print(r1.text)  # 以文本的方式去显示

# URL传递参数
payload = {'keyword': '香港', 'salecityid': '2'}
r7= requests.get("http://m.ctrip.com/webapp/tourvisa/visa_list", params=payload)
print("查看增加参数后的链接:",r7.url) # 示例为http://m.ctrip.com/webapp/tourvisa/visa_list?salecityid=2&keyword=香港

# 获取/修改网页编码
r8 = requests.get('https://github.com/timeline.json')
print("查看该链接的编码:",r8.encoding)


# json处理
r9 = requests.get('https://github.com/timeline.json')
print("查看r9json处理前的结果:",r9.text)
print("查看r9json处理后的结果:",r9.json())# 需要先import json

# 定制请求头
url='http://m.ctrip.com'
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 4 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19'}
r10 = requests.post(url, headers=headers)
print("查看r10增加的headers:",r10.request.headers)

# 复杂post请求
url = 'http://m.ctrip.com'
payload = {'some': 'data'}
print("查看payload的类型",type(payload))
r11 = requests.post(url, data=json.dumps(payload))  # 如果传递的payload是string而不是dict，需要先调用dumps方法格式化一下
print("查看post的链接",r11.url)

# post多部分编码文件
# url = 'http://m.ctrip.com'
# files = {'file': open('report.xls', 'rb')}
# r12 = requests.post(url, files=files)

# 响应状态码
r13 = requests.get('http://m.ctrip.com')
print("查看r13的响应码",r13.status_code)

# 响应头
r14 = requests.get('http://m.ctrip.com')
print("查看r14的响应头",r14.headers)
print(r14.headers['Content-Type'])
print(r14.headers.get('content-type'))  # 访问响应头部分内容的两种方式

# Cookies
# url = 'http://hd.t.ziroom.com/2019new/zrk_school//?router=login&utm_source=test'
# r15 = requests.get(url)
# print(r15)
# r15.cookies['CURRENT_CITY_CODE']  # 读取cookies

# url = 'http://m.ctrip.com/cookies'
# cookies = dict(cookies_are='working')
# r16 = requests.get(url, cookies=cookies)  # 发送cookies
#
# # 设置超时时间
# r17 = requests.get('http://m.ctrip.com', timeout=0.001)
#
# # 设置访问代理
# proxies = {"http": "http://10.10.1.10:3128","https": "http://10.10.1.100:4444",}
# r18=requests.get('http://m.ctrip.com', proxies=proxies)
#
# # 如果代理需要用户名和密码，则需要这样：
# proxies = {"http": "http://user:pass@10.10.1.10:3128/"}
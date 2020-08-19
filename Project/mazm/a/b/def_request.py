import requests
import request
class Request:
    def request_method(self,url,data,http_method='post'):#注意实例化函数前面的self
        if http_method.upper()=='GET':
            res=requests.get(url,data)
        else:
            res=requests.post(url,data)
        print("http的请求结果为：",res.json())
        print("http的请求头为：",res.headers)
#
# URl='http://activity.inside.t.ziroom.com/survey/survey/select-user'
# data={"uid":"6e025a92-af81-4aab-bb15-294de11636ca","sign":"9bcc33185ee88c90324e6ef4d9c644da","timestamp":"1586673759","appid":"600011"}

# Request().request_method(URl,data,'post')


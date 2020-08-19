#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/7/2   17:33
# @Author　 : mazm
# @ File　　  :ful_01.py
# @Software  :PyCharm


from flask import *
from flask_restful import Resource,Api,reqparse
from flask_httpauth import HTTPBasicAuth

app=Flask(__name__)   #实例化操作，因为他是一个类
api=Api(app=app)   #app就是一个应用
auth=HTTPBasicAuth()   #鉴权里面的基本认证实例化

@app.route('/index')  #路由地址
@auth.login_required() #给这个接口增加鉴权机制
def index():
	# 将数据解析为json
	return jsonify({'status':0,'msg':'ok','data':{'userID':1001,'name':'mazm','age':13}})

'''
案例演示接口测试的维度

401:需要认证，鉴权
403:其实本质也是鉴权
404:找不到资源，地址不存在
405:接口以post请求，但是以get发起  405不允许此方法
'''

# 模拟401需要
@auth.get_password
def get_password(username):
	if username=='mazm':
		return 'mazm1818'


@auth.error_handler
def authorized():
	return make_response(jsonify({'msg':'您好，请认证！'}),401)

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error':'资源走丢了，请寻求其他帮助'}),404)

@app.errorhandler(405)
def not_found(error):
	return make_response(jsonify({'error':'该方法只支持GET请求'}),405)


# 这里随便输入一个地址测试--404：http://127.0.0.1:5000/index/ssd
# 这里随便输入一个地址测试--405：http://127.0.0.1:5000/index






# class LoginView(Resource):
# 	def get(self):
# 		return jsonify({'status':0,'msg':'ok','data':''})
#
# 	def post(self):
# 		parser=reqparse.RequestParser()
# 		parser.add_argument('username',type=str,required=True,help='您的用户名参数不能为空')
# 		parser.add_argument('password',type=str)
# 		parser.add_argument('age',type=int,help='您的年龄必须是整型')
# 		return jsonify({'status':0,'msg':'ok','data':parser.parse_args()})
#
# api.add_resource(LoginView,'/login',endpoint='login')



if __name__ == '__main__':
    app.run(debug=True)

    # 请求接口：http://127.0.0.1:5000/index
#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/7/5   20:12
# @Author　 : mazm
# @ File　　  :完善_管理系统.py
# @Software  :PyCharm
from flask import Flask,make_response,jsonify,abort,request
from  flask_restful import Api,Resource
from  flask_httpauth import HTTPBasicAuth

app=Flask(__name__)
api=Api(app=app)
auth=HTTPBasicAuth()

@auth.get_password
def get_password(name):
	if name=='mazm':
		return 'mazm1018'

@auth.error_handler
def authorized():
	return make_response(jsonify({"msg":"请认证"}),401)

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error':'资源走丢了，请寻求其他帮助'}),404)

books=[
	{'id':1,'author':'mazm','name':'图书管理实战','done':True},
	{'id':2,'author':'小小','name':'图书管理实战','done':False}
]

class Books(Resource):
	decorators = [auth.login_required]  # 增加鉴权
	'''查询书籍信息'''
	def get(self):
		return jsonify(books)
	'''新增书籍信息'''
	def post(self):
		if not request.json:
			return jsonify({'status':1001,'msg':'请求的参数不是JSON数据，请检查，谢谢'})
		else:
			book={
				'id': books[-1]['id'] + 1,  # 最后一位增加1
				'author': request.json.get('author'),
				'name': request.json.get('name'),
				'done': True
			}
			books.append(book)
			return jsonify({'status': 1002, 'msg': 'created ok '})

class Book(Resource):
	decorators = [auth.login_required]   #增加鉴权

	'''根据id查询书籍信息'''
	def get(self, book_id):
		book = list(filter(lambda t: t['id'] == book_id, books))
		if len(book) == 0:
			return jsonify({'status': 1003, 'msg': '很抱歉，你查询的数据不存在'})
		else:
			return jsonify({'status': 0, 'msg': 'ok', 'datas': book})

	'''根据id修改书籍信息'''
	def post(self, book_id):
		book = list(filter(lambda t: t['id'] == book_id, books))
		if len(book) == 0:
			return jsonify({'status': 1003, 'msg': '很抱歉，你查询的数据不存在'})
		elif not request.json:
			return jsonify({'status': 1001, 'msg': '请求的参数不是JSON数据，请检查，谢谢'})
		elif 'author' not in request.json:
			return jsonify({'status': 1004, 'msg':'请求参数author不能为空' })
		elif 'name' not in request.json:
			return jsonify({'status': 1005, 'msg':'请求参数name不能为空' })
		elif 'done' not in request.json:
			return jsonify({'status': 1006, 'msg': '请求参数done不能为空'})
		elif type(request.json['done']) is not bool:
			return jsonify({'status': 1007, 'msg': '请求参数done为bool类型'})

			abort(400)
		else:
			book[0]['author'] = request.json.get('author', book[0]['author'])
			book[0]['name'] = request.json.get('name', book[0]['name'])
			book[0]['done'] = request.json.get('done', book[0]['done'])
			return jsonify({'status': 1008, 'msg': '更新图书信息成功', 'dats': book})

	'''根据id删除书籍信息'''
	def post(self, book_id):
		book = list(filter(lambda t: t['id'] == book_id, books))
		if len(book) == 0:
			return jsonify({'status': 1003, 'msg': '很抱歉，你查询的数据不存在'})
		else:
			books.remove(book[0])
			return jsonify({'status': 1009, 'msg': '书籍的信息已经删除成功'})




api.add_resource(Books,'/v1/api/books')
api.add_resource(Book,'/v1/api/book/<int:book_id>')

if __name__ == '__main__':
    app.run(debug=True)
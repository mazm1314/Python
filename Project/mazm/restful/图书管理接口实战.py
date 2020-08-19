#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/7/5   19:33
# @Author　 : mazm
# @ File　　  :图书管理接口实战.py
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

'''查看图书信息'''
@app.route('/v1/api/books',methods=['GET'])
@auth.login_required
def get_books():
	return jsonify(books)

'''增加图书信息'''
@app.route('/v1/api/books',methods=['POST'])
@auth.login_required
def create_books():
	if not request.json:
		abort(400)
	else:
		book={
			'id':books[-1]['id']+1,#最后一位增加1
			'author':request.json.get('author'),
			'name':request.json.get('name'),
			'done':True
		}
		books.append(book)
		return jsonify({'msg':'created ok '},201)

'''根据id查找图书信息'''
@app.route('/v1/api/book/<int:book_id>',methods=['GET'])
@auth.login_required
def get_book(book_id):
	book=list(filter(lambda t:t['id']==book_id,books))
	if len(book)==0:
		abort(404)
	else:
		return jsonify({'status':0,'msg':'ok','datas':book})


'''根据id删除图书信息'''
@app.route('/v1/api/book/<int:book_id>',methods=['DELETE'])
@auth.login_required
def delete_book(book_id):
	book=list(filter(lambda t:t['id']==book_id,books))
	if len(book)==0:
		abort(404)
	else:
		books.remove(book[0])
		return jsonify({'status':1001,'msg':'书籍的信息已经删除成功'})



'''根据id修改图书信息'''
@app.route('/v1/api/book/<int:book_id>',methods=['PUT'])
@auth.login_required
def update_book(book_id):
	book=list(filter(lambda t:t['id']==book_id,books))
	if len(book)==0:
		abort(404)
	elif not request.json:
		abort(400)
	elif 'author' not  in request.json and 'name' not in request.json:
		abort(400)
	elif 'done' not in request.json and type(request.json['done']) is not bool:
		abort(400)
	else:
		book[0]['author']=request.json.get('author',book[0]['author'])
		book[0]['name'] = request.json.get('name', book[0]['name'])
		book[0]['done'] = request.json.get('done', book[0]['done'])
		return jsonify({'status':1002,'msg':'更新图书信息成功','dats':book})


if __name__ == '__main__':
    app.run(debug=True)




import pytest

from APIFrame.base.method import *
from APIFrame.utils.OperationYAML import Operationyaml
'''
pytest的参数化讲解，接章节10 的课程

参数化：对列表中的元素进行循环
用例中的参数必须跟参数化的参数保持一致，

单个的API的测试--面向函数式的测试方案

'''
# 实例化
obj=Requests()
objyaml=Operationyaml()

'''循环读取login.yaml中的数据进行请求，参数化可以循环读取yaml文件中列表，避免重复性的工作'''
@pytest.mark.parametrize('datas',objyaml.readYaml())
def test_login(datas):
	r=obj.post(url=datas['url'],data=datas['data'],headers=datas['headers'])
	# print(type(datas['url']))
	# print(type(datas['data']))
	# print(type(datas['headers']))
	except_res=datas['except']
	true_res=r.json()['message']
	# print(true_res)
	# print(r.text)
	assert except_res in  true_res
	# assert except_res ==  true_res
	# print(type(datas['data']))


# @pytest.mark.parametrize('data',objyaml.readYaml())
# def test_login(data):
# 	print(data['url'])

# def add(a,b):
# 	return a+b
#
# @pytest.mark.parametrize('a,b,result',[
# 	(1,2,3),
# 	(1,2,4)
# ])
# def test_add(a,b,result):
# 	assert add(a,b)==result


if __name__ == '__main__':
    pytest.main(['-s','-v'])



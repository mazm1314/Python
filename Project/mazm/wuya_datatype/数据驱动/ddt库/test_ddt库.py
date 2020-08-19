#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/6/21   16:50
# @Author　 : mazm
# @ File　　  :ddt库.py
# @Software  :PyCharm
'''
测试拉勾网的翻页

在ddt的模块中，@data标识元组的列表数据，@unpack表示用来解压元组到多个参数，
ddt只适用于行同步轴的测试用例，这点要切记，

'''
import  requests
import ddt
import pytest

def getHeaders():
	headers={
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
		'Referer':'https://www.lagou.com/jobs/list_%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=sug&fromSearch=true&suginput=%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95'}
	return headers


@ddt.ddt()
class TestLaGou():
	@ddt.data((2,), (3,), (4,))
	@ddt.unpack
	def test_laGou(self,page=2):
		url_start = "https://www.lagou.com/jobs/list_运维?city=%E6%88%90%E9%83%BD&cl=false&fromSearch=true&labelWords=&suginput="
		url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
		s = requests.Session()  # 创建一个session对象
		s.get(url_start, headers=getHeaders(), timeout=2)  # 用session对象发出get请求，请求首页获取cookies
		cookie = s.cookies  # 为此次获取的cookies
		r = requests.post(
			url=url,
			headers=getHeaders(),
			cookies=cookie,
			data={'first': False, 'pn': page, 'kd': '自动化测试工程师'},
			timeout=3)
		assert r.json()['content']['positionResult']['result'][0]['city'] in ('深圳','上海','武汉','广州','北京')
		print(r.json()['content']['positionResult']['result'][0]['city'])

if __name__ == '__main__':
	pytest.main(['-v','-s'])

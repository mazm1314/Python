#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/6/20   15:34
# @Author　 : mazm
# @ File　　  :CSV写操作.py
# @Software  :PyCharm
import  csv
import  requests
import time




def getHeaders():
	headers={
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
		'Referer':'https://www.lagou.com/jobs/list_%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=sug&fromSearch=true&suginput=%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95'}
	return headers


def laGou(url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false',page=2):
	positions = []
	url_start = "https://www.lagou.com/jobs/list_运维?city=%E6%88%90%E9%83%BD&cl=false&fromSearch=true&labelWords=&suginput="
	s = requests.Session()  # 创建一个session对象
	s.get(url_start, headers=getHeaders(), timeout=2)  # 用session对象发出get请求，请求首页获取cookies
	cookie = s.cookies  # 为此次获取的cookies
	r = requests.post(
		url=url,
		headers=getHeaders(),
		cookies=cookie,
		data={'first': False, 'pn': page, 'kd': '自动化测试工程师'},
		timeout=3)
	time.sleep(5)
	for i in range(15):
		city = r.json()['content']['positionResult']['result'][i]['city']
		education = r.json()['content']['positionResult']['result'][i]['education']
		workYear = r.json()['content']['positionResult']['result'][i]['workYear']
		positionAdvantage = r.json()['content']['positionResult']['result'][i]['positionAdvantage']
		salary = r.json()['content']['positionResult']['result'][i]['salary']
		companyFullName = r.json()['content']['positionResult']['result'][i]['companyFullName']
		positionLables = r.json()['content']['positionResult']['result'][i]['positionLables']
		position = {
			'公司名称': companyFullName,
			'城市': city,
			'学历': education,
			'工作年限': workYear,
			'薪资': salary,
			'工作标签': positionLables,
			'福利': positionAdvantage
		}
		positions.append(position)
	for item in positions:
		return item
		# print(item)

if __name__ == '__main__':
	laGou(page=2)
	# for item in range(1, 2):
	# 	laGou(page=item)




def writeCsv():
	headers={'公司名称','城市','学历','工作年限','薪资','工作标签','福利'}
	# for item in range(1, 2):
		# positions=dict(laGou(page=item))
	positions=laGou(page=2)
	print(type(positions))
	with open('lagou.csv','a',newline='',encoding='gbk') as f:
		writer=csv.DictWriter(f,headers)
		writer.writeheader()
		writer.writerows(positions.values())
writeCsv()


#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/6/20   19:05
# @Author　 : mazm
# @ File　　  :1.py
# @Software  :PyCharm
import requests
from bs4 import BeautifulSoup
import csv

url = "https://movie.douban.com/cinema/later/chengdu/"
response = requests.get(url)
soup = BeautifulSoup(response.content.decode('utf-8'), 'lxml')
all_movies = soup.find('div', id = "showing-soon")
#写模式打开csv文件
csv_obj = open('data.csv', 'w', encoding="utf-8")
#写入一行标题
csv.writer(csv_obj).writerow(["影片名", "链接", "上映日期", "影片类型", "地区", "关注者"])
for each_movie in all_movies.find_all('div', class_ = "item"):
    all_a = each_movie.find_all('a')
    all_li = each_movie.find_all('li')
    movie_name = all_a[1].text
    movie_href = all_a[1]['href']
    movie_date = all_li[0].text
    movie_type = all_li[1].text
    movie_area = all_li[2].text
    movie_lovers = all_li[3].text
    # 逐个写入电影信息
csv.writer(csv_obj).writerow([movie_name,movie_href,movie_date,movie_type,movie_area,movie_lovers])
#关闭
csv_obj.close()
print("finshed")
import requests


from bs4 import BeautifulSoup

# 爬取图片信息
# 安装第三方软件，beautiful soup    用来抓取数据，代替正则匹配  安装 bs4  lxml
# contents=requests.get('http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CD%BC%C6%AC&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=000000').text
# #
# # print(contents)
#
# soup=BeautifulSoup(contents,'lxml')
# # print(soup.prettify())
# # 获取标题
# print(soup.title)
# # 获取标题内容
# print(soup.title.string)
# # 获取标签
# print(soup.p)

con=requests.get('https://www.baidu.com/s?cl=3&tn=baidutop10&fr=top1000&wd=%E8%80%83%E7%A0%94%E5%9B%BD%E5%AE%B6%E7%BA%BF%E5%85%AC%E5%B8%83&rsv_idx=2&rsv_dl=fyb_n_homepage&hisfilter=1').text

soup=BeautifulSoup(con,'lxml')

for title in soup.find_all('div',class_='option '):
    print(title.get('title'))



print(con)



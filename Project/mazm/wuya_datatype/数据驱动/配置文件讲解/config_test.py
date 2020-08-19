#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time　　:2020/6/16   17:52
# @Author　 : mazm
# @ File　　  :config_test.py
# @Software  :PyCharm

import os
import configparser

def base_dir(filename=None):
	return os.path.join(os.path.dirname(__file__),filename)


def getconfig(linux='linux'):
	list1=[]
	config=configparser.ConfigParser()
	config.read(base_dir('config.ini'))
	ip=config.get(linux,'IP')
	port=config.get(linux,'PORT')
	username=config.get(linux,'USERNAME')
	password=config.get(linux,'USERNAME')
	list1.append(ip)
	list1.append(port)
	list1.append(username)
	list1.append(password)
	return list1

print(getconfig()[0])
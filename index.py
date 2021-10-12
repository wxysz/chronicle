#-*-coding:utf-8
import os,sys
import requests
import xml.etree.ElementTree as ET
import datetime

def getNVisitor():
	naver_id = 'proevil' # 네이버 아이디
	headers = {'User-Agent': 'Mozilla/5.0'}	
	res = requests.get("https://blog.naver.com/NVisitorgp4Ajax.nhn?blogId="+naver_id,headers=headers,timeout=5)	
	print("#########################################")
	print(res.text)
	print("#########################################")
	return ET.fromstring(res.text)	
	
def getToDay():
	return datetime.datetime.today().strftime("%Y%m%d")

def getNowTime():
	return datetime.datetime.today().strftime("%Y.%m.%d %H시%M분")


if __name__ == '__main__':
	try:
		visitor_xtree = getNVisitor()		
		for node in visitor_xtree.findall('visitorcnt'):
			if getToDay() == node.get('id'):
				print("%s %s명이 방문했어요!" %(getNowTime(), node.get('cnt')))
				break											
	except Exception as e:
		print("e: ",e)

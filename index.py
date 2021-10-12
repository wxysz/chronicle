#-*-coding:utf-8
import os,sys
import requests
import xml.etree.ElementTree as ET
import datetime
import telegram
from pytz import timezone
 
KST = datetime.datetime.now(timezone('Asia/Seoul'))
 
def getNVisitor():
	naver_id = 'ahnsk3939'
	headers = {'User-Agent': 'Mozilla/5.0'}	
	res = requests.get("https://blog.naver.com/NVisitorgp4Ajax.nhn?blogId="+naver_id,headers=headers,timeout=5)	
	# print("#########################################")
	# print(res.text)
	# print("#########################################")
	return ET.fromstring(res.text)	
def getToDay():
	return KST.strftime("%Y%m%d")
def getNowTime():
	return KST.strftime("%Y년%m월%d일 %H시%M분")

def sendMsg(telegram_token, msgText):
	bot 	= telegram.Bot(token = telegram_token)
	cat_id 	= '-1001400475289'			
	bot.sendMessage(chat_id = cat_id, text=msgText)	


if __name__ == '__main__':
	telegram_token = sys.argv[1]
	try:
		visitor_xtree = getNVisitor()		
		for node in visitor_xtree.findall('visitorcnt'):
			if getToDay() == node.get('id'):
				msgText = ("%s %s명이 방문했어요!" %(getNowTime(), node.get('cnt')))
				print(msgText)
				sendMsg(telegram_token, msgText)
				break															
	except Exception as e:
		print("e:",e)

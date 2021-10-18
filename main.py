from bs4 import BeautifulSoup
import requests
import json
import os
import sys
import re
from urllib.request import urlopen
from html import unescape

#datas = soup.select("div.ranking")
#datas = soup.select(    'div.sub-contents-wrap > div > div:nth-child(2) > table'    )
'''
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print('뉴스기사 스크래핑 시작')

req = requests.get('https://www.yna.co.kr/safe/news')
req.encoding= None
html = req.content
soup = BeautifulSoup(html, 'html.parser')
datas = soup.select(
    'div.contents > div.content01 > div > ul > li >article > div >h3'
    )

data = {}

for title in datas:   
    name = title.find_all('a')[0].text
    url = 'http:'+title.find('a')['href']
    data[name] = url

with open(os.path.join(BASE_DIR, 'rank.json'), 'w+',encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii = False, indent='\t')

print('뉴스기사 스크래핑 끝')
'''

'''
html3 = """<html> <head><title>test  site</title></head> <body><p>test</p> <p>test1</p> <p>test2</p> </body></html>"""
soup3 = BeautifulSoup(html3, 'lxml')
print(soup3.prettify())  # html 구조로 이쁘게 보여주기
'''

'''
#=========================== 네이버 쇼핑 제이슨
file = open("./naver.json", "w")

url = "https://search.shopping.naver.com/search/all?query=%EA%B1%B4%EC%A1%B0%EA%B8%B0&cat_id=&frm=NVSHATC"
html1 = requests.get(url)
soup1 = BeautifulSoup(html1.text, 'lxml')
cnt = len(soup1.find_all('div', class_='basicList_title__3P9Q7'))

for i in range(0,cnt) :
    naver = {}
    metadata = soup1.find_all('div', class_='basicList_title__3P9Q7')[i]
    title = metadata.a.get('title')
    print("<제품명> : ", title)               # title
    
    price = soup1.find_all('span', class_='price_num__2WUXn')[i].text
    print("<가격> : ", price)                # 가격
    
    url = metadata.a.get('href')
    print("<url> : ", url)                  # url
         
    print("===================================================")
    
    naver = {'제품명' : title , '가격' : price, 'url' : url }
    file.write(json.dumps(naver))

file.close()
'''

'''
#===========================
# 웹 페이지 읽어오기
req = urlopen("http://www.hanbit.co.kr/store/books/full_book_list.html")
encoding = req.info().get_content_charset(failobj="utf-8")
html2 = req.read().decode(encoding)

#    kleague_club_ranking_url = "https://kleague.com/api/clubRank.do"
#    jsonObject = json.loads(kleague_club_ranking_url)
#    jsonArray = jsonObject.get("data")
#    for list in jsonArray:
#         print(list)

# 파일 생성
with open("booklist.json", "w", encoding="utf-8") as f:
    data = []
    # 데이터 추출
    for partial_html in re.findall(r'<td class="left"><a.*?</td>', html2, re.DOTALL):
        url = re.search(r'<a href="(.*?)">', partial_html).group(1)
        url = 'http://www.hanbit.co.kr' + url
        title = re.sub(r'<.*?>', '', partial_html)
        title = unescape(title)
        data.append({"BookName": title, "Link": url})
        # 데이터 json 형태로 출력
        print(json.dumps(data, ensure_ascii=False, indent=2))
        
    # 데이터 변형 및 추가
    json.dump(data, f, ensure_ascii=False, indent=2)
'''

file_path = "rank.json"

data = {}
data['posts'] = []
data['posts'].append({
    "title": "How to get stroage size",
    "url": "https://codechacha.com/ko/get-free-and-total-size-of-volumes-in-android/",
    "draft": "false"
})
data['posts'].append({
    "title": "Android Q, Scoped Storage",
    "url": "https://codechacha.com/ko/android-q-scoped-storage/",
    "draft": "false"
})

with open(file_path, 'w') as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent="\t")
    


# https://www.python2.net/questions-763617.htm
'''
url1 = 'https://irus.jisc.ac.uk/api/sushilite/v1_7/GetReport/?Report=IR1&Release=4&RequestorID=Cambridge&BeginDate=2020-01&EndDate=2020-05&ItemIdentifier=irusuk%3A1861749&Granularity=Monthly&Pretty=Pretty'
req1 = requests.get(url1)
html1 = req1.text
soup1 = BeautifulSoup(html1,'html.parser')
site_json=json.loads(soup1.text)
for itemIdentifier in site_json["ReportResponse"]["Report"]["Report"]['Customer']["ReportItems"]:
    for itemPerformance in itemIdentifier["ItemPerformance"]:
        print(itemPerformance["Instance"]["Count"])
'''
        # ?leagueId=" + leagueId + "&year=" + year + "&stadium=" + stadium + "&recordType=" + recordType
        # https://kleague.com/record/teamRank.do?leagueId=1&year=2021&stadium=all&recordType=null

'''
rank1 = []
rank2 = []
url2 = 'https://kleague.com/api/clubRank.do'
req2 = requests.get(url2)
html2 = req2.text
soup2 = BeautifulSoup(html2,'html.parser')
rank_json=json.loads(soup2.text)
rank1 = rank_json["data"]["league1"]
rank2 = rank_json["data"]["league2"]
rank_zip = rank1 + rank2
#for league_ranking in rank_zip:
#        print(json.dumps(league_ranking, ensure_ascii=False, indent="\t"))
        
league_rank = dict()
league_rank = rank_zip
with open('rank.json', 'w+', encoding='utf-8') as make_file:
    json.dump(rank_zip, make_file, ensure_ascii=False, indent="\t")
    
with open('rank.json', 'r') as read_file:
    json_data = json.load(read_file)
    json.dumps(json_data, ensure_ascii=False, indent="\t")
#print(json.dumps(json_data, ensure_ascii=False, indent="\t") )
'''

'''    
json_data = {}
file_path = "./rank.json"
    with open("rank.json", "r") as json_file:
        json_data = json.load(json_file)
        json_data.append(rank_zip)

    with open("rank.json", 'w') as outfile:
        json.dumps(outfile, ensure_ascii=False, indent=2)
'''
    

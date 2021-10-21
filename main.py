import os
import sys
import requests
import json
from bs4 import BeautifulSoup
from github import Github
from datetime import datetime
from pytz import timezone

#datas = soup.select("div.ranking")
#datas = soup.select(    'div.sub-contents-wrap > div > div:nth-child(2) > table'    )

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

with open(os.path.join(BASE_DIR, 'news.json'), 'w+',encoding='utf-8') as json_file:
  json.dump(data, json_file, ensure_ascii = False, indent='\t')



print('뉴스기사 스크래핑 끝')


req1 = requests.get('https://kleague.com/api/clubRank.do')
req1.encoding= None
html1 = req1.content
soup1 = BeautifulSoup(html1, 'html.parser')
rank = json.loads(soup1.text)

seoul_timezone = timezone('Asia/Seoul')
today = datetime.now(seoul_timezone)
today_date = today.strftime("%Y년 %m월 %d일")

access_token = os.environ['MY_GITHUB_TOKEN']
repository_name = "chronicle" # 내 저장소 이름 필수로 바꿔야함 

g = Github(access_token)
repo = g.get_user().get_repo(repository_name)

# issue_title = f"리그 순위({today_date})"

# repo.create_issue(title=issue_title, body=rank)

with open(os.path.join(BASE_DIR, 'rank.json'), 'w+', encoding="utf-8") as f:
    json.dump(rank, f, ensure_ascii = False, indent=2)

# https://www.python2.net/questions-763617.htm
# https://devpouch.tistory.com/33

    

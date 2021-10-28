import os
import sys
import requests
import json
from bs4 import BeautifulSoup
from github import Github
from datetime import datetime
from pytz import timezone

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('https://kleague.com/api/clubRank.do')
req.encoding= None
html = req.content
soup = BeautifulSoup(html, 'html.parser')
rank = json.loads(soup.text)

rank_json = json.dumps(rank, sort_keys=True)  # dict()를 str로 변경 rank, indent=2, sort_keys=True

with open(os.path.join(BASE_DIR, 'rank.json'), 'w+', encoding="utf-8") as f:
    json.dump(rank, f, ensure_ascii = False, indent=2)
        
seoul_timezone = timezone('Asia/Seoul')
today = datetime.now(seoul_timezone)
today_date = today.strftime("%Y년 %m월 %d일")

access_token = os.environ['MY_GITHUB_TOKEN']
repository_name = "chronicle" # 내 저장소 이름 필수로 바꿔야함 

g = Github(access_token)
repo = g.get_user().get_repo(repository_name)

# http://throughkim.kr/2016/04/01/beautifulsoup/
# https://www.kovo.co.kr/game/v-league/11210_team-ranking.asp # 남자 ?season=018&g_part=201&s_part=1 # 여자 ?season=018&g_part=201&s_part=2
'''
req1 = requests.get('https://www.kovo.co.kr/game/v-league/11210_team-ranking.asp?season=018&g_part=201&s_part=2')
req1.encoding= None
html1 = req.content
soup1 = BeautifulSoup(html, "lxml")
table_div = soup.find(id="wrp_lst mt10")
tables = table_div.find_all("table")
'''
req1 = requests.get('http://dgucoop.dongguk.edu/store/store.php?w=4&l=2&j=0')
req1.encoding= None
soup1 = BeautifulSoup(html, "lxml")
table_div = soup1.find(id="sdetail")
tables = table_div.find_all("table")
menu_table = tables[1]
trs = menu_table.find_all('tr')
sangrok_bakban_lunch = trs[8]
tds = sangrok_bakban_lunch.find_all('td')
mon = tds[3].span.string
tue = tds[4].span.string
wed = tds[5].span.string
thu = tds[6].span.string
fri = tds[7].span.string

print(mon, tue, wed, thu, fri)


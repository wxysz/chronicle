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

file = repo.get_contents('rank.json')

# repo.update_file('rank.json', "file update", rank_json, file.sha)


req1 = requests.get('https://www.kovo.co.kr/game/v-league/11210_team-ranking.asp?season=018&g_part=201&s_part=2')
req1.encoding= None
html1 = req1.content
soup1 = BeautifulSoup(html1, 'html.parser')
datas = soup1.select( #tab1 > div.wrp_lst.mt10 )

print(datas)
'''
for title in datas:   
    name = title.find_all('a')[0].text
    url = 'http:'+title.find('a')['href']
    data[name] = url

with open(os.path.join(BASE_DIR, 'news.json'), 'w+',encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii = False, indent='\t')
   ''' 
# V_League_Rank = json.dumps(V_League, sort_keys=True)  # dict()를 str로 변경 rank, indent=2, sort_keys=True

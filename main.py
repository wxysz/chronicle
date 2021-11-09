import os
import sys
import requests
import json
from bs4 import BeautifulSoup
from github import Github
from datetime import datetime
from pytz import timezone
import pandas
import calendar

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('https://kleague.com/api/clubRank.do')
req.encoding= None
html = req.content
soup = BeautifulSoup(html, 'html.parser')
rank = json.loads(soup.text)

rank_json = json.dumps(rank, sort_keys=True)  # dict()를 str로 변경 rank, indent=2, sort_keys=True

with open(os.path.join(BASE_DIR, 'rank.json'), 'w+', encoding="utf-8") as f:
    json.dump(rank, f, ensure_ascii = False, indent=2)
        

days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
seoul_timezone = timezone('Asia/Seoul')
today = datetime.now(seoul_timezone)
# today_date = today.strftime("%Y년 %m월 %d일 %A요일")
today_date_year = today.strftime("%Y")
today_date_month = today.strftime("%m")
today_date_day = today.strftime("%d")
yyyy = int(today_date_year)
mm = int(today_date_month)
dd = int(today_date_day)
dotw = calendar.weekday(yyyy, mm, dd)

print(days[dotw])

access_token = os.environ['MY_GITHUB_TOKEN']
repository_name = "chronicle" # 내 저장소 이름 필수로 바꿔야함 

g = Github(access_token)
repo = g.get_user().get_repo(repository_name)

# https://m.blog.naver.com/kiddwannabe/221811618848
# http://throughkim.kr/2016/04/01/beautifulsoup/
# https://www.kovo.co.kr/game/v-league/11210_team-ranking.asp # 남자 ?season=018&g_part=201&s_part=1 # 여자 ?season=018&g_part=201&s_part=2

req1 = requests.get('https://www.kovo.co.kr/game/v-league/11210_team-ranking.asp?season=018&g_part=201&s_part=2')
req1.encoding= None
html1 = req.content
soup1 = BeautifulSoup(html, "lxml")

# 현재 페이지에서 table 태그 모두 선택하기
#tables = soup1.select('#tab1 > div.wrp_lst.mt10')
tables = soup1.find_all('tr')
print(tables)
'''
# 하나의 테이블 태그 선택하기
table = tables[0]

# 테이블 html 정보를 문자열로 변경하기
table_html = str(table)

# 판다스의 read_html 로 테이블 정보 읽기
table_df_list = pandas.read_html(table_html)

# 데이터프레임 선택하기
table_df = table_df_list[0]

print(table_df)
'''

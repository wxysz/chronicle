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
# today_date_year = today.strftime("%Y")
# today_date_month = today.strftime("%m")
# today_date_day = today.strftime("%d")
# today_date_week = today.strftime("%A")

day = ['월', '화', '수', '목', '금', '토', '일']
tw = datetime.today().weekday()
now = str(today.year) + '-' + str(today.month) + '-' + str(today.day) + '-' + day[tw]
print(now)
'''
yyyy = int(today_date_year)
mm = int(today_date_month)
dd = int(today_date_day)
dotw = calendar.weekday(yyyy, mm, dd)
print(days[dotw])


### 요일 구하기
import datetime
 
def what_day_is_today(self):
    now = datetime.datetime.now()
    t = ['월', '화', '수', '목', '금', '토', '일']
    r = datetime.datetime.today().weekday()
    day = str(now.year) + '년 ' + str(now.month) + '월 ' + str(now.day) + '일 ' + t[r] + '요일'
    return day
    
'''


access_token = os.environ['MY_GITHUB_TOKEN']
repository_name = "chronicle" # 내 저장소 이름 필수로 바꿔야함 

g = Github(access_token)
repo = g.get_user().get_repo(repository_name)

# https://m.blog.naver.com/kiddwannabe/221811618848
# http://throughkim.kr/2016/04/01/beautifulsoup/
# https://www.kovo.co.kr/game/v-league/11210_team-ranking.asp # 남자 ?season=018&g_part=201&s_part=1 # 여자 ?season=018&g_part=201&s_part=2

req1 = requests.get('https://www.kovo.co.kr/game/v-league/11210_team-ranking.asp?season=018&g_part=201&s_part=2')
req1.encoding= None
html1 = req1.content
soup1 = BeautifulSoup(html1, "lxml")
# soup = BeautifulSoup(req.content, 'html.parser')
tables = soup1.select('#tab1 > div.wrp_lst.mt10')
print(tables)


req2 = requests.get('https://www.kovo.co.kr/main.asp')
req2.encoding= None
html2 = req2.content
soup2 = BeautifulSoup(html2, "lxml")
# soup1 = BeautifulSoup(req1.content, 'html.parser')
match1 = soup2.select('#mainWrap > article.schedule > div > div.con.l > div.sch_slider > ul.slider > li > div.match')

match2 = soup2.select('#mainWrap > article.schedule > div > div.con.r > div.sch_slider > ul.slider > li > div.match')

print(match1)
print(match2)

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

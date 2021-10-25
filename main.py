import os
import sys
import requests
import json
from bs4 import BeautifulSoup
from github import Github
from datetime import datetime
from pytz import timezone
from panadas import display, DataFrame

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('https://kleague.com/api/clubRank.do')
req.encoding= None
html = req.content
soup = BeautifulSoup(html, 'html.parser')
rank = json.loads(soup.text)

with open(os.path.join(BASE_DIR, 'rank.json'), 'w+', encoding="utf-8") as f:
    json.dump(rank, f, ensure_ascii = False, indent=2)
        
seoul_timezone = timezone('Asia/Seoul')
today = datetime.now(seoul_timezone)
today_date = today.strftime("%Y년 %m월 %d일")

access_token = os.environ['MY_GITHUB_TOKEN']
repository_name = "chronicle" # 내 저장소 이름 필수로 바꿔야함 

g = Github(access_token)
repo = g.get_user().get_repo(repository_name)

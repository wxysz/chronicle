import json,re
from urllib.request import urlopen
from html import unescape

# 웹 페이지 읽어오기
req = urlopen("http://www.hanbit.co.kr/store/books/full_book_list.html")
encoding = req.info().get_content_charset(failobj="utf-8")
html = req.read().decode(encoding)

# 파일 생성
with open("booklist.json", "w", encoding="utf-8") as f:
    data = []
    # 데이터 추출
    for partial_html in re.findall(r'<td class="left"><a.*?</td>', html, re.DOTALL):
        url = re.search(r'<a href="(.*?)">', partial_html).group(1)
        url = 'http://www.hanbit.co.kr' + url
        title = re.sub(r'<.*?>', '', partial_html)
        title = unescape(title)
        data.append({"BookName": title, "Link": url})
        # 데이터 json 형태로 출력
        print(json.dumps(data, ensure_ascii=False, indent=2))

    # 데이터 변형 및 추가
    json.dump(data, f, ensure_ascii=False, indent=2)

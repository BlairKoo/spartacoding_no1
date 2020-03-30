import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

# TODO: 제일 마지막 tr.list만 써주셔도 코드는 문제없이 실행됩니다. 그럼 title_tag, singer_tag 쪽 코드도 줄일 수 있겠죠?
songs = soup.select('#body-content>div.newest-list>div.music-list-wrap>table.list-wrap>tbody>tr.list')
rank = 0
for song in songs:
    rank += 1
    title_tag = song.select_one('td.info>a.title')
    singer_tag = song.select_one('td.info>a.artist')
    singer = singer_tag.text
    title = title_tag.text
    print(rank, title.strip(), singer.strip())



    #if title_tag is not None && singer_tag is not None:
        #singer = singer_tag.text
        #title = title_tag.text
        #print(rank, title, singer)
#############################
# (입맛에 맞게 코딩)
#############################
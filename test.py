import requests
from bs4 import BeautifulSoup
import datetime
url = 'https://www.kw.ac.kr/ko/life/notice.jsp'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
req = requests.get(url, headers=header)
html = req.text
soup = BeautifulSoup(html, "html.parser")

saved_title_list = []       #최초의 저장된 제목리스트는 빈 리스트로 가정
title_list = []
link_list = []
register_date_list = []
modified_date_list = []
new_index = []

for c in range(3):      #테스트를 위해 3번 반복
    new_title = []
    new_index = []
    new_link = []

    req = requests.get(url, headers=header)
    html = req.text
    soup = BeautifulSoup(html, "html.parser")

    dates = soup.select('p.info')
    divs = soup.select('div.board-text > a')

    for div in divs:            #제목과 링크를 얻기 위한 반복문
        title = ''.join(div.text.split())
        title_list.append(title.replace("신규게시글", '').replace("Attachment", ''))
        link_list.append(div.get('href'))

    for date in dates:          #등록일과 수정일을 얻기 위한 반복문
        register_date_list.append(date.text.split()[4])
        modified_date_list.append(date.text.split()[7])
    if c == 1:  #의도적으로 제목리스트를 변경
        title_list[1] = "가가가가가가"
    if saved_title_list != title_list:  #기존에 저장된 데이터와 비교
        for check in title_list:
            if check not in saved_title_list:
                new_index.append(title_list.index(check))
        for i in range(len(register_date_list)):
            if register_date_list[i] != modified_date_list[i]: #and modified_date_list[i] == datetime.date.today():  # 수정된 날이 다르고 현재 날짜와 다름
                new_index.append(modified_date_list.index(modified_date_list[i]))
        saved_title_list = title_list[:]
    for index in new_index: #index를 기반으로 새로운 제목과 링크를 저장
        new_title.append(title_list[index])
        new_link.append("https://www.kw.ac.kr" + link_list[index])
    print(new_title) # 3번 출력 / 1번 째 : 현재 제목리스트를 모두 출력 / 2번 째 : 새롭게 추가된 제목 출력(가가가가가) / 3번 째 : 빈 리스트 출력
    #print(new_link)
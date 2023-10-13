from bs4 import BeautifulSoup
from selenium import webdriver


def get_google_data(keyword):
    # 가져올 웹 페이지 url
    url = f'https://www.google.com/search?q={keyword}'
    
    # 크롬 브라우저가 열리고
    # 이 때, 동적인 내용(JS)들이 모두 채워진다!
    driver = webdriver.Chrome()
    driver.get(url)

    # 열린 페이지 소스를 받아옴
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # 검색 결과 가져오기
    # div 태그 안의 id가 result-stats 라는 요소를가져와보자
    results_stats = soup.select_one("div#result-stats")
    print(results_stats.text)


    # 검색 결과물의 제목들을 뽑아봅시다.
    #1. div 태그중 g class 를 가진 모든 요소 선택
    g_list = soup.select("div.g")
    for g in g_list:
        # 요소 안에 LC20lb MBeuO DKV0Md  class를 가진 특정 요소를 선택
        title = g.select_one(".LC20lb.MBeuO.DKV0Md")
        # 결측치 처리
        if title is not None:
            print(f'제목: {title.text}')





    # 파일로 저장하기
    with open('soup.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())


get_google_data('파이썬')
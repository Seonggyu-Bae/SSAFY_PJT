import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def crawling_basic():
    # 가져올 웹 페이지 url
    url = 'https://quotes.toscrape.com/'
    
    response = requests.get(url)

    # 우리가 얻고자 하는 HTML 내용이 담김
    html_text = response.text

    # HTML을 파싱이 가능한 정리된 형태로 변환
    soup = BeautifulSoup(html_text, 'html.parser')
    
    # 알아 볼 수 있도록 출력 prettify()
    #print(soup.prettify())

    # 파일로 저장하기
    with open('soup.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())

    # 크롤링 순서 : 페이지 분석 -> 검색

    # 1. 태그로 검색하기

    # 1-1 가장 첫 번째 태그에 해당하는 요소
    title = soup.find('a')
    print(f'제목 : {title.text}')
    
    # 1-2 해당 태그 모든 요소
    a_tags = soup.find_all('a')
    for idx, a in enumerate(a_tags):
        print(f'{idx} = {a.text}')


    # 2. CSS 선택자로 검색하기

    # 2-1 첫 번째로 CSS 선택자와 일치하는 요소
    sentence = soup.select_one('.text')
    author = soup.select_one('.author')
    print(f'첫 번째 글 : {sentence.text} - {author.text}')

    #2-2 CSS 선택자와 일치하는 모든 요소
    words = soup.select('.text')
    authors = soup.select('.author')
    for idx in range(len(words)):
        print(f'{words[idx].text} - {authors[idx].text}')

crawling_basic()
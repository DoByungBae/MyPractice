import requests
from bs4 import BeautifulSoup
import sys

# 기본 출력을 today.txt로 바꿈
sys.stdout = open('today.txt', 'w', encoding='utf8')

def requests_function(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
    }
    response = requests.get(url, headers=header)

    soup = BeautifulSoup(response.text, 'lxml')

    return soup

# 대구의 날씨 url
weather_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8"
weather_soup = requests_function(weather_url)

print('[오늘의 날씨]')

# 오늘의 날씨의 요약을 가져옴
summary = weather_soup.find('p', attrs={'class': 'summary'}).get_text().split()
print(summary[3], ' '.join(summary[:3]))

# 현재 온도를 가져옴
curr_temp = weather_soup.select_one('.temperature_text > strong').get_text()
print(curr_temp[:3] + curr_temp[5:], end='')

# 최저, 최고 온도를 가져옴
temp = weather_soup.select_one('.temperature_inner').get_text().split('/')
print(' (' + temp[0][:3].strip(), temp[0][5:].strip(), '/', temp[1][:3].strip(), temp[1][5:].strip() + ')')

# 강수 확률을 가져옴
rain = weather_soup.find_all('span', attrs={'class': 'rainfall'})
print(f'오전 강수 확률 {rain[0].get_text()} / 오후 강수 확률 {rain[1].get_text()}', end='\n\n')

# 미세먼지 정보를 가져옴
dust = weather_soup.select('.today_chart_list .txt')
print(f'미세먼지 : {dust[0].get_text()}')
print(f'초 미세먼지 : {dust[1].get_text()}', end='\n\n')

# 뉴스 정보
news_url = 'https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y'
news_soup = requests_function(news_url)

print('[헤드라인 뉴스]')

# 상위 뉴스를 가져옴
newses = news_soup.find_all('a', attrs={'class': 'nclicks(fls.list)'})

for i, news in enumerate(newses):
    print(f'{i+1}. {news.get_text()}')
    print(f'링크 : {news["href"]}')

# IT뉴스 정보
IT_news_url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105'
IT_news_soup = requests_function(IT_news_url)

print('\n[IT 뉴스]')

# 상위 뉴스를 가져옴
IT_newses = IT_news_soup.find_all('a', attrs={'class': 'cluster_text_headline nclicks(cls_sci.clsart)'})

for i,IT_news in zip(range(3), IT_newses):
    print(f'{i+1}. {IT_news.get_text()}')
    print(f'링크 : {IT_news["href"]}')

# 영어회화 정보
eng_url = 'https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english'
eng_soup = requests_function(eng_url)

print('\n[오늘의 영어 회화]')

# 오늘의 영어 회화를 가져옴
print('(영어 지문)')
for i in range(2, 6):
    print(eng_soup.find_all('div', attrs={'id':'conv_kor_t{}'.format(i)})[1].get_text().strip())

# 오늘의 영어 회화 한글문을 가져옴
print('\n(한글 지문)')
for i in range(2, 6):
    print(eng_soup.find_all('div', attrs={'id':'conv_kor_t{}'.format(i)})[0].get_text().strip())

sys.stdout.close()
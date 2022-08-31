from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv

# csv파일 생성
f = open('apartment.csv', 'w', encoding="utf-8-sig", newline='')
w = csv.writer(f)
w.writerow(['거래', '면적', '가격', '동', '상세 설명'])

# 아래의 함수를 사용하여 크롬 창을 열지 않고 백그라운드로 실행
option = webdriver.ChromeOptions()
option.add_argument('headless')

# 옵션에 위에서 만든 option을 추가
url = 'http://naver.com'
browser = webdriver.Chrome(options=option)
browser.get(url)

browser.find_element(By.ID, 'query').send_keys("동대구 에일린의뜰", Keys.ENTER)
url = browser.find_element(By.CLASS_NAME, 'api_more_theme').get_attribute('href')
browser.get(url)

# 해당하는 페이지의 HTML 소스를 어서 BeautifulSoup 객체로 만듬
soup = BeautifulSoup(browser.page_source, 'lxml')

browser.quit()

# 아래의 문장은 soup.find('div', attrs={'class': 'item_link'})와 같은 문장임
# 대신 select를 이용하면 아래와 같이 .price_line > .price와 같이 태그간의 이동이 유용함
datas = soup.select('.item_link')

for i,data in enumerate(datas):
    print(f'========== 매물{i} ==========')
    type = data.select('.price_line > .type')[0].string
    print(f'거래 : {type}')
    spec = data.select('.info_area .spec')
    print(f'면적 : {spec[0].string}')
    price = data.select('.price_line > .price')[0].string
    print(f"가격 : {price}")
    where = data.select('.item_title > .text')[0].string.split()[1]
    print(f"동 : {where}")
    print(f'상세 설명 : {spec[1].string}')
    w.writerow([type, spec[0].string, price, where, spec[1].string])

f.close()
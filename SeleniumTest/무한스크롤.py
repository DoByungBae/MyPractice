import time
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
from Check_Chromedriver import Check_Chromedriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)

# 설치된 Chrome 버전 확인 후 전용 Driver 자동 Download
# def set_driver(self):
#
#     if not os.path.isdir(self.driver_root_path):
#         os.makedirs(self.driver_root_path)
#
#         Check_Chromedriver.driver_mother_path = self.driver_root_path
#         Check_Chromedriver.main()
#         self.chrome_driver_path = self.driver_root_path + "chromedriver.exe"

# 웹 사이트 열기
browser.get("http://www.naver.com")
browser.implicitly_wait(10)
browser.maximize_window()

elem = browser.find_element(By.XPATH, '//*[@id="NM_FAVORITE"]/div[1]/ul[1]/li[5]/a')
elem.click()

elem = browser.find_element(By.XPATH, '//*[@id="_verticalGnbModule"]/div/div[2]/div/div[2]/div/div[2]/form/fieldset/div/input')
elem.click()

elem.send_keys('아이폰13')
elem.send_keys(Keys.RETURN)

#before_h = browser.execute_script("return window.scrollY")

# 무한 스크롤
#SCROLL_PAUSE_SEC = 1

# 스크롤 전 높이
before_h = browser.execute_script("return window.scrollY")

while True:
    # 끝까지 스크롤 다운
    #browser.find_element_by_css_selector("body").send_keys(Keys.END)
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    # 1초 대기
    time.sleep(1)

    # 스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")
    if after_h == before_h:
        break
    before_h = after_h

# 파일 생성
f = open('iphone13.csv', 'w', encoding="utf-8-sig", newline='')
csvWriter = csv.writer(f)

# 상품 정보 div
items = browser.find_elements(By.CSS_SELECTOR, '.basicList_info_area__17Xyo')
for item in items:
    name = item.find_element(By.CSS_SELECTOR, '.basicList_title__3P9Q7').text

    try:
        price = item.find_element(By.CSS_SELECTOR, '.price_num__2WUXn').text

    except:
        price = "판매중단"

    link = item.find_element(By.CSS_SELECTOR, '.basicList_title__3P9Q7 > a').get_attribute('href')
    print(name, price, link)
    csvWriter.writerow([name, price, link])

# 파일닫기
f.close()


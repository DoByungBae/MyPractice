import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)

# 대상 URL 이동
url = 'https://finance.naver.com/sise/sise_market_sum.naver?&page'
browser.get(url)
browser.maximize_window()

# 조회 항목 초기화
checkboxes = browser.find_elements(By.NAME, 'fieldIds')
for checkbox in checkboxes:
    if checkbox.is_selected(): #체크된 상태인지 확인
        checkbox.click() #클릭 체크.해제

# 조회 항목 설정
items_to_select = ['영업이익', '자산총계', '매출액']
for checkbox in checkboxes:
    parent = checkbox.find_element(By.XPATH, '..') #부모 element
    label = parent.find_element(By.TAG_NAME, 'label')
    if label.text in items_to_select: #선택항목과 일치 한다면
        checkbox.click() #체크

# 적용하기
btn_apply = browser.find_element(By.XPATH, '//a[@href="javascript:fieldSubmit()"]')
btn_apply.click()

for idx in range(1, 40): #1페이지 이상 40페이지 반복
    #사전 작업 : 페이지 이동
    browser.get(url + str(idx)) # page=2

    # 데이터추출
    df = pd.read_html(browser.page_source)[1]
    df.dropna(axis='index', how='all', inplace=True)
    df.dropna(axis='columns', how='all', inplace=True)
    if len(df) == 0:
        break
    
    # 파일 저장
    f_name = 'sise.csv'
    if os.path.exists(f_name): # 파일이 있다면 헤더 제외
        df.to_csv(f_name, encoding='utf-8-sig', index=False, mode='a')
    else:
        df.to_csv(f_name, encoding='utf-8-sig', index=False)
    print(f'{idx} 페이지완료')

browser.quit()

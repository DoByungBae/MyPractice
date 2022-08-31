from cmath import exp
from importlib.resources import path
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utilies import excelUtl

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)

# 대상 URL 이동
browser.get("https://demo.opencart.com/")

# 로그인 페이지 진입
elem = browser.find_element(By.XPATH, '//*[@id="top"]/div[2]/div[2]/ul/li[2]/div/a/span')
elem.click()
elem = browser.find_element(By.XPATH, '//*[@id="top"]/div[2]/div[2]/ul/li[2]/div/ul/li[2]/a')
elem.click()

# step1 : 로그인 페이지 진입 판정
step1 = browser.title
print('This Page Title name :' + step1)
if step1 == "Account Login":
    assert True
    print("[STEP1] : PASS")
else:
    assert False
    print("[STEP1] : Fail")

# 엑셀파일의 경로 지정, 경로는 역슬래시 2개를 넣어줘야함
path = '../../pythonWorkSpace/test.xlsx'

# Test data의 행숫자를 가져옴
rows = excelUtl.getRowCount(path, 'Sheet1')

# print(rows)

# 판정결과를 저장할 빈 리스트 지정
lst_status = []

# # ID, PW 변수 지정
# userName = 'somethingmat@naver.com'
# pw = 'ehqud1208!'

for r in range(2, rows + 1):
    # 엑셀에서 email과 pw를 가져옴
    userName = excelUtl.readData(path, 'Sheet1', r, 1)
    pw = excelUtl.readData(path, 'Sheet1', r, 2)
    exp = excelUtl.readData(path, 'Sheet1', r, 3)

    # 1초 쉼
    time.sleep(1)

    # ID 필드를 찾아서 변수를 입력
    elem = browser.find_element(By.XPATH, '//*[@id="input-email"]')
    elem.send_keys(userName)

    # 1초 쉼
    time.sleep(1)

    # PW 필드를 찾아서 PW 입력
    elem = browser.find_element(By.XPATH, '//*[@id="input-password"]')
    elem.send_keys(pw)

    # 1초 쉼
    time.sleep(1)

    # 로그인 버튼 클릭
    elem = browser.find_element(By.CSS_SELECTOR, '#form-login > button')
    elem.click()

    # 1초 쉼
    time.sleep(1)

    # Step2에 현재 타이틀값을 저장
    step2 = browser.title
    # 정상값을 저장
    act_title = "My Account"

    # step2 로그인 성공 여부 판정
    if step2 == act_title:
        if exp == "Pass":
            lst_status.append("Pass")
            print("   [STEP2-", r - 1, "]: Pass")
            browser.find_element(By.XPATH, '//*[@id="top"]/div[2]/div[2]/ul/li[2]/div/a/span').click()
            browser.find_element(By.XPATH, '//*[@id="top"]/div[2]/div[2]/ul/li[2]/div/a/span').click()
            browser.find_element(By.XPATH, '//*[@id="top"]/div[2]/div[2]/ul/li[2]/div/a/span').click()
        elif exp == "Fail":
            lst_status.append("Fail")
            print("   [STEP2-", r - 1, "]: Fail")
            browser.find_element(By.XPATH, '//*[@id="top"]/div[2]/div[2]/ul/li[2]/div/a/span').click()
            browser.find_element(By.XPATH, '//*[@id="top"]/div[2]/div[2]/ul/li[2]/div/a/span').click()
            browser.find_element(By.XPATH, '//*[@id="top"]/div[2]/div[2]/ul/li[2]/div/a/span').click()

    elif step2 != act_title:
        if exp == "Pass":
            lst_status.append("Fail")
            print("   [STEP2-", r - 1, "]: Fail")
            browser.find_element(By.XPATH, '//*[@id="top"]/div[2]/div[2]/ul/li[2]/div/a/span').click()
        elif exp == "Fail":
            lst_status.append("Pass")
            print("   [STEP2-", r - 1, "]: Pass")
            browser.find_element(By.XPATH, '//*[@id="top"]/div[2]/div[2]/ul/li[2]/div/a/span').click()


if "Fail" not in lst_status:
    print("[STEP2] : PASS")
else:
    print("[STEP2] : Fail")

# step2 = browser.title
# print('This Page Title name : ' + step2)
# if step2 == "My Account":
#     assert True
#     print("[STEP2] : PASS")
# else:
#     assert False
#     print("[STEP2] : Fail")

# web browser 닫음
browser.close()

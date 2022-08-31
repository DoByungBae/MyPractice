import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilies import excelUtl
import pytest

def test_login():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = webdriver.Chrome(options=options)

    # 대상 URL 이동
    browser.get("https://www.opencart.com")
    browser.maximize_window()

    browser.find_element(By.XPATH, '//*[@id="navbar-collapse-header"]/div/a[1]').click()


    # 로그인 페이지 진입 판정
    # step1 : 로그인 페이지 진입 판정
    step1 = browser.title
    print('This Page Title name :' + step1)
    if step1 == "OpenCart - Account Login":
        assert True
        print("[STEP1] : PASS")
    else:
        assert False
        print("[STEP1] : Fail")

    # 엑셀파일의 경로 지정, 경로는 역슬래시 2개를 넣어줘야함
    path = '..\\pythonWorkSpace\\test.xlsx'

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
        browser.find_element(By.XPATH, '//*[@id="input-email"]').send_keys(userName)

        # 1초 쉼
        time.sleep(1)

        # PW 필드를 찾아서 PW 입력
        browser.find_element(By.XPATH, '//*[@id="input-password"]').send_keys(pw)

        # 1초 쉼
        time.sleep(1)

        # 로그인 버튼 클릭
        browser.find_element(By.XPATH, '//*[@id="account-login"]/div[2]/div/div[1]/form/div[3]/div[1]/button[1]').click()

        # 1초 쉼
        time.sleep(1)

        # 핀코드
        step3 = browser.title
        act_title2 = "Account PIN"
        if step3 == act_title2:
            browser.find_element(By.XPATH, '//*[@id="input-pin"]').send_keys(1208)
            browser.find_element(By.XPATH, '//*[@id="account-security"]/div[2]/div/div[1]/form/div[2]/button').click()
        elif step3 != act_title2:
            browser.find_element(By.XPATH, '//*[@id="navbar-collapse-header"]/div/a[1]').click()

        # Step2에 현재 타이틀값을 저장
        step2 = browser.title
        # 정상값을 저장
        act_title = "OpenCart - Your Account"

        # step2 로그인 성공 여부 판정
        if step2 == act_title:
            if exp == "Pass":
                lst_status.append("Pass")
                print("   [STEP2-", r - 1, "]: Pass")
                browser.find_element(By.XPATH, '//*[@id="navbar-collapse-header"]/div/a[2]').click()
                browser.find_element(By.XPATH, '//*[@id="navbar-collapse-header"]/div/a[1]').click()

            elif exp == "Fail":
                lst_status.append("Fail")
                print("   [STEP2-", r - 1, "]: Fail")
                browser.find_element(By.XPATH, '//*[@id="navbar-collapse-header"]/div/a[2]').click()
                browser.find_element(By.XPATH, '//*[@id="navbar-collapse-header"]/div/a[1]').click()

        elif step2 != act_title:
            if exp == "Pass":
                lst_status.append("Fail")
                print("   [STEP2-", r - 1, "]: Fail")
                browser.find_element(By.XPATH, '//*[@id="navbar-collapse-header"]/div/a[1]').click()
            elif exp == "Fail":
                lst_status.append("Pass")
                print("   [STEP2-", r - 1, "]: Pass")
                browser.find_element(By.XPATH, '//*[@id="navbar-collapse-header"]/div/a[1]').click()


    if "Fail" not in lst_status:
        assert True
        print("[STEP2] : PASS")
    else:
        assert False
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



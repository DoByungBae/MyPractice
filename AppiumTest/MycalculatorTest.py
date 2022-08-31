from configuration import AppiumTest
from utilies import excelUtl
from appium.webdriver.common.appiumby import By

file_path = '..\\testdata\\data.xlsx'
N = excelUtl.getRowCount(file_path, 'Sheet1')
wd = AppiumTest.cal()

for i in range(2, N+1):
    first = excelUtl.readData(file_path, 'Sheet1', i, 2)
    second = excelUtl.readData(file_path, 'Sheet1', i, 5)
    op = excelUtl.readData(file_path, 'Sheet1', i, 4)
    result = excelUtl.readData(file_path, 'Sheet1', i, 6)

    wd.find_element(By.XPATH, f'//android.widget.Button[@content-desc="{first}"]').click()
    wd.find_element(By.XPATH, f'//android.widget.Button[@content-desc="{op}"]').click()
    wd.find_element(By.XPATH, f'//android.widget.Button[@content-desc="{second}"]').click()
    wd.find_element(By.XPATH, '//android.widget.Button[@content-desc="계산"]').click()

    #result = excelUtl.readData(file_path, 'Sheet1', 2, 6)

    cal_result = float(wd.find_element(By.ID, 'com.sec.android.app.popupcalculator:id/calc_edt_formula').text)

    if result == cal_result:
        print("TEST[i-1} : PASS")

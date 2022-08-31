from appium.webdriver.common.appiumby import By

from configuration import AppiumTest
from appium.webdriver.common.touch_action import TouchAction
import time


wd = AppiumTest.cal()

action = TouchAction(wd)
action.tap(x=215, y=1995).perform()

# tap
action = TouchAction(wd)
# action.tap(x=215, y=1995).perform()
# action.tap(x=215, y=1995).perform()
# action.tap(x=215, y=1995).perform()
#
# action.press(x=700, y=700).move_to(x=700, y=1400).release().perform()

# for i in range(7, 17):
#     wd.press_keycode(i)

wd.find_element(By.XPATH, '//android.widget.Button[@content-desc="1"]').click()
wd.find_element(By.XPATH, '//android.widget.Button[@content-desc="더하기"]').click()
wd.find_element(By.XPATH, '//android.widget.Button[@content-desc="2"]').click()
wd.find_element(By.XPATH, '//android.widget.Button[@content-desc="계산"]').click()



from appium import webdriver

desired_cap = {
  "appium:deviceName": "R3CR70AR4LZ",
  "platformName": "Android",
  "appium:appPackage": "com.sec.android.app.popupcalculator",
  "appium:appActivity": "com.sec.android.app.popupcalculator.Calculator"
}

def cal():
  wd = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
  wd.implicitly_wait(10)
  return wd

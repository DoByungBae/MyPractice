from appium import webdriver

desired_cap = {
  "appium:deviceName": "R3CR70AR4LZ",
  "platformName": "Android",
  "appium:appPackage": "com.elevenst",
  "appium:appActivity": "com.elevenst.intro.Intro"
}

def cal():
  wd = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
  wd.implicitly_wait(10)
  return wd
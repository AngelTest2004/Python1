
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

path = r'C:\Users\AnqiLi\Documents\tool\geckodriver\geckodriver.exe' # c:\users\user\desktop\test
firefox_driver_path = str(path)
print(firefox_driver_path)
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False
driver = webdriver.Firefox(capabilities=cap,executable_path=firefox_driver_path)
driver.get("https://www.yahoo.co.jp/")

if __name__ == '__main__':
    testChrome().setUp()
    time.sleep(5)
    testChrome().tearDown()
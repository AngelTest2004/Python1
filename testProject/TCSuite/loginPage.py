from testProject.BaseMethod.webTest import webChromeTest
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class loginPageTest(webChromeTest):
  def setUp(cls):
    webChromeTest.setUp()

  def tearDown(cls):
    webChromeTest.tearDown()

  def negativeCase(cls):
      #toMailPageXpath="/html/body/div/div/header/div[2]/div[1]/ul/li[3]/a"
      toMailPageXpath="/html/body/div[1]/header/nav/div[1]/div/ul/li[2]/a"
      webChromeTest.clickButton(cls,toMailPageXpath)
      mailItemxpath="/html/body/div[1]/div[2]/div/div[2]/div[1]/div/div/fieldset/form/div/div[1]/div[3]/dl/dd/input"
      value="a"
      webChromeTest.setValueByxpath(cls,mailItemxpath,value)
      buttonXpath="/html/body/div[1]/div[2]/div/div[2]/div[1]/div/div/fieldset/form/div/div[1]/div[3]/div/button"
      webChromeTest.clickButton(cls,buttonXpath)
      #driver = webChromeTest.browser



if __name__ == '__main__':
    loginPageTest().setUp()
    time.sleep(2)
    loginPageTest().negativeCase()

    time.sleep(2)
    loginPageTest().tearDown()


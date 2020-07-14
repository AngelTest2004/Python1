from selenium import webdriver
import configparser
from time import strftime,gmtime
import os

class webChromeTest():
 global browser
 global homeLink
 global chromedriver_path
 global TC_Col,SP_Col,AC_Col,Xp_Col,IV_Col,IVLen_Col,ER_ColM,AR_Col

 @classmethod
 def getConf(cls):
     conf = configparser.ConfigParser()
     configPath=os.path.abspath(os.path.dirname(os.getcwd()))+"\\BaseMethod\\configuration"
     conf.read(configPath)
     cls.homeLink = conf.get("BASE", "HOMEPAGE")
     cls.chromedriver_path = conf.get("BASE", "CHROMEDRIVER")
     cls.TC_Col=conf.get("TC", "TC_NM")
     cls.SP_Col = conf.get("TC", "Sp_NM")
     cls.AC_Col = conf.get("TC", "AC_NM")
     cls.Xp_Col = conf.get("TC", "Xp_NM")
     cls.IV_Col=conf.get("TC", "IV_NM")
     cls.IVLen_Col = conf.get("TC", "IVLEN_NM")
     cls.ER_ColM=conf.get("TC", "ER_NM")
     cls.AR_Col=conf.get("TC", "AR_NM")



 @classmethod
 def setUp(cls):
     cls.getConf()
     cls.browser = webdriver.Chrome(executable_path=cls.chromedriver_path)
     cls.browser.get(cls.homeLink)
     cls.browser.implicitly_wait(3)
 @classmethod
 def tearDown(cls):
     cls.browser.close()

 # def testCase(cls):
 #     cls.browser.find_element_by_xpath("/html/body/div/div/header/div[2]/div[1]/ul/li[3]/a").click()

 def setValueByxpath(cls,xpath,value):
     objectItem=cls.browser.find_element_by_xpath(xpath)
     objectItem.send_keys("value")

 def clickButton(cls,xpath):
     objectItem=cls.browser.find_element_by_xpath(xpath).click()

 def runTC(self,actKey,itemXpath,value,expResult,actResult):
     if actKey.strip()== "1":
         self.setUp()
 def getRandomValue(self,length):
     value=strftime("%Y%m%d%H%M%S", gmtime())
     local_len=int((length))

     if len(value)>=local_len:
         print(value[0:local_len])
         return int(value[0:local_len])
     else:
         for i in (local_len-int(len(value))):
             value=value+'0'
         return value
 def runTC2(self,data):
     self.setUp()


     i=0
     while i <= len(data.columns):

         ac_value=data.iat[i,int(self.AC_Col)]
         xp_value = data.iat[i, int(self.Xp_Col)]
         iv_value = data.iat[i, int(self.IV_Col)]
         ivlen_value = data.iat[i, int(self.IVLen_Col)]
         er_value = data.iat[i, int(self.ER_ColM)]

         if iv_value=='Random':
             iv_value=self.getRandomValue(ivlen_value)

         if ac_value.strip() == 'click':
             self.clickButton(xp_value)
         elif ac_value.strip() == 'input':
             self.setValueByxpath(xp_value,iv_value)

         i=i+1

# if __name__ == '__main__':
#     chromeTest().setUp()
#     time.sleep(5)
# ''''''
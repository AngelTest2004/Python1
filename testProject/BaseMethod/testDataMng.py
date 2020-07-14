from testProject.BaseMethod.webTest import webChromeTest
import xlrd
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

class testDataMng():
 global data_xls

 def openDataFile(self,filePath):
     self.data_xls = pd.read_excel(filePath,sheet_name=None)

 def runTC(self,filePath):
     self.openDataFile(filePath)
     for i in self.data_xls.sheet_names:
         file=pd.read_excel(filePath,sheet_name=i)
         fileRow=file.shape[0]
         m=2
         while m < fileRow:

             pass
             # n = m + 1
             # while n <fileRow:
             #     if file["TC"][m]== file["TC"][n]:
             #         n=n+1
             #     else:
             #         break
             # while m< (n-1) :
             #
             #     stepID=file["Step"][m]
             #     actKey=file["Action"][m]
             #     itemXpath=file["ItemXpath"][m]
             #     value = file["Value"][m]
             #     expResult = file["ExpectedResult"][m]
             #     actResult = file["ActualResult"][m]
             #     # run test with above value
             #     webChromeTest().runTest(actKey,itemXpath,value,expResult,actResult)
             #     m=m+1

 def runTC1(self,filePath):
     self.openDataFile(filePath)
     for i in self.data_xls.keys():
         file = pd.read_excel(filePath, sheet_name=i)
         for j in file['TC'].unique():
             data=file.loc[file['TC']==j]
             webChromeTest().runTC2(data)

if __name__ == '__main__':
    filePath="C:\\Users\\AnqiLi\\Documents\\testData.xlsx"
    testDataMng().runTC1(filePath)
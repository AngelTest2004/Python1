
import time
import os
import json

class readJson():

 def __init__(self,filePath,noteName):
     with open(filePath, 'r') as jsonfile:
         json_string = json.load(jsonfile)
         for element in json_string['noteName']:
             json_string



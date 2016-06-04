# -*- coding: utf-8 -*-
"""
Created on Fri May 27 16:55:47 2016

@author: kia
"""

#JSON to CSV Converter

stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
import json
jsonDataAsPythonValue = json.loads(stringOfJsonData)
jsonDataAsPythonValue


#Address of JSON file
jfile_path ='/home/kia/workspace/Python_Kia/JSONtoCSV/page_country_simple.json'

f = open(jfile_path, 'r')
#f.read()
jsonDataAsPythonValue = json.loads(f.read())
f.close()
jsonDataAsPythonValue

lis1 =[]
for line in jsonDataAsPythonValue:
    lis1.append(line)

print(jsonDataAsPythonValue['period'])
print(jsonDataAsPythonValue['values']['value'])
print(jsonDataAsPythonValue['values']['value']['US'])


jfile_path ='/home/kia/workspace/Python_Kia/JSONtoCSV/page_country.json'

f = open(jfile_path, 'r')
#f.read()
jsonDataAsPythonValue = json.loads(f.read())
f.close()
jsonDataAsPythonValue

lis1 =[]
for line in jsonDataAsPythonValue:
    lis1.append(line)

print(jsonDataAsPythonValue['data_page_fans_country'][0]['period'])
print(jsonDataAsPythonValue['data_page_fans_country'][0]['values'][0]['value']['US'])
print(jsonDataAsPythonValue['data_page_fans_country'][0]['values'][1]['value']['US'])
print(jsonDataAsPythonValue['data_page_fans_country'][0]['values'][0]['end_time'])

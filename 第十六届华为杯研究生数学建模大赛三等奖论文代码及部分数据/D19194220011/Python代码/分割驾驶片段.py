# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:29:45 2019

@author: dell
"""

import pandas as pd

filePath = "C:/Users/dell/.spyder-py3/"
savePath = "C:/Users/dell/.spyder-py3/3/"

data = pd.read_excel(filePath+"文件3+距离+加时间+丢失补全.xlsx", header=None)
head = data[:1]

dataNum = 193302
start = 1
index = 0

for i in range(1, dataNum):
    if data[1][i] > 1:
        
        newData = data[start:i]
        start = i
        newData = head.append(newData, ignore_index=True)
        newData[1][1] = 1
        newData.to_excel(savePath+"3-"+str(index)+".xlsx", index=None, header=None)
        index = index + 1
        
newData = data[start:dataNum]
newData = head.append(newData, ignore_index=True)
newData[1][1] = 1
newData.to_excel(savePath+"3-"+str(index)+".xlsx", index=None, header=None)
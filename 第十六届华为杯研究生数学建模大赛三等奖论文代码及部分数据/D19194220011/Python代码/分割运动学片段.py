# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 16:21:45 2019

@author: dell
"""

import pandas as pd

filePath = "C:/Users/dell/.spyder-py3/预处理完毕2.0/3/"
savePath = "C:/Users/dell/.spyder-py3/3/"

fileNum = 68


cnt = 2450
for i in range(fileNum):
    data = pd.read_excel(filePath+"3-"+str(i)+".xlsx", header=None)
    start = False
    end = False
    startIndex = 1
    endIndex = 0
    flag = False
    for j in range(1, len(data[0])-5):
        if data[2][j] == 0 and flag:
            continue
        elif flag:
            flag = False
       
            
        elif data[2][j] == 0 and sum(data[2][m] for m in range(j, j+5)) == 0 and flag==False:
            
            endIndex = j
            newData = data[startIndex:endIndex]
            newData.to_excel(savePath+str(cnt)+".xlsx", index=None, header=None)
            flag = True
            startIndex = endIndex
            cnt += 1
            
    if startIndex < (len(data[0])-10):
        newData = data[startIndex:]
        newData.to_excel(savePath+str(cnt)+".xlsx", index=None, header=None)
        

            
            
            
            
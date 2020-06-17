# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:44:38 2019

@author: dell
"""

import pandas as pd
import re

filePath = "C:/Users/dell/.spyder-py3/"

data = pd.read_excel(filePath+"文件3_加距离.xlsx", header=None)


prev = 0
cur = 19*3600 + 43*60 + 57

for i in range(2, 164915):
    prev = cur
    
    year,month,day,hour,minute,sec = map(int, re.split("[/ :.]", data[0][i])[:-2])
        
    cur = (day-1)*86400 + hour*3600 + minute*60 + sec
    data[1][i] = cur - prev
    print(i)
    
data.to_excel("文件3+距离+时间差.xlsx", index=None, header=None)
    
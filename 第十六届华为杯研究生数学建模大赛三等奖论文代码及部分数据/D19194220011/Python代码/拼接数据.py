# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 22:17:10 2019

@author: dell
"""

import pandas as pd

filePath = "C:/Users/dell/.spyder-py3/所有片段按顺序/"

ret = pd.DataFrame()

for i in range(1, 2949):
    data = pd.read_excel(filePath+str(i)+".xlsx", header=None)
    ret = ret.append(data, ignore_index=True)
    
ret.to_excel("拼接数据.xlsx", index=None, header=None)
    
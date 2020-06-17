# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:44:38 2019

@author: dell
my_df = pd.DataFrame(a)

my_df.to_csv('my_csv.csv', index=False, header=False)
"""

import pandas as pd
import re
import os


filePath = "C:/Users/dell/Desktop/所有片段按顺序/"
paths = [i for i in os.listdir(filePath)]
f=[]
aaa=0
for path in paths:
    data = pd.read_excel(filePath+path, header=None)
    speed = []
    for i in range(0,len(data[2])):
        speed.append(data[2][i])
    speed.sort()
    mid = speed[int(len(speed)/2)]
    f.append(mid)

    aaa+=1
    print(aaa)
f = pd.DataFrame(f)
f.to_excel("C:/Users/dell/Desktop/save/" + '13速度中位数.xlsx', index=None, header=None)

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:44:38 2019

@author: dell
"""

import pandas as pd
import re
import os


filePath = "C:/Users/dell/Desktop/运动片段2.0/3/"
paths = [i for i in os.listdir(filePath)]
aaa=0
for path in paths:
    data = pd.read_excel(filePath+path, header=None)

    c = 0
    start = 0
    f = False
    for i in range(1,len(data[2])):
        if i == len(data[2]) - 1:
            if c >= 20:
                data[2][start : start + c] = 0
            c = 0
            f = False
        if data[2][i]>0 and data[2][i]<=10:
            if f == False:
                start = i
                f = True
            c +=1
        else:
            if c >= 20:
                data[2][start : start + c] = 0
            c = 0
            f = False

    #data.to_excel("C:/Users/dell/Desktop/save/" + path, index=None, header=None)
    aaa+=1
    print(aaa)

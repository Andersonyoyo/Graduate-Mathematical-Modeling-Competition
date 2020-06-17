# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:44:38 2019

@author: dell
"""
import os
import pandas as pd
import re

filePath = "C:/Users/dell/Desktop/3删怠速/"
paths = [i for i in os.listdir(filePath)]
aaa=0
d_n=0
for path in paths:
    data = pd.read_excel(filePath+path, header=None)
    for i in range(1,len(data[17])):
        if data[17][i] >= 4:
            data[17][i] = 3.96
            d_n+=1
        if data[17][i] < -7.5:
            data[17][i] = -7.5
            d_n+=1
    data.to_excel("C:/Users/dell/Desktop/save3/" + path, index=None, header=None)
    aaa+=1
    print(aaa)
print('修改了',d_n,'条')

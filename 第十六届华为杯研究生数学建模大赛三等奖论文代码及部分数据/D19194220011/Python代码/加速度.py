# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:44:38 2019

@author: dell
"""
import os
import pandas as pd
import re

filePath = "C:/Users/dell/Desktop/3加怠速/"
paths = [i for i in os.listdir(filePath)]
aaa=0
for path in paths:
    data = pd.read_excel(filePath+path, header=None)
    data=pd.concat([data,pd.DataFrame(columns=list('1'))])
    data['1'][0] = '加速度'
    for i in range(1,len(data[2])-1):
        data['1'][i] = (data[2][i+1] - data[2][i])/3.6
    data.to_excel("C:/Users/dell/Desktop/save3/" + path, index=None, header=None)
    aaa+=1
    print(aaa)

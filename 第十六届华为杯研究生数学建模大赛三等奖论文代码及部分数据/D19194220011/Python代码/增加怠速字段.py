# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:44:38 2019

@author: dell
"""
import os
import pandas as pd
import re

filePath = "C:/Users/dell/Desktop/3低速置0/"
paths = [i for i in os.listdir(filePath)]
aaa=0
for path in paths:
    data = pd.read_excel(filePath+path, header=None)
    data=pd.concat([data,pd.DataFrame(columns=list('1'))])
    data['1'][0] = '怠速状态'
    for i in range(1,len(data[2])):
        if data[2][i] == 0:
            data['1'][i] = 1
        else:
            data['1'][i] = 0
        #1为怠速状态  0为非怠速状态

    data.to_excel("C:/Users/dell/Desktop/save/" + path, index=None, header=None)
    aaa+=1
    print(aaa)

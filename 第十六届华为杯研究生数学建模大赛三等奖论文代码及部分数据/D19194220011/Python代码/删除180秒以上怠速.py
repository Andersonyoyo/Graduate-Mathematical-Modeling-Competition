# -*- coding: utf-8 -*-
"""
data=pd.concat([data,pd.DataFrame(columns=list('2'))])
"""
import os
import pandas as pd
import re

filePath = "C:/Users/dell/Desktop/2加速度/"
paths = [i for i in os.listdir(filePath)]
aaa=0
d_n=0
for path in paths:
    data = pd.read_excel(filePath+path, header=None)
    c = 0
    start = 0
    f = False
    index = []
    for i in range(1,len(data[16])):

        if data[16][i]==1:
            if f == False:
                start = i
                f = True
            c +=1
        else:
            if c >= 180:
                for j in range(start+180, start+c):
                    index.append(j)
            c = 0
            f = False
        if i == len(data[16]) - 1:
            if c >= 180:
                for j in range(start+180, start+c):
                    index.append(j)
            c = 0
            f = False

    for i in index:
        data=data.drop(i)
        d_n+=1

    data.to_excel("C:/Users/dell/Desktop/save2/" + path, index=None, header=None)
    aaa+=1
    print(aaa)
    print('删除了：',d_n)
print(d_n)

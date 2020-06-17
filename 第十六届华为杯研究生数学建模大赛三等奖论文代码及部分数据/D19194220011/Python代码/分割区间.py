# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 09:09:29 2019

@author: dell
"""

import pandas as pd

filePath = "C:/Users/dell/.spyder-py3/"

'''data = pd.read_excel(filePath+"文件1+距离+时间差.xlsx", header=None)'''

sepPos = []

for i in range(2, 185726):
    timeInterval = data[1][i]
    if timeInterval > 3600 and data[8][i] < (0.15*timeInterval):
        sepPos.append(i)
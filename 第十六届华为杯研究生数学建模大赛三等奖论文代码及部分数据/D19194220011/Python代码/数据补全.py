# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 21:52:49 2019

@author: dell
"""

import pandas as pd
import re
import math
from datetime import *

def e_insert(last_speed, next_speed, time_perd):
    """
    :param last_speed:断点前速度
    :param next_speed:断点后速度
    :param time_perd:间断时间/s
    :return:
    """
    if last_speed <= next_speed:
        b = last_speed
        a = math.log(next_speed-last_speed+0.0001)/time_perd
        for i in range(time_perd-1):
            yield i, (math.exp((i+1)*a)+b)

    if last_speed > next_speed:
        b = last_speed
        a = math.log(last_speed - next_speed+0.0001) / time_perd
        for i in range(time_perd-1):
            yield i, (-math.exp((i+1)*a)+b)

def lin_insert(last_speed, next_speed, time_perd):
    """
    :param last_speed:断点前速度
    :param next_speed:断点后速度
    :param time_perd:间断时间/s
    :return:
    """
    b = last_speed
    a = (next_speed - last_speed)/time_perd
    for i in range(time_perd-1):
        yield i, (a*i+b)



filePath = "C:/Users/dell/.spyder-py3/"

data = pd.read_excel(filePath+"文件3+距离+时间差.xlsx", header=None)

for i in range(2, 164915):
    timeItv = data[1][i]
    speed = data[8][i]/timeItv
    if (1 < timeItv < 181) or (timeItv > 180 and speed >1):
        misData = [ [0 for i in range(16)] for j in range(timeItv-1) ]
        
        startTime = data[0][i-1]
        year,month,day,hour,minute,sec = map(int, re.split("[/ :.]", startTime)[:-2])
        startTime = datetime(year,month,day,hour,minute,sec)
        
        
        '''添加时间'''
        for row in range(timeItv-1):
            startTime = startTime + timedelta(seconds=1)
            year = startTime.date().year
            month = startTime.date().month
            day = startTime.date().day
            hour = startTime.time().hour
            minute = startTime.time().minute
            sec = startTime.time().second
            
            time = "{}/{:0>2}/{:0>2} {:0>2}:{:0>2}:{:0>2}.000.".format(year,month,day,hour,minute,sec)
            misData[row][0] = time
        
        '''添加时间差'''
        for row in range(timeItv-1):
            misData[row][1] = 1
        data[1][i] = 1    
        
        
        '''速度'''
        for row, speed in e_insert(data[2][i-1], data[2][i], timeItv):
            misData[row][2] = speed
        
        
        '''后13列参数'''
        for col in range(3, 16):
              for row, value in lin_insert(data[col][i-1], data[col][i], timeItv):
                  misData[row][col] = value
              
        misData = pd.DataFrame(misData)
        data = data.append(misData, ignore_index=True)
    '''print(i)'''
    
data.to_excel("文件3+距离+加时间+丢失补全.xlsx", index=None, header=None)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
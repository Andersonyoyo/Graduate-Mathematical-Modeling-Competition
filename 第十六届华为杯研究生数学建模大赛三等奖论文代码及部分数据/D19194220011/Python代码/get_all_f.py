import pandas as pd
import re
import os

#path = r'C:\Users\dell\Desktop\拼接数据.xlsx'
path = r'C:\Users\dell\Desktop\分类数4\拼接4.xlsx'
data = pd.read_excel(path, header=None)
speed_avg = 0       #平均速度        1  29.98
speed_run_avg = 0   #平均行驶速度    2   38.92
temp1 = 0
a_up_avg = 0        #平均加速度      3   0.315
temp2 = 0
a_down_avg = 0      #平均减速度      4   -0.364
temp3 = 0
speed0_ratio = 0    #怠速比          5   0.23
a_up_ratio = 0      #加速比          6    0.38

a_down_ratio = 0    #减速比          7   0.34
speed_s = 0         #速度标准差      8   26.468
a_s = 0             #加速度标准差    9   0.4
speed_max = 0



l = len(data)
for i in range(0,len(data)):
    speed_avg += data[2][i]
    if data[2][i] > 0:
        speed_run_avg += data[2][i]
        temp1 += 1

    if data[2][i] > speed_max:
        speed_max = data[2][i]

    if data[17][i] > 0:
        a_up_avg += data[17][i]
        temp2 += 1
        a_up_ratio += 1

    if data[17][i] < 0:
        a_down_avg += data[17][i]
        temp3 += 1
        a_down_ratio += 1

    if data[2][i] == 0:
        speed0_ratio += 1

speed_avg = speed_avg/l
speed_run_avg = speed_run_avg/temp1
a_up_avg = a_up_avg/temp2
a_down_avg =a_down_avg/temp3
a_up_ratio = a_up_ratio/l
a_down_ratio = a_down_ratio/l
speed0_ratio = speed0_ratio/l
ss = 0
sss = 0
nnn = 0
for i in range(0,len(data)):
    ss += (data[2][i]-speed_avg)**2
    if data[17][i] > 0:
        sss += (data[17][i] - a_up_avg) ** 2
speed_s = (ss/len(data))**0.5
a_s = (sss/temp2)**0.5
print('平均速度：', speed_avg)
print('平均行驶速度:', speed_run_avg)
print('平均加速度', a_up_avg)
print('平均减速度', a_down_avg)
print('怠速比', speed0_ratio)
print('加速比', a_up_ratio)
print('减速比', a_down_ratio)
print('速度标准差', speed_s)
print('加速度标准差', a_s)

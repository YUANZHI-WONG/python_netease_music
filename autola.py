# -*- coding=utf-8 -*-
import random
import matplotlib.pyplot as plt
from pylab import mpl
import csv

plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号

x = [] 
y = [] 

with open('test.csv') as f:
    f_csv=csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        try:
            i=row[0].split(";")[0][1:-2].split(",")[1]
            if i.count(".") == 1 and not i.startswith(".") and not i.endswith("."):
                x.append(i)
        except:
            print(0)

save_path='y.txt'

for line in x:
    with open(save_path, 'a', encoding='utf-8') as f: 
        f.write(line+'\n') 

# -*- coding=utf-8 -*-
import random
import matplotlib.pyplot as plt
from pylab import mpl
import csv

plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号

x = [] 
y = [] 
ix=0
iy=0
item=16520
with open('x.csv') as f:
    f_csv=csv.reader(f)
    
    for row in f_csv:
        try:
            if ix <item:
                x.append(float(row[0][0:-2]))
                ix=ix+1
        except:
            print(0)


with open('y.csv') as fy:
    fy_csv=csv.reader(fy)
    
    for row in fy_csv:
        try:
            if iy <item:
                y.append(float(row[0][0:-2]))
                iy=iy+1
        except:
            print(0)


#设置图信息
fig=plt.figure()


ax=plt.Axes(fig,[0.04, 0.025,0.95,0.92])
ax.set_xlim(2.5,10)
ax.set_ylim(-2.5,5)
#设置地图


x1=[3,6]
y1=[0,-2]

x2=[6,9]
y2=[-2,2]

x3=[9,3]
y3=[2,0]


ax.plot(x,y,linewidth=2,linestyle='-',color='blue')

ax.plot(x1,y1,linewidth=2,linestyle='-',color='red')
ax.plot(x2,y2,linewidth=2,linestyle='-',color='red')
ax.plot(x3,y3,linewidth=2,linestyle='-',color='red')

fig.add_axes(ax)
plt.show()




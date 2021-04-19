import matplotlib.pyplot as plt
import numpy as np
import scipy.signal


x = np.arange(0,105,5)


y2=[1.00,
2.36 ,
0.78,
1.21 ,
0.37 ,
1.00 ,
0.92 ,
0.28 ,
0.77 ,
1.09 ,
0.89 ,
0.32 ,
0.73 ,
0.93 ,
0.22 ,
1.16 ,
0.74 ,
0.67 ,
0.83 ,
1.25 ,
1.5
 ]

y3=[
1.28 ,
2.36 ,
0.78 ,
1.24 ,
0.69 ,
1.12 ,
1.61 ,
0.57 ,
0.91 ,
1.23 ,
1.31 ,
0.64 ,
0.89 ,
1.02 ,
0.63 ,
1.21 ,
1.36 ,
1.19 ,
1.68 ,
1.25 ,
1.5
]

fig, ax1 = plt.subplots()
l1, =ax1.plot(x,y3,linestyle = '-', # 折线类型
         linewidth = 1, # 折线宽度
         color = 'steelblue', # 折线颜色
         #marker = 'o', # 点的形状
         markersize = 2, # 点的大小
         markeredgecolor='black', # 点的边框色
         markerfacecolor='steelblue') # 点的填充色



xtick = np.arange(start=0, stop=120, step=10) 
x_ticks_label=['0','2min', "4min","6min" ,"8min","10min","12min","14min","16min","18min","20min",' ']

#ax1_y_label=np.arange(start=0, stop=100, step=10)/100

ax1.set_xticks(xtick)
ax1.set_xticklabels(x_ticks_label)
#ax1.set_ylabel(ax1_y_label)


ax1.set_xlabel("time")
ax1.set_ylabel("Average minimum distance between pedestrians",color='g')


# 设置图例
#plt.legend(handles=[l1,l2,l3,],labels=['s_dq_pctchange','s_dq_volume','1234'],loc='best')

plt.show()
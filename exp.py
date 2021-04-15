import matplotlib.pyplot as plt
import numpy as np
import scipy.signal


x = np.arange(0,100,5)


y1=[0.4181818, 
 0.10723301,
 0.09172121, 
 0.18837228, 
 0.61206671, 
 0.48093   , 
 0.32650818, 
 0.35039491, 
 0.58039491, 
 0.75039491, 
 0.72039491, 
 0.325578443,
 0.44382501,
 0.68094895, 
 0.53431938, 
 0.64661444, 
 0.59955388, 
 0.34313231, 
 0.47205522,
 0.31181618, ]


y2=[1.4181818,
 1.10723301,
 1.06172121, 
 1.18837228, 
 1.61206671, 
 1.28093   , 
 1.12650818, 
 1.15039491, 
 1.58039491, 
 1.85039491, 
 1.78039491, 
 1.325578443,
 1.44382501,
 1.68094895, 
 1.83431938, 
 1.84661444, 
 1.09955388, 
 1.54313231, 
 1.47205522,
 1.51181618, ]




#y2 = -1 * y1
#y3=6*y1

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
#ax3=ax1.twinx()

l1, =ax1.plot(x,y1,linestyle = '-', # 折线类型
         linewidth = 1, # 折线宽度
         color = 'steelblue', # 折线颜色
         #marker = 'o', # 点的形状
         markersize = 2, # 点的大小
         markeredgecolor='black', # 点的边框色
         markerfacecolor='steelblue') # 点的填充色
'''
l2, =ax2.plot(x,y2,linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = 'steelblue', # 折线颜色
         #marker = 'o', # 点的形状
         markersize = 6, # 点的大小
         markeredgecolor='black', # 点的边框色
         markerfacecolor='steelblue') # 点的填充色
''''''
l3, =ax2.plot(x,y3,linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = 'steelblue', # 折线颜色
         marker = 'o', # 点的形状
         markersize = 6, # 点的大小
         markeredgecolor='black', # 点的边框色
         markerfacecolor='steelblue') # 点的填充色
'''


xtick = np.arange(start=0, stop=120, step=10) 
x_ticks_label=['0','2min', "4min","6min" ,"8min","10min","12min","14min","16min","18min","20min",' ']

#ax1_y_label=np.arange(start=0, stop=100, step=10)/100

ax1.set_xticks(xtick)
ax1.set_xticklabels(x_ticks_label)
#ax1.set_ylabel(ax1_y_label)


ax1.set_xlabel("time")
ax1.set_ylabel("Density of Pedestrians",color='g')
ax2.set_ylabel("Pedestrian Distance",color='b')

# 设置图例
#plt.legend(handles=[l1,l2,l3,],labels=['s_dq_pctchange','s_dq_volume','1234'],loc='best')

plt.show()
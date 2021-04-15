import matplotlib.pyplot as plt
import numpy as np
import scipy.signal


x = np.arange(0,100,1)
print(x)

y1=[0.4181818 , 0.17271024, 0.12509825, 0.54494677, 0.15759899, 0.46458535,\
 0.10723301, 0.96223606, 0.38338149 ,0.63228686, 0.64072838, 0.75145779,\
 0.06172121, 0.82789339, 0.84407703 ,0.2733791 , 0.04367833, 0.35678594,\
 0.18837228, 0.00261954, 0.65256543, 0.59145671, 0.84511559, 0.15862903,\
 0.61206671, 0.41233294 ,0.32576054, 0.31128229, 0.77169419, 0.89360219,\
 0.28093   , 0.84311508 ,0.55295905, 0.48205396, 0.32814106, 0.22271474,\
 0.12650818, 0.15982693, 0.03530576, 0.58756545, 0.58412981, 0.81720334,\
 0.95039491, 0.00207922 ,0.68025556, 0.12010345, 0.84228866, 0.89228542,\
 0.05578443, 0.11285932 ,0.07217272, 0.64847655, 0.23423048, 0.69521211,\
 0.81382501, 0.48468489 ,0.37001743, 0.20728719, 0.31082172, 0.84323027,\
 0.78094895, 0.98453961 ,0.99743146, 0.6861553,  0.06433607, 0.62448205,\
 0.83431938, 0.3046135 , 0.87562318, 0.11790782, 0.27811535, 0.10181848,\
 0.84661444, 0.94705109 ,0.44005372, 0.73688689 ,0.76958943, 0.13888947,\
 0.09955388, 0.11318463, 0.11248519, 0.14577386, 0.82167814, 0.74384312,\
 0.54313231, 0.92203956, 0.47983416, 0.12500126, 0.75557341, 0.97175653,\
 0.47205522, 0.40365322, 0.23675068, 0.79724734, 0.62546294, 0.35330563,\
 0.51181618, 0.78645654, 0.92246969, 0.52332482]


#y1=np.random.rand(100)
print(y1)
y1 = scipy.signal.savgol_filter(y1,13,3)

y2=y1+0.3
print(y2)
y2 = scipy.signal.savgol_filter(y2,15,5)
#y2 = -1 * y1
#y3=6*y1

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
#ax3=ax1.twinx()
'''
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
'''
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
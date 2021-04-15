# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)  

# 设置绘图风格
#plt.style.use('ggplot')
# 设置中文编码和负号的正常显示
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False
#柱状图
#plt.bar([0], [0], label='graph 1')


x=[9,3]
y=[2,0]



# 绘图
plt.plot(x, # x轴数据
         y, # y轴数据
         linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = 'steelblue', # 折线颜色
         marker = 'o', # 点的形状
         markersize = 6, # 点的大小
         markeredgecolor='black', # 点的边框色
         markerfacecolor='steelblue') # 点的填充色



xtick = np.arange(start=0, stop=120, step=10) 
x_ticks_label=[' ','2min', "4min","6min" ,"8min","10min","12min","14min","16min","18min","20min",' ']

plt.xticks(xtick, x_ticks_label, fontsize=7) 

# params

# x: 条形图x轴
# y：条形图的高度
# width：条形图的宽度 默认是0.8
# bottom：条形底部的y坐标值 默认是0
# align：center / edge 条形图是否以x轴坐标为中心点或者是以x轴坐标为边缘

plt.legend()

plt.xlabel('time')
plt.ylabel('density')

#plt.title(u'测试例子——条形图', FontProperties=font)

plt.show()
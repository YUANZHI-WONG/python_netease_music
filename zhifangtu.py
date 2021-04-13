# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)  

plt.bar([10, 30, 50, 70, 90], [5.13,12.82,12.82,23.08,15.38,10.26,12.82,5.13,2.56], label='graph 1')

#plt.bar([2, 4, 6, 8, 10], [4, 6, 8, 13, 15], label='graph 2')

xtick = np.arange(start=0, stop=110, step=10) 
x_ticks_label=[' ','[0.00,0.05]', "[0.05,0.1]","[0.1,0.15]" ,"[0.15,0.2]","[0.2,0.25]","[0.3,0.35]","[0.35,0.4]","[0.4,0.45]","[>0.45]",' ']

plt.xticks(xtick, x_ticks_label, fontsize=7) 

# params

# x: 条形图x轴
# y：条形图的高度
# width：条形图的宽度 默认是0.8
# bottom：条形底部的y坐标值 默认是0
# align：center / edge 条形图是否以x轴坐标为中心点或者是以x轴坐标为边缘

plt.legend()

plt.xlabel('number')
plt.ylabel('value')

plt.title(u'测试例子——条形图', FontProperties=font)

plt.show()
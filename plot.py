# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)  


plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号
# 画出双坐标轴图像
fig,ax1 = plt.subplots(figsize = (10,8))
ax2 = ax1.twinx()
l1, = ax1.plot(data['date'],data["s_dq_pctchange"],'r-')
l2, = ax2.plot(data['date'],data["s_dq_volume"],'g-')
# 设置x,y轴文字说明
ax1.set_xlabel('time')
ax1.set_xticklabels(data["date"], rotation=45)
ax1.set_ylabel("y1,s_dq_pctchange")
ax2.set_ylabel("y2,s_dq_volume")
# 设置图例
plt.legend(handles=[l1,l2,],labels=['s_dq_pctchange','s_dq_volume'],loc='best')
# 设置标题
ax1.set_title('Comparison chart')
'''
# 两条line的数据
line1 = [(2, 0), (2, 1)]
line2 = [(7, 0), (7, 1)]
(line1_xs, line1_ys) = zip(*line1)
(line2_xs, line2_ys) = zip(*line2)
# 创建两条线，并添加
ax1.add_line(Line2D(line1_xs, line1_ys, linewidth=1, color='black'))
ax1.add_line(Line2D(line2_xs, line2_ys, linewidth=1, color='black'))
'''
plt.show()
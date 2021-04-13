import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
fig = plt.figure()
ax = fig.add_subplot(111) # 111代表1*1的图的第一个子图

'''
x = [-2.03,-2.16,-2.67,-1.43,-0.90,-0.32,-1.84,-2.77,-1.05,-0.60,-1.92,
2.03,
-2.15,
-2.27,
-2.39,
2.51,
-2.63
]
y = [-0.78,0.63,-1.57,-0.13,1.27,1.24,0.58,-0.79,-0.54,0.96,3.09,
2.58,
-2.66,
2.74,
-2.82,
2.90,
-3.48
]'''

x = [-2.03,
-2.16,
-2.67,

-2.90,
0.45,

-3.2,
-1.05,
-0.60,

1.03,
-2.15,
-1.27,
-4.39,
2.51,
-1.53,
0.13
]
y = [0.78,
-0.63,
-2.57,
1.27,
0.32,
-0,
-0.54,
-1.96,

1.58,
-1.66,
1.74,
-3.82,
-3.20,
-2.48,
-0.94
]


for i in range(15):

    circle_2 = Circle(xy=(x[i], y[i]), radius=0.05, alpha=1, color='black')
    ax.add_patch(circle_2)
    if x[i]>-4.5 and x[i]<1.5 and y[i]>-3 and  y[i]<3:
        circle_1 = Circle(xy=(x[i], y[i]), radius=0.5, alpha=0.1, color='r')
        ax.add_patch(circle_1)


circle_center = Circle(xy=(-1.5, 0), radius=3, alpha=0.5, color='lightgray')
ax.add_patch(circle_center)    

#plt.plot(x, y, 'b')

new_ticks = np.linspace(-5, 4, 10)
plt.xticks(new_ticks)


plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.axis('equal')
plt.show()

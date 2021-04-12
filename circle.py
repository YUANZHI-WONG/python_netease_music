import matplotlib.pyplot as plt
from matplotlib.patches import Circle

fig = plt.figure()
ax = fig.add_subplot(111) # 111代表1*1的图的第一个子图

x = [0]*100
y = [0]*100
for i in range(100):
	x[i] = i/100
	y[i] = pow(i/100,2)

for i in range(100):
    circle = Circle(xy=(x[i], y[i]), radius=0.02, alpha=0.1, color='b')
    ax.add_patch(circle)

plt.plot(x, y, 'b.')
plt.title('draw circle')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.axis('equal')
plt.show()

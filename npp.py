import numpy as np

arr = np.array([[1, 2, 3],
               [4, 5, 6]])
np.save('weight.npy', arr)

loadData = np.load('w.npy')

print("----type----")
print(type(loadData))
print("----shape----")
print(loadData.shape)
print("----data----")
print(loadData)
import numpy as np

array2d = np.array([[1,2,3], [4, 5, 6], [7,8,9]])
print("-" * 10)
print(array2d[:, 0:2])
print("-" * 10)
print(array2d[1:3, 0:3])
print("-" * 10)
print(array2d[-1::-1, -1::-1])
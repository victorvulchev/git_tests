import numpy as np

array1d = np.array([1, 2, 3, 4, 5, 6])
print(array1d.ndim)
array2d = np.array([[1, 2, 3], [4, 5, 6]])
print(array2d.ndim)
array3d = np.array([[[1, 2,3 ], [4, 5, 6]], [[7, 8, 9], [0, 1, 2]]])
print(array3d.ndim)
print(array3d)
array3d = array3d.reshape(2, 3, 2)
print(array3d.ndim)
print(array3d)

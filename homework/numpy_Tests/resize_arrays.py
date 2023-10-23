import numpy as np

the_array = np.array([1, 2, 3, 4, 5, 6, 7, 8])
the_array.resize(4)
print(the_array)
print("_"* 10)

the_array = np.array([1, 2, 3, 4, 5, 6, 7, 8])
the_array.resize(2, 4)
print(the_array)
print("_"* 10)

the_array = np.array([1, 2, 3, 4, 5, 6, 7, 8])
the_array.resize(3, 3)
print(the_array)

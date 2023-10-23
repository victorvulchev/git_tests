import numpy as np

the_array = np.array([1, 2, 3, 4, 5, 6, 7, 8])
the_array = the_array.reshape(2, 4)
print(the_array)
print("_"*10)

the_array = np.array([1, 2, 3, 4, 5, 6, 7, 8])
the_array = the_array.reshape(4, 2)
print(the_array)
print("_"*10)

the_array = np.array([1, 2, 3, 4, 5, 6, 7, 8])
the_array = the_array.reshape(8, 1)
print(the_array)
print("_"*10)
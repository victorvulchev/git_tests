import numpy as np
the_list = [1, 2, 3]
print(type(the_list))

array1 = np.array(the_list)
print(type(array1))

the_tuple = ((1, 2, 3))
print(type(the_tuple))

array2 = np.array(the_tuple)
print(type(array2))

array3 = np.array([the_tuple, the_list, array1])
print(array3)
import numpy as np
from numpy import dtype

type1 = np.array([1,2,3,4,5])
type2 = np.array([1.5, 2.5, 3.5, 6])
type3 = np.array(["a", "b", "c"])
#type4 = np.array(["Canada", "Australia"], dtype='US') doesn't work?
type5 = np.array([555, 666], dtype=float)

print(type1.dtype)
print(type2.dtype)
print(type3.dtype)
#print(type4.dtype)
print(type5.dtype)
print("_" * 5)

print(type1)

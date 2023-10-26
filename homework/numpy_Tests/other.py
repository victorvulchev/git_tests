import numpy as np

print("where():")
before = np.array([[1, 2, 3], [4, 5, 6]])
after = np.where(before < 4, before * 2, before *3)
print(after)

print("_"*10)
print("select():")
before2 = np.array([[1, 2, 3], [4, 5, 6]])
after2 = np.select([before2 < 4, before2 > 5], [before2 *2, before2 *3])
print(after2)

print("_"*10)
print("choose():")
a = np.array([[0, 1, 2], [2, 0, 1], [1, 2, 0]])
choises = [5, 10, 15]
b = np.choose(a, choises)
print(b)

print("*" * 10)
a = np.array([[0, 0, 0], [2, 2, 2], [1, 1, 1]])
choise1 = [5, 10, 15]
choise2 = [8, 16, 24]
choise3 = [9, 18, 27]
b = np.choose(a, (choise1, choise2, choise3))
print(b)





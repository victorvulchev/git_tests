test_list_1 = [1,2,3,4]
test_list_2 = [6,7,8,9]
from itertools import product

cartesian_product = list(product(test_list_1,test_list_2))

for i in cartesian_product:
    print(i)
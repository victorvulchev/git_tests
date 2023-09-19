def task(list1,list2):
    new_list = list1 + list2
    sorted_list = sorted(new_list)
    return sorted_list

test_list_1 = [1, 2, 3, 4, 5]
test_list_2 = [6,7,8,9,10]

print(list(task(test_list_1,test_list_2)))
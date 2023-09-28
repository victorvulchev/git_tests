def task_6(a_list):
    return sorted(a_list, key= lambda x: x[1])

my_list = [("John", 30), ("Alice", 25), ("Bob", 35), ("Eve", 28)]

#print(task_6(my_list))

def task_7(a_dict):
    return sorted(a_dict, key=lambda x:x["city"])

my_dict = [
    {"name": "John", "age": 30, "city": "New York"},
    {"name": "Alice", "age": 25, "city": "Los Angeles"},
    {"name": "Bob", "age": 35, "city": "Chicago"},
    {"name": "Eve", "age": 28, "city": "San Francisco"}
]

#print(task_7(my_dict))

def task_8(list_a, list_b):
    return list(filter(lambda x: x in list_b, list_a))

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

#print(task_8(list1, list2))

def task_9(a_list):
    evens = list(filter(lambda x: x% 2== 0, a_list))
    odds = list(filter(lambda x: x% 2!= 0, a_list))
    return f"Even numbers: {len(evens)} \nOdd numbers: {len(odds)}"

print(task_9(list1))
    

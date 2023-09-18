a_set = set([])
b_set = set([])

command = input("Add element to set 1:")
while command != "":
    a_set.add(command)
    command = input("Add element to set 1:")

command = input("Add element to set 2:")
while command != "":
    b_set.add(command)
    command = input("Add element to set 2:")

dictionary = {}
el_1 = a_set|b_set
el_2 = a_set&b_set
el_3 = a_set-b_set
dictionary[f"{a_set}|{b_set}"] = el_1
dictionary[f"{a_set}&{b_set}"] = el_2
dictionary[f"{a_set}-{b_set}"] = el_3

for i,j in dictionary.items():
    print(f"{i}:{j}")
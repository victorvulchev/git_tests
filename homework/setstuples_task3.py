your_set = set([])
command = input("What do you want to add to the set?")
while command != "":
    your_set.add(command)
    command = input("What do you want to add to the set?")
your_set2 = set([])
command = input("What do you want to add to the second set?")
while command != "":
    your_set2.add(command)
    command = input("What do you want to add to the second set?")

a = len(your_set|your_set2)
b = len(your_set.intersection(your_set2))

print(b)

t = (a,b)

print(t)

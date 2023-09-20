import re
the_list = []
everything = dir(re)

for i in everything:
    if "find" in i:
        the_list.append(i)

for i in the_list:
    print(i)
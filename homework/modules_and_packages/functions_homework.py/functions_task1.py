def reader(list, element):
    is_found = False
    position = 0
    for i in range(0,len(list) - 1):
        if element == list[i]:
            is_found = True
            position = i
            break
    if is_found:
        print(f"Position {position}")
    else:
        print("Not found")

reader([1, 2, 5, 9, 10], 5)
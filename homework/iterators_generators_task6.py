test_list = [1,-2,3,-4,5,-6]

main_list = iter(test_list)
positive = []
negative = []
while True:
    try:
        item = next(main_list)
        if item > 0:
            positive.append(item)
        else:
            negative.append(item)
    except StopIteration as e:
        break
print(positive)
print(negative)
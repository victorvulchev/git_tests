seq = [1,2,3,4,5,6,7,8,9,10]

iterator = iter(seq)

while True:
    try:
        item = next(iterator)
        if item % 2 != 0:
            print(item)
    except StopIteration as e:
        break


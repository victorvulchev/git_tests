
for i in range(1, 20 + 1):
    if i == 1:
        print(i)
    else:
        for j in range(2,i +1):
            if i == j:
                print(i)
            elif i == 2:
                print(i)
                break
            elif i % j == 0:
                break
            else:
                continue

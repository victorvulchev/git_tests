def prime_numbs(start,end):
    for i in range(start, end + 1):
        if i == 1:
            yield i
        else:
            for j in range(2,i +1):
                if i == j:
                    yield i
                elif i == 2:
                    yield i
                    break
                elif i % j == 0:
                    break
begin = 1
ending = 20

print((list(prime_numbs(begin,ending))))
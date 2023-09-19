

def even_numbers(start,end):
    for i in range(start, end):
        if i % 2 == 0:
            yield i
begin = 1
ending = 20

print((list(even_numbers(begin,ending))))
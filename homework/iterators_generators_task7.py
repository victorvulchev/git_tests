test_list = [1,-2,3,-4,5,-6]

def is_positive(a):
    for i in a:
        if i > 0:
            yield i
def is_negative(a):
    for i in a:
        if i < 0:
            yield i

print(list(is_positive(test_list)))
print(list(is_negative(test_list)))
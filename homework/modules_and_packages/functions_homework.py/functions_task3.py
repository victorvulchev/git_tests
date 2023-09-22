def fibonacci(numb):
    counter = 1
    first = 0
    second = 1
    result = 0
    while counter != numb:
        counter += 1
        result = first + second
        first = second
        second = result
    print(f"The {numb}th fib term is {result}")

fibonacci(5)

def factorial(numb):
    fact = 1
    for i in range(1,numb + 1):
        fact *= i
    print(fact)

factorial(5)
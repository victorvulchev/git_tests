def volwels_in_word(a):
    vowels = "AEIOUaeiou"
    for i in a:
        if i in vowels:
            yield i

word = input("Enter a word:")
#f = volwels_in_word
from itertools import islice

print(list(volwels_in_word(word)))
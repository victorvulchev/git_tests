word = input("Enter a word:")
iterator = iter(word)
vowel_list = []

while True:
    try:
        vowels = vowels = "AEIOUaeiou"
        item = next(iterator)
        if item in vowels:
            vowel_list.append(item)
    except StopIteration as e:
        break

print(vowel_list)
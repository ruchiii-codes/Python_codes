# Using filter() and list() functions and .lower() method filter all the vowels in a given string.
text = "Hello World"

vowels = list(filter(lambda x: x.lower() in "aeiou", text))

print(vowels)
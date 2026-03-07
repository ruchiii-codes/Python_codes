# Write a python function that accepts a string as input and returns the word with most occurence.
def most_word(text):
    words = text.split()
    
    max_count = 0
    max_word = ""

    for word in words:
        count = words.count(word)
        if count > max_count:
            max_count = count
            max_word = word

    print(max_word, "->", max_count)


most_word("hello how are you i am fine thank you")
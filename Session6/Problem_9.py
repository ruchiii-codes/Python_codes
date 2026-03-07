# Write a python program that receives a list of strings and performs bag of word operation on those strings
def bag_of_words(sentences):
    bag = {}

    for sentence in sentences:
        words = sentence.split()
        for word in words:
            if word in bag:
                bag[word] += 1
            else:
                bag[word] = 1

    print(bag)


texts = [
    "i love python",
    "python is easy",
    "i love coding"
]

bag_of_words(texts)
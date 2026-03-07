# Write a Python function that accepts a hyphen-separated sequence of words as parameter and returns the words in a hyphen-separated sequence after sorting them alphabetically.
def sort_words(text):
    words = text.split("-")     # split words by hyphen
    words.sort()                # sort alphabetically
    return "-".join(words)      # join with hyphen again

print(sort_words("green-red-yellow-black-white"))
# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def count_case(text):
    upper = 0
    lower = 0
    
    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    print("No. of Upper case characters :", upper)
    print("No. of Lower case characters :", lower)


count_case("Python Is Very Useful For Data Science And Machine Learning.")
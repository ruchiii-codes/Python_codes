# Count the frequency of a particular character in a provided string. 
# Eg 'hello how are you' is the string, the frequency of h in this string is 2.

string = input("Enter a string: ")
frequency = input("Enter the character to find frequency: ")
counter = 0

for i in string:
    if i == frequency:
        counter += 1
print(f"The frequency of '{frequency}' in the string is: {counter}")
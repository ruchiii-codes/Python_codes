# Write a program which can remove a particular character from a string.

string = input("Enter a string : ")
term = input("What would like to remove : ")

result = ''
for i in string:
    if i != term:
        result = result + i

print("The string after removing", term, "is:", result)

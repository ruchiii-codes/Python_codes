# Write a program to Check if a given string is binary string of or not.
# A string is said to be binary if it's consists of only two unique characters.
# Take string input from user.
# Input: str = "01010101010", Input: str = "1222211", Input: str = "Campusx"

s = input("Enter string: ")

unique_chars = set(s)

if len(unique_chars) == 2:
    print("Yes")
else:
    print("No")
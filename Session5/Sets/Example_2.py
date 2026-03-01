# Write a program to count unique number of vowels using sets in a given string.
# Lowercase and upercase vowels will be taken as different.

Str1 = "hands-on data science mentorship progrAm with live classes at affordable fee only on Online Classes"

vowels = "aeiouAEIOU"
unique_vowels = set()

for ch in Str1:
    if ch in vowels:
        unique_vowels.add(ch)

print("No of unique vowels-", len(unique_vowels))
# Write a Python program to create a list containing the power of said number in bases raised to the corresponding number in the index using Python map.
nums = [2, 3, 4, 5]

result = list(map(lambda x: x ** nums.index(x), nums))

print(result)
# Print all numbers divisible by 5 in the range of 1 to 50

L = [i for i in range (1,51) if i % 5 == 0]  # List comprehension to create a list of numbers from 1 to 50 that are divisible by 5
print(L)  # Output: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
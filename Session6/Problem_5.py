# Write a Python function to check whether a number is perfect or not. 
# A Perfect number is a number that is half the sum of all of its positive divisors (including itself).
# Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. 
# Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. 
# The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.
def is_perfect(num):
    sum = 0
    
    for i in range(1, num):
        if num % i == 0:
            sum += i
            
    if sum == num:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")

is_perfect(6)
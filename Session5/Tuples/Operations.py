# + and *
t1 = (1,2,3,4)
t2 = (5,6,7,8)
print(t1 + t2)  # Concatenation of two tuples
print(t1 * 2)   # Repetition of a tuple
print(t2 * 3)   # Repetition of a tuple

# Membership operator
t3 = (1,2,3,4)
print(2 in t3)  # Output: True
print(5 in t3)  # Output: False

# Iteration
t4 = (1,2,3,4)
for i in t4:
    print(i)

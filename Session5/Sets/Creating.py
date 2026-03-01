# Empty
s = set()
print(s)
print(type(s))

# 1D set
s1 = {1, 2, 3, 4, 5}
print(s1)

# 2D set      
# This will raise a TypeError because sets cannot contain mutable elements in it.
# And sets are mutable, so they cannot be added to a set.
# s2 = { 1, 2, {3, 4} } 
# print(s2)

# Heterogeneous set
s3 = {1,'hello', 3.14, True} # True is considered as 1 in a set, so it will not be added to the set because 1 is already present in the set.
print(s3)  # True will not print in the set because it is considered as 1 in a set, and 1 is already present in the set.
s4 = {1, 'hello', 3.14, (1,2,3)} # This will not raise a TypeError because tuples are immutable, so they can be added to a set.
print(s4)  # output : {1, 3.14, 'hello', (1, 2, 3)}    because sets are unordered, so the order of elements in the set may not be the same as the order of elements in the set literal.

# Type conversion
s5 = set('hello')  # set is a built-in function that converts an iterable to a set
print(s5) 
s6 = set([1, 2, 3, 4, 5])  # set is a built-in function that converts an iterable to a set
print(s6)

# Duplicates not allowed in a set
s7 = {1,1,2,3,3,2,4,5,5}
print(s7) # output : {1, 2, 3, 4, 5} because duplicates are not allowed in a set, so only one occurrence of each element will be stored in the set.


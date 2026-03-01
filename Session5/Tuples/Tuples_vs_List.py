# Differences between Tuples and Lists
# Mutable vs Immutable

# List
a = [1,2,3]
b = a

a.append(4)
print(a)
print(b)

# Tuple
a = (1,2,3)
b = a

a = a + (4,)
print(a)
print(b)
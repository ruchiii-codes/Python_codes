# Set Operations
s1 = { 1, 2, 3, 4, 5}
s2 = { 4, 5, 6, 7, 8}

# Union(|)
print(s1 | s2)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection(&)
print(s1 & s2)  # Output: {4, 5}

# Difference(-)
print(s1 - s2)  # Output: {1, 2, 3} (Items in s1 but not in s2)
print(s2 - s1)  # Output: {6, 7, 8} (Items in s2 but not in s1)

# Symmetric Difference(^)
print(s1 ^ s2)  # Output: {1, 2, 3, 6, 7, 8} (Same items will be removed from both sets)

# Membership
print(3 in s1)  # Output: True
print(6 not in s2)  # Output: False

# Iteration
for item in s1:
    print(item)
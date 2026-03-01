# Frozenset is an immutable version of a set.
# It is created using the frozenset() function.
# Once a frozenset is created, it cannot be modified.
# This means that you cannot add or remove elements from a frozenset.
# But you can perform set operations on it because it only reads the elements.
# Only read functions can be used on a frozenset, such as union, intersection, difference, etc.
# Write operations and functions will not work on a frozenset, such as add, remove, discard, pop, clear, etc.

fs = frozenset([1,2,3])
print(fs)

# 2d frozenset
fs = frozenset([1,2,frozenset([3,4])])
print(fs)
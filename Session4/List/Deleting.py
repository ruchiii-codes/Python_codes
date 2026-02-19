#del
L = [1, 2, 3, 4, 5]  # 1D List
print(L)  # Output: [1, 2, 3, 4, 5]
del L[-1]  # Deleting the last element
print(L)  # Output: [1, 2, 3, 4]   INDEXING
del L[1:3]  # Deleting elements from index 1 to 2 (exclusive)
print(L)  # Output: [1, 4]    SLICING
del L  # Deleting the entire list
# print(L)  # This will raise an error because L is no longer defined

#remove
L1 = [1, 2, 3, 4, 5]  # 1D List
print(L1)  # Output: [1, 2, 3, 4, 5]
L1.remove(3)  # Removing the first occurrence of 3
print(L1)  # Output: [1, 2, 4, 5]  # The first occurrence of 3 is removed

#pop
L2 = [1, 2, 3, 4, 5]  # 1D List
L2.pop()  # Removing the last element (default behavior)
print(L2)  # Output: [1, 2, 3, 4]  # The last element (5) is removed
L2.pop(1)  # Removing the element at index 1
print(L2)  # Output: [1, 3]  # The last element (5) and the element at index 1 (2) are removed

#clear
L3 = [1, 2, 3, 4, 5]  # 1D List
print(L3)  # Output: [1, 2, 3, 4, 5]
L3.clear()  # Clearing all elements from the list
print(L3)  # Output: []  # The list is now empty
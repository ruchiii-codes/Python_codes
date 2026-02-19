#Append     (Add an item to the end of the list)
L = [1, 2, 3]
L.append(4)  # Appending an integer
print(L)  # Output: [1, 2, 3, 4]
L.append([6,7,8])
print(L)  # Output: [1, 2, 3, 4, [6, 7, 8]] (appending a list)

# Extend     (Add multiple items to the end of the list)
L1 = [1, 2, 3, 4, 5]
L1.extend([5, 6, 7])  # Extending with multiple integers 
print(L1)  # Output: [1, 2, 3, 4, 5, 5, 6, 7]
L1.extend('Hello')  # Extending with a string (adds each character)
print(L1)  # Output: [1, 2, 3, 4, 5, 5, 6, 7, 'H', 'e', 'l', 'l', 'o']

# Insert     (Insert an item at a specific position)
L2 = [1, 2, 3, 4, 5]
L2.insert(2, 10)  # Inserting 10 at index 2
print(L2)  # Output: [1, 2, 10, 3, 4, 5]
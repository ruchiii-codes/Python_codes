#Indexing
L = [1, 2, 3, 4, 5]     # 1D List
L[-1] = 10  # Changing last element to 10
print(L)  # Output: [1, 2, 3, 4, 10]

L1 = [1, 2, 3, [4, 5]]  # 2D List
L1[3][0] = 20  # Changing first element of sublist to 20
print(L1)  # Output: [1, 2, 3, [20, 5]]

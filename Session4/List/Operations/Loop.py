#Loop
L1 = [1, 2, 3, 4, 5]  # 1D List
L2 = [1, 2, 3, [4, 5]]  # 2D List
for i in L1:
    print(i)  # Output: 1, 2, 3, 4, 5 (each element in L1)
for i in L2:
    print(i)  # Output: 1, 2, 3, [4, 5] (each element in L2)
for i in L2[3]:  # Looping through the sublist in L2
    print(i)  # Output: 4, 5 (each element in the sublist [4, 5])

L3 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]  # 3D List
for i in L3:
    print(i) # Output: 1, 2, 3, 4, 5, 6, 7, 8 (each element in L3)

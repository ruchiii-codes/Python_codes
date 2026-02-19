#Membership 
L1 = [1, 2, 3, 4, 5]  # 1D List
L2 = [1, 2, 3, [4, 5]]  # 2D List
print(1 in L1)  # Output: True (1 is in L1)
print(6 in L1)  # Output: False (6 is not in L1)
print(4 in L2)  # Output: False (4 is not directly in L2)
print([4, 5] in L2)  # Output: True ([4, 5] is a sublist in L2)
print(4 in L2[3])  # Output: True (4 is in the sublist [4, 5])
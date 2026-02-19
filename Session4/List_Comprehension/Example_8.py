# cartesian products -> List comprehension on 2 lists together
L1 = [1,2,3,4]
L2 = [5,6,7,8]

L3 = [i*j for i in L1 for j in L2]  # Cartesian product of L1 and L2
print(L3)  # Output: [5, 6, 7, 8, 10, 12, 14, 16, 15, 18, 21, 24, 20, 24, 28, 32]
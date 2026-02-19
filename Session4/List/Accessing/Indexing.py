#Indexing
L = [1, 2, 3, 4, 5]     # 1D List
# Accessing elements using positive indexing
print(L[0])  # Output: 1  
print(L[1])  # Output: 2
print(L[2])  # Output: 3   
print(L[3])  # Output: 4
print(L[4])  # Output: 5

# Accessing elements using negative indexing
print(L[-1])  # Output: 5 (last element)    
print(L[-2])  # Output: 4 (second last element)
print(L[-3])  # Output: 3 (third last element)
print(L[-4])  # Output: 2 (fourth last element) 
print(L[-5])  # Output: 1 (fifth last element)

L1 = [1, 2, 3, [4, 5]]  # 2D List
# Accessing elements using positive indexing    
print(L1[0])  # Output: 1
print(L1[1])  # Output: 2
print(L1[2])  # Output: 3
print(L1[3])  # Output: [4, 5] (sublist)
print(L1[3][0])  # Output: 4 (first element of sublist)
print(L1[3][1])  # Output: 5 (second element of sublist)

# Accessing elements using negative indexing
print(L1[-1])  # Output: [4, 5] (sublist)
print(L1[-2])  # Output: 3
print(L1[-3])  # Output: 2
print(L1[-4])  # Output: 1
print(L1[-1][0])  # Output: 4 (first element of sublist)    
print(L1[-1][1])  # Output: 5 (second element of sublist)

L3 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]  # 3D List
# Accessing elements using positive indexing
print(L3[0])  # Output: [[1, 2], [3, 4]] (first sublist)
print(L3[0][0])  # Output: [1, 2] (first sub-sublist)
print(L3[0][0][0])  # Output: 1 (first element of first sub-sublist)
print(L3[0][0][1])  # Output: 2 (second element of first sub-sublist)
print(L3[0][1])  # Output: [3, 4] (second sub-sublist)
print(L3[0][1][0])  # Output: 3 (first element of second sub-sublist)
print(L3[0][1][1])  # Output: 4 (second element of second sub-sublist)
print(L3[1])  # Output: [[5, 6], [7, 8]] (second sublist)
print(L3[1][0])  # Output: [5, 6] (first sub-sublist of second sublist)
print(L3[1][0][0])  # Output: 5 (first element of first sub-sublist of second sublist)
print(L3[1][0][1])  # Output: 6 (second element of first sub-sublist of second sublist)
print(L3[1][1])  # Output: [7, 8] (second sub-sublist of second sublist)
print(L3[1][1][0])  # Output: 7 (first element of second sub-sublist of second sublist)
print(L3[1][1][1])  # Output: 8 (second element of second sub-sublist of second sublist)

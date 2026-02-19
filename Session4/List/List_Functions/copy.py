L = [2, 1, 5, 7, 0] 
print(L)
print(id(L))
L1 = L.copy()  # Output: [2, 1, 5, 7, 0] (creates a shallow copy of the list L)  Note: The original list L remains unchanged.  
print(L1)
print(id(L1))

L1 = [1, 2, 3, 4]
L2 = [-1, -2, -3, -4]

print(zip(L1, L2))  # Returns an iterator of tuples, pairing elements from L1 and L2
L3 = list(zip(L1, L2))  # Convert the iterator to a list of tuples
print(L3)  # Output: [(1, -1), (2, -2), (3, -3), (4, -4)]


# Example
list(zip(L1,L2))

List = [i+j for i,j in zip(L1,L2)]  # Element-wise addition of paired elements from L1 and L2
print(List)   # Output: [0, 0, 0, 0] (since each pair sums to zero)
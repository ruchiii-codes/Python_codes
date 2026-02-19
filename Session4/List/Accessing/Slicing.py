L = [1, 2, 3, 4, 5, 6]  # 1D List
print(L[0:3])  # Output: [1, 2, 3] (first three elements)
print(L[-3 :])  # Output: [3, 4, 5, 6] (from third element to end)
print(L[0:])  # Output: [1, 2, 3, 4, 5, 6] (all elements)
print(L[0: :2])  # Output: [2, 3, 4] (from second to fourth element)
print(L[-5:-2:2])  # Output: [2, 4] (from second to fifth element with step 2)
print(L[: :-1])  # Output: [2, 4] (from second to fifth element with step 2)
# Find union of n arrays.
arrays = [
    [1, 2, 2, 4, 3, 6],
    [5, 1, 3, 4],
    [9, 5, 7, 1],
    [2, 4, 1, 3]
]

result = set()

for arr in arrays:
    result = result.union(arr)

print(sorted(list(result)))
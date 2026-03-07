# Use reduce to convert a 2D list to 1D
from functools import reduce

list2d = [[1,2],[3,4],[5,6]]

result = reduce(lambda x, y: x + y, list2d)

print(result)
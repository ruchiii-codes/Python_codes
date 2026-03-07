# Reduce apply logic to all items of a list and return a single value
# sum of all item
import functools

print(functools.reduce(lambda x,y:x+y,[1,2,3,4,5]))
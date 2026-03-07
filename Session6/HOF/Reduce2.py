# find min and max
import functools
print(functools.reduce(lambda x,y:x if x<y else y,[23,11,45,10,1]))
print(functools.reduce(lambda x,y:x if x>y else y,[23,11,45,10,1]))
# Tuples are immutable, which means that once a tuple is created, its elements cannot be changed.
# This will raise a TypeError because tuples are immutable
t1 = (1,2,3,4)
t1[0] = 10  
print(t1)

#Also we cannot add or remove elements from a tuple
#Because tuples are immutable

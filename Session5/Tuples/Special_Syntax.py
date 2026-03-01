# Type Unpacking 
# is a feature in Python 
# That allows you to assign the elements of a tuple (or any iterable) to multiple variables in a single line of code. 
# This can make your code more concise and easier to read.

a,b,c = (1,2,3)  # a=1, b=2, c=3
print(a,b,c)

#a,b = (1,2,3) 
#print(a,b)  # This will raise a ValueError because there are more values to unpack than variables

# Swap Values
a = 1
b = 2
a,b = b,a  # a=2, b=1
print(a,b)

# If there are too many values but user only wants first 2 values and ignore the rest, user can use * to unpack the remaining values into a list
a,b,*rest = (1,2,3,4,5)  # a=1, b=2, rest=[3,4,5]
print(a,b,rest)

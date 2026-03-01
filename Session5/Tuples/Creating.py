# Empty
t1 = ()   # List have [] and tuples have ()
print(t1)


# Creating a tuple with single item
t2 = (1)   # This is not a tuple, it's an integer
print(t2)
print(type(t2))  # Output: <class 'int'>    
t3 = ('hello')  # This is not a tuple, it's a string
print(t3)
print(type(t3))  # Output: <class 'str'>

# To create a tuple with a single item, we need to add a comma after the item
t4 = (1,)  # This is a tuple with a single item
print(t4)
print(type(t4))  # Output: <class 'tuple'>
t5 = ('hello',)  # This is a tuple with a single item
print(t5)
print(type(t5))  # Output: <class 'tuple'>


#Homogeneous tuple
t6 = (1,2,3,4,5)
print(t6)

# Heterogeneous tuple
t7 = (1, 'hello', 3.14, True, [1, 2, 3])
print(t7)

#2D tuple
t8 = (1, 2, 3, (4, 5, 6))
print(t8)

# Type conversion
t9 = tuple('hello')  # tuple is a built-in function that converts an iterable to a tuple
print(t9)  # Output: ('h', 'e', 'l', 'l', 'o')
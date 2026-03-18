# Object is an instance of a class.
# Everything in python is an object.
 
L = [1,2,3]  # L is variable  and the type of L is list and list is a class and L is an object of list class.
print(type(L))
# L.upper()  -> L is a list object and list class does not have upper function that's why we get AttributeError: 'list' object has no attribute 'upper'


# Syntax to create an object of a class:
# object_name = Class_name()


# Object literal for datatypes:
# List -> []
L = [1,2,3]   # L is an object name of list datatype and list is a class and L is an object of list class.
print(type(L)) # <class 'list'>

# Dictionary -> {}
D = {'a': 1, 'b': 2}
print(type(D)) # <class 'dict'>

# Set -> set()
S = {1,2,3}
print(type(S)) # <class 'set'>

# Tuple -> ()
T = (1,2,3)
print(type(T)) # <class 'tuple'>



# But we can also create like this:
L = list([1,2,3])
print(type(L)) # <class 'list'>

D = dict({'a': 1, 'b': 2})
print(type(D)) # <class 'dict'>

S = set({1,2,3})
print(type(S)) # <class 'set'>

T = tuple((1,2,3))
print(type(T)) # <class 'tuple'>
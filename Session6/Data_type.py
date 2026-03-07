# Functions are first class objects in python, which means they can be treated like any other data type.
# They can be assigned to variables, passed as arguments to other functions, and returned from functions.
# type and id
def square(num):  # Function in python is data type
  return num**2

type(square)

id(square)

# reassign
x = square  # we can call that square function by x
id(x)
x(3)

# deleting a function
# del square

# storing
L = [1,2,3,4,square]
L[-1](3)

s = {square} # sets does not store mutable data type so if it run it means function is immutable 
s
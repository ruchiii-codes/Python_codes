s = 'hello world'
print(s)
del s
print(s) # This will raise an error because the variable s has been deleted and cannot be accessed anymore.

str = 'hello world'
del str[-1:-5:2]
print(str)  # This will raise an error because we cannot delete a slice of a string. Strings are immutable, and we cannot change their content after they have been created.
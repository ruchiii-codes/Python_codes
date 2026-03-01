# User can delete a tuple using the del keyword, but this will remove the entire tuple from memory.
# User can not delete a specific element from a tuple because tuples are immutable.
t1 = (1,2,3,4)
del t1     # t1 is deleted from memory
print(t1)  # This will raise a NameError because t1 has been deleted

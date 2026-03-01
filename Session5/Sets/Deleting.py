# del  
# can delete the entire set from memory, but cannot delete specific elements from a set
s1 = {1,2,3,4,5}
print(s1)
del s1
#print(s1)  # This will raise a NameError because s1 has been deleted from memory

# discard 
# can delete specific elements from a set, but will not raise an error if the element is not found in the set
s2 = {1,2,3,4,5}
s2.discard(3)  # This will remove 3 from the set
s2.discard(10) # This will not raise an error because 10 is not in the set
print(s2)

# remove
# can delete specific elements from a set, but will raise a KeyError if the element is not found in the set
s3 = {1,2,3,4,5}
s3.remove(4)  # This will remove 4 from the set 
#s3.remove(10) # This will raise a KeyError because 10 is not in the set
print(s3)

# pop
# can delete a random element from the set and return it, but will raise a KeyError if the set is empty
s4 = {1,2,3,4,5}
print(s4.pop())  # This will remove and return a random element from the set
print(s4)

# clear
# can delete all elements from a set, leaving it empty
s5 = {1,2,3,4,5}
s5.clear()  # This will remove all elements from the set
print(s5)
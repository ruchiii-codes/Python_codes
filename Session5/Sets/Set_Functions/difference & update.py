# difference / difference_update
s5 = {1,2,3,4,5}
s6 = {4,5,6,7,8}
print(s5.difference(s6))

s5.difference_update(s6)
print(s5) # Difference results will be stored in s5
print(s6)
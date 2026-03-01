# symmetric_difference / symmetric_difference_update
s7 = {1,2,3,4,5}
s8 = {4,5,6,7,8}
print(s7.symmetric_difference(s8))

s7.symmetric_difference_update(s8)
print(s7) # Symmetric difference results will be stored in s7
print(s8)
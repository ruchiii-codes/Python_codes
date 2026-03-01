# intersection / intersection_update
s3 = {1,2,3,4,5}
s4 = {4,5,6,7,8}
print(s3.intersection(s4))

s3.intersection_update(s4)
print(s3) # Intersection results will be stored in s3
print(s4)
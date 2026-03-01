# Nested Comprehension
# print tables of number from 2 to 4
Tables = {i:{j:i*j for j in range(1,11)} for i in range(2,5)}
print(Tables)
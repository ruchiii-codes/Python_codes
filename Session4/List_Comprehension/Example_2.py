# Scalar multiplication on a vector
v = [2, 4, 6]
s = -3

scalar = [s*i for i in v]  # In one line by using List Comprehension
print(scalar)  # Output: [-6, -12, -18] (each element in v multiplied by s)



# Not using List Comprehension
x = []
for i in v:
    x.append(s * i)  # In multiple lines by using a for loop
print(x)  # Output: [-6, -12, -18] (each element in v multiplied by s)
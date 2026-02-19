# Print a (3,3) matrix using list comprehension -> Nested List comprehension

Matrix = [[i*j for i in range (1,4)] for j in range (1,4)]  # Nested list comprehension to create a multiplication table from 1 to 3
print(Matrix)   # Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]] 
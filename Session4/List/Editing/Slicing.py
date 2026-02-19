#Slicing in Python allows you to access a portion of a list by specifying a start and end index.
# The syntax is list[start:end:step], where 'start' is the index to begin slicing, 'end' is the index to stop (exclusive), and 'step' is the interval between indices.
L = [1, 2, 3, 4, 5]  # 1D List
L[1:4] = [200,300,400] # Replacing elements from index 1 to 3 with new values
print(L)  # Output: [1, 200, 300, 400, 5]
# Write a program that can convert a 2D list to 1D list
L = [[1,2,3],
     [4,5,6],
     [7,8,9]]

new_list = []

for row in L:
    for item in row:
        new_list.append(item)

print(new_list)

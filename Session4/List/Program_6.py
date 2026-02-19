# Write a program to remove duplicate items from a list

L = [1,2,1,2,3,4,5,3,4]
new_list = []

for i in L:
    if i not in new_list:
        new_list.append(i)

print(new_list)
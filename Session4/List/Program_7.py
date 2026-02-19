# Write a program to check if a list is in ascending order or not
L = [1, 2, 3, 4, 5]

flag = True

for i in range(len(L) - 1):
    if L[i] > L[i + 1]:
        flag = False
        break

if flag:
    print("List is in ascending order")
else:
    print("List is not in ascending order")
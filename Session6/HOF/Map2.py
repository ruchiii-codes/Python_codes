# odd/even labelling of list items
L = [1,2,3,4,5]
print(list(map(lambda x:'even' if x%2 == 0 else 'odd',L)))
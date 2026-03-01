# Count no of tuples, list and set from a list
list1 = [{'hi', 'bye'}, {'Geeks', 'forGeeks'}, ('a', 'b'), ['hi', 'bye'], ['a', 'b']]

list_count = 0
set_count = 0
tuple_count = 0

for i in list1:
    if type(i) == list:
        list_count += 1
    elif type(i) == set:
        set_count += 1
    elif type(i) == tuple:
        tuple_count += 1

print("List-", list_count)
print("Set-", set_count)
print("Tuples-", tuple_count)
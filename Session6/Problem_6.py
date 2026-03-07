# Write a Python function to concatenate any no of dictionaries to create a new one.
def concatenate_dicts(d1, d2, d3):
    result = {}
    result.update(d1)
    result.update(d2)
    result.update(d3)
    return result

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

print(concatenate_dicts(dic1, dic2, dic3))
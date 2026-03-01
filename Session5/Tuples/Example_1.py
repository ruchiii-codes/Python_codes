# Join Tuples if similar initial element
test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]

result = {}

for a, b in test_list:
    if a in result:
        result[a].append(b)
    else:
        result[a] = [b]

output = [(k, *v) for k, v in result.items()]

print(output)
# Multiply Adjacent elements (both side) and take sum of right and lest side multiplication result.
t = (1, 5, 7, 8, 10)

result = []

for i in range(len(t)):
    if i == 0:
        result.append(t[i] * t[i+1])
    elif i == len(t)-1:
        result.append(t[i] * t[i-1])
    else:
        result.append(t[i]*t[i-1] + t[i]*t[i+1])

print(tuple(result))
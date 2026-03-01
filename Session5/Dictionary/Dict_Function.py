# len/sum/min/max/sorted
d = {'a':1,'b':2,'c':3,'d':4,'e':5}
print(len(d))


print(sum(d.values()))

print(min(d))
print(min(d.values()))

print(max(d))
print(max(d.values()))

print(sorted(d))
print(sorted(d,reverse=True))

d1 = {'name': 'nitish', 'gender': 'male', 'age': 33}
print(d)

print(d.items()) # displays in list of tuples format
print(d.keys()) # print only keys
print(d.values()) # print only values

# update
a1 = {1:2,3:4,4:5}
a2 = {4:7,6:8}

a1.update(a2)
print(a1)
# len/sum/min/max/sorted
t = (1,5,3,2,4,6)
print(len(t))

print(sum(t))

print(min(t))

print(max(t))

print(sorted(t))
print(sorted(t,reverse=True))

# count
t = (1,2,3,4,5)
print(t.count(2))
print(t.count(10))

# index
print(t.index(3))
#print(t.index(10)) # This will raise a ValueError because 10 is not in the tuple
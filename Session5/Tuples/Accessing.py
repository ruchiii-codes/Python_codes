# Indexing 
t1 = (1,2,3,4)
print(t1[0])   # Positive indexing
print(t1[-1])  # Negative indexing

# Slicing
t2 = (1,2,3,4)
print(t2[0:4])
print(t2[0:4:2])
print(t2[-3:-1])
print(t2[::-1])  # Reversing the tuple

t3 = (1, 2, 3, (4, 5))
print(t3[-1][0])
print(t3[-1][-1])
print(t3[3][0])
print(t3[-3])
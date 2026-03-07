# Higher Order Functions (HOF)
def transform(f,L):
  output = []
  for i in L:
    output.append(f(i))

  print(output)

L = [1,2,3,4,5]

transform(lambda x:x**2,L)
transform(lambda x:x**3,L)
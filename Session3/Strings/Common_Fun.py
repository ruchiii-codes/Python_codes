#len, max, min, sorted
print(len('hello world'))
print(max('hello world'))
print(min('hello world'))
print(sorted('hello world',reverse=True))

#Capitalize, Title, Upper, Lower, Swapcase
s = 'hello world'
print(s.capitalize())
print(s)

print(s.title())

print(s.upper())

print('Hello Wolrd'.lower())

print('HeLlO WorLD'.swapcase())

#Count, Find, Index
print('my name is Ruchi'.count('i'))
print('my name is Ruchi'.find('x'))

#endswith, startswith
print('my name is Ruchi'.endswith('i'))
print('my name is Ruchi'.startswith('ok'))

#isalnum/ isalpha/ isdigit/ isidentifier
print('Ruchi1234%'.isalnum())
print('Ruchi'.isalpha())
print('123abc'.isdigit())
print('first-name'.isidentifier())

#Split/Join
print('hi my name is Ruchi'.split())
print(" ".join(['hi', 'my', 'name', 'is', 'Ruchi']))

#Replace
print('hi my name is Ruchi'.replace('Ruchi','Vispute'))

# Strip
print('Ruchi                           '.strip())
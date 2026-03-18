# object without a reference
class Person:

  def __init__(self):
    self.name = 'Ruchi'
    self.gender = 'female'

p = Person()
q = p

# Multiple ref
print(id(p))
print(id(q)) 

# change attribute value with the help of 2nd object
print(p.name)
print(q.name)
q.name = 'Vispute'
print(q.name)
print(p.name)
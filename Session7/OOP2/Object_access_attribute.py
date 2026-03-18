class Person:

  def __init__(self,name_input,country_input):
    self.name = name_input
    self.country = country_input

  def greet(self):
    if self.country == 'india':
      print('Hello',self.name)
    else:
      print('Hello',self.name)

# how to access attributes
p = Person('Ruhci','india')
p.name
# how to access methods
p.greet()
# what if i try to access non-existent attributes
# p.gender  # get an error - AttributeError: 'Person' object has no attribute      
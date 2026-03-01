# indexing and slicing does not support in dictionary

# 1d dictionary
my_dict = {'name': 'Ruchi', 'age': 20}

# accessing values using keys
print(my_dict['name'])  
print(my_dict['age'])  

# accessing values using get() method
print(my_dict.get('name'))  
print(my_dict.get('age'))

# 2d dictionary
s = {
    'name':'Ruchi',
     'college':'bit',
     'sem':6,
     'subjects':{
         'dsa':61,
         'maths':78,
         'english':84
     }
}
print(s)

print(s['subjects']['maths'])

# 1d dictionary
d = {'name': 'Ruchi', 'age': 20, 3: 3 ,'gender': 'Female', 'weight': 40}

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

# pop  
d.pop(3) # Provide key
print(d)

# popitem
d.popitem() # it will remove the last item
print(d)

# del
del d['name']
print(d)

del s['subjects']['maths']
print(s)

# clear
d.clear() # it will remove all items from the dictionary but the dictionary will still exist in memory
print(d) # {} empty dictionary
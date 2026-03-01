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

d['age'] = 21 # update value of existing key
print(d)

s['subjects']['dsa'] = 65 # update value of existing key in nested dictionary
print(s)
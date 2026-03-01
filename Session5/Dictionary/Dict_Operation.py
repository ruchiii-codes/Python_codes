d = {'name': 'Ruchi', 'age': 20, 'gender': 'Female', 'weight': 40}

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

# membership operator
'name' in s    # always use key
'gender' in s 

# iteration 
for i in d:
    print(i)  # it will print keys of the dictionary

for i in d:
    print(i, d[i])  # it will print key and value of the dictionary
# 1d dictionary
d = {'name':'Ruchi','age':20} 
print(d)
d['gender'] = 'Female'
d['weight'] = 40
print(d)

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

s['subjects']['science'] = 75
print(s)

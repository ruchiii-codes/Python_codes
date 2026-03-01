# empty dictionary
d = {}
print(d)

# 1D dictionary  # Homogeneous dictionary
d1 = { 'name' : 'Ruchi' ,'gender' : 'Female' }
print(d1)

# with mixed keys
d2 = {(1,2,3):1,'Hello':'World'}
print(d2)

# 2D dictionary -> JSON
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

# using sequence and dict function
d4 = dict([('name','Ruchi'),('age',20),(6,3)])
print(d4)

# duplicate keys (cannot have duplicate keys in a dictionary, the last value will overwrite the previous one)
d5 = {'name':'Ruchi','name':'rahul'} # first 'name' key will be update by the second 'name' key, so the value of 'name' key will be 'rahul'
print(d5)

# mutable items as keys (not allowed)
d6 = {'name':'Ruchi',(1,2,3):2}
print(d6)
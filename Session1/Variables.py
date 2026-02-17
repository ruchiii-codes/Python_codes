# Dynamic Typing (Where we do not need to declare the type of variable)
a = 5
# Static Typing (Where we need to declare the type of variable)
#int a = 5


# Dynamic Binding (There is no fix data type for a variable, it can be re-assigned to any data type)
a = 5
print(a)
a = 'Ruchi'
print(a)

# Static Binding (A variable is bound to a specific data type and cannot be re-assigned to a different data type)
# int a = 5


#Multiple veriables at one time
a,b,c = 1,2,3
print(a,b,c)

a=b=c= 5
print(a,b,c)
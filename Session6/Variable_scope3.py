def h(y):
    # global x        we can use here 'global x' to modify the global variable x but this is not good for code 
    x += 1 # we can't modify x because it is global 
x = 5
h(x)
print(x)
# This will give an error because we are trying to modify a global variable x inside the function h without declaring it as global.
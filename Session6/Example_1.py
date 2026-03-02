def is_even(num):
    """This function checks if a number is even or odd."""
    if type(num) == int: 
       if num % 2 == 0:
           return 'even'
       else:
           return 'odd'
    else :
        return 'Please enter an integer.'   


for i in range(1,11):
    x = is_even(i)
    print(x)

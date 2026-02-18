fnum = int(input("Enter first number: "))
snum = int(input("Enter second number: "))

op = input("Enter operator (+, -, *, /): ")

if op == '+':
    result = fnum + snum
    print(result)
elif op == '-':
    result = fnum - snum
    print(result)
elif op == '*':
    result = fnum * snum
    print(result)
elif op == '/':
    if snum != 0:
        result = fnum / snum
        print(result)
    else:
        result = "Error! Division by zero."
        print(result)
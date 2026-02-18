# Write a program that can convert an integer to string.

number = input('Enter the number : ')

digits = '0123456789'
result = ''

while number != 0:
    result = digits[number % 10] + result  #getting error here
    number = number // 10

print(result)
print(type(result))
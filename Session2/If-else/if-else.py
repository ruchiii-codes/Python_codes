# login program and indentation
# email -> ruchi@gmail.com
# password -> 123456

email = input("Enter your email: ")
password = input("Enter your password: ")

if email == "ruchi@gmail.com" and password == "123456":
    print("Login successful")

elif email == 'ruchi@gmail.com' and password != '123456':
  # tell the user
  print('Incorrect password')
  password = input('enter password again')
    # check if password is correct   (Nested if-else)
  if password == '123456':
    print('Welcome,finally!')
  else:
    print('Try again later')

else:
    print("Login failed")
    print("Please check your email and password")
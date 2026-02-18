# Extract username from a given email. 
# Eg if the email is Ruchi06@gmail.com 
# then the username should be Ruchi06

s = input('Enter the email : ')

pos =s.index('@')
print(s[0:pos])
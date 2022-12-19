s1 = 'abc123'
s2 = 'abc$*123'
s3 = ''

print(s1.isalnum())  # True
print(s2.isalnum())  # False
print(s3.isalnum())  # False


s1 = 'ABCabc'
s2 = 'abc123'
s3 = ''

print(s1.isalpha())  # True
print(s2.isalpha())  # False
print(s3.isalpha())  # False


s1 = '1234567'
s2 = 'abc123'
s3 = ''

print(s1.isdigit())  # True
print(s2.isdigit())  # False
print(s3.isdigit())  # False


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

'''
Метод islower() определяет, являются ли все буквенные символы исходной строки строчными (имеют нижний регистр). 
Метод возвращает значение True если все буквенные символы исходной строки являются строчными и False в противном случае.
Все неалфавитные символы игнорируются!

'''

s1 = 'abc'
s2 = 'abc1$d'
s3 = 'Abc1$D'

print(s1.islower())  # True
print(s2.islower())  # True
print(s3.islower())  # False


'''
Метод isupper() определяет, являются ли все буквенные символы исходной строки заглавными (имеют верхний регистр).
Метод возвращает значение True если все буквенные символы исходной строки являются заглавными и False в противном случае.
Все неалфавитные символы игнорируются!
'''
s1 = 'ABC'
s2 = 'ABC1$D'
s3 = 'Abc1$D'

print(s1.isupper())  # True
print(s2.isupper())  # True
print(s3.isupper())  # False

'''
Метод isspace() определяет, состоит ли исходная строка только из пробельных символов.
Метод возвращает значение True если строка состоит только из пробельных символов и False в противном случае.
'''

s1 = '       '
s2 = 'abc1$d '

print(s1.isspace())  # True
print(s2.isspace())  # False


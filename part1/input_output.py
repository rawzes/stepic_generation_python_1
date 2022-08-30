'''
*
**
***
****
*****
******
*******
'''

print('*')
print('**')
print('***')
print('****')
print('*****')
print('******')
print('*******')

for i in range(7):
    print('*' * i)


print('a', 'b', 'c', sep='***')
print('a', 'b', 'c', end='\t')
print('d')

print('I', 'like', 'python', sep='***')

'''
separator = input()
str1 = input()
str2 = input()
str3 = input()
print(str1, str2, str3, sep=separator)
'''

name = input()
print("Привет,", name, end='!')

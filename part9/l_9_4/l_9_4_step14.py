s = input()
char = 'f'

if s.count(char) == 1:
    print(s.find(char))
elif s.count(char) >= 2:
    print(s.find(char), s.rfind(char))
else:
    print('NO')
    
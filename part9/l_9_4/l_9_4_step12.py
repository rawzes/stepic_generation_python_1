s = input()
if s.endswith('.com') or s.endswith('.ru'):
    print('YES')
else:
    print('NO')


# variant 2

if s.endswith(('.com', '.ru')):
    print('YES')
else:
    print('NO')

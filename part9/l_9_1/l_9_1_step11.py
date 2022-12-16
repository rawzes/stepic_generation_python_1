s = input()
is_number = False
for c in s:
    if c in '0123456789':
        is_number = True
        break
if is_number:
    print('Цифра')
else:
    print('Цифр нет')


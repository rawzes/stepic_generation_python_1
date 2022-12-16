s = input()
count_stars = 0
count_plus = 0

for c in s:
    if c == '*':
        count_stars += 1
    elif c == '+':
        count_plus += 1
print('Символ + встречается', count_plus, 'раз')
print('Символ * встречается', count_stars, 'раз')

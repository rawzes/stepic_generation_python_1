s = input()
count_gl = 0
count_sogl = 0

for c in s:
    if c in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
        count_gl += 1
    elif c in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        count_sogl += 1
print('Количество гласных букв равно', count_gl)
print('Количество согласных букв равно', count_sogl)

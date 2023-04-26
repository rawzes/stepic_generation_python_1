
alph = ['АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
#direction = input('Выбери направление: \n(+) - Шифрование \n(-) - Дешифрование:\n ')
#lang = int(input('Выбери язык алфавита: \n0 - Русский \n1 - Английский: \n'))
#step = int(direction + input('Веди число, шаг сдвига (со сдвигом вправо): '))
text = input()
text_splitted = text.split()
result = ''

for n in text_splitted:
    count = 0
    for c in n:
        if c.isalpha():
            count += 1
    for i in n:
        if i.isalpha():
            char = alph[1][(alph[1].index(i.upper()) + count) % len(alph[1])]
            result += char if i.isupper() else char.lower()
        else:
            result += i
    result += ' '
print(result)

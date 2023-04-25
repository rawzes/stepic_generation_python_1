import random


def generate_password(length, chars):
    password = ''
    for i in range(length):
        password += random.choice(chars)

    return password


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
non_clear = 'il1Lo0O'

chars = ''

n = int(input('Количество паролей для генерации: '))
length = int(input('Введите длину пароля: '))
is_digits = input(f'Включать ли цифры {digits}? (да \ нет) \n')
is_uppercase = input(f'Включать ли прописные буквы {uppercase_letters}? (да \ нет) \n')
is_lowercase = input(f'Включать ли строчные буквы {lowercase_letters}? (да \ нет) \n')
is_punctuation = input(f'Включать ли строчные буквы {punctuation}? (да \ нет) \n')
is_clear = input(f'Исключать ли неоднозначные символы {non_clear}? (да \ нет) \n')

if is_digits  == 'да':
    chars += digits
if is_uppercase == 'да':
    chars += uppercase_letters
if is_lowercase == 'да':
    chars += lowercase_letters
if is_punctuation == 'да':
    chars += punctuation
if is_clear == 'да':
    for c in chars:
        if c in non_clear:
            chars = chars.replace(c, '')


for i in range(n):
    print(generate_password(length, chars))



# объявление функции
def is_palindrome(text):
    simbols = ',.!?-'
    tmp = "".join(c for c in text if c.isalpha()).lower()
    if tmp[:] == tmp[::-1]:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))

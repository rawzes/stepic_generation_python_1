# объявление функции
def is_correct_bracket(text):
    if len(text) % 2 != 0:
        return False

    count = 0

    for i in range(len(text)):
        if text[i] == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    if count == 0:
        return True
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))

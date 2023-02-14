# объявление функции
def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1

    if count == 0 or count >= 2:
        return False
    else:
        return True


# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))

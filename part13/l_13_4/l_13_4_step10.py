# объявление функции
def find_all(target, symbol):
    results = []
    for i in range(len(target)):
        if target.find(symbol, i, i+1) != -1:
            results.append(target.find(symbol, i, i+1))
    return results


# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))

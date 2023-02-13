# объявление функции
def get_factors(num):
    results = []
    for i in range(1, num + 1):
        if num % i == 0:
            results.append(i)
    return results


# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))

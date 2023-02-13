# объявление функции
def number_of_factors(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count
def get_factors(num):
    results = []
    for i in range(1, num + 1):
        if num % i == 0:
            results.append(i)
    return results

# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))
print(len(get_factors(n)))

'''
def get_factors(num):
    results = []
    for i in range(1, num + 1):
        if num % i == 0:
            results.append(i)
    return results

'''
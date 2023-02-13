# объявление ункции

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_next_prime(num):
    result = num + 1
    while not is_prime(result):
        result += 1
    return result


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))

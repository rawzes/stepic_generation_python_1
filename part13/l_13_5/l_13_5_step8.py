# объявление функции

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def is_valid_password(password):
    values = password.split(':')
    if len(values) != 3:
        return False

    if values[0][:] != values[0][::-1]:
        return False

    if not is_prime(int(values[1])):
        return False

    if int(values[2]) % 2 == 1:
        return False

    return True


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))

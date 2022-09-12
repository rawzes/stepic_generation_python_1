n = int(input())

if 0 <= n <= 36:
    if 1 <= n <= 10:
        if n % 2 == 0:
            print('черный')
        else:
            print('красный')
    elif 10 < n <= 18:
        if n % 2 == 0:
            print('красный')
        else:
            print('черный')
    elif 18 < n <= 28:
        if n % 2 == 0:
            print('черный')
        else:
            print('красный')
    elif 28 < n <= 36:
        if n % 2 == 0:
            print('красный')
        else:
            print('черный')
    else:
        print('зеленый')
else:
    print('ошибка ввода')
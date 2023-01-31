# объявление функции
def get_days(month):
    if month == 2:
        return 28
    elif month < 8 and month % 2 == 1:
        return 31
    elif month < 8 and month % 2 == 0:
        return 30
    elif month > 7 and month % 2 == 0:
        return 31
    else:
        return 30

'''
variant 2
def get_days(month):
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return m[month - 1]
'''


# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))

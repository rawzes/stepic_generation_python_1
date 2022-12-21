numbers = [2, 4, 6, 8, 10]
languages = ['Python', 'C#', 'C++', 'Java']

print(f'Length of numbers is {len(numbers)}')
print(len(languages))

#  Оператор in позволяет проверить, содержит ли список некоторый элемент.

if 2 in numbers:
    print('Число содержится в списке')
else:
    print('Число не содержится в списке')

numbers = [2, 4, 6, 8, 10]

if 0 not in numbers:
    print('Список numbers не содержит нулей')

#  print(numbers[17])  IndexError: list index out of range
print(numbers[1:3])  # [4, 6]
print(numbers[2:5])  # [6, 8, 10]

fruits = ['apple', 'apricot', 'banana', 'cherry', 'kiwi', 'lemon', 'mango']
print(len(fruits))
fruits[1] = 'абрикос'
print(fruits)
print(len(fruits))

fruits[1:3] = ['абрикос', 'бананы']
print(fruits)  # ['apple', 'абрикос', 'бананы', 'cherry', 'kiwi', 'lemon', 'mango']
print(len(fruits))  # 7

fruits[1:3] = 'test'
print(fruits)  # ['apple', 't', 'e', 's', 't', 'cherry', 'kiwi', 'lemon', 'mango']
print(len(fruits))  # 9


print([1, 2, 3, 4] + [5, 6, 7, 8])
print(len([7, 8] * 10))  # 20 elements
print([0] * 10)

a = [1, 2, 3, 4]
b = [7, 8]
a += b   # добавляем к списку a список b
b *= 5   # повторяем список b 5 раз

print(a)  # [1, 2, 3, 4, 7, 8]
print(b)  # [7, 8, 7, 8, 7, 8, 7, 8, 7, 8]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Сумма всех элементов списка =', sum(numbers))
numbers = [3, 4, 10, 3333, 12, -7, -5, 4]
print('Минимальный элемент =', min(numbers))
print('Максимальный элемент =', max(numbers))


numbers = [1, 2, 3, 4, 5, 6, 7]
numbers[1] = 101     # изменяем 2 элемент (по индексу 1) списка
print(numbers)  # [1, 101, 3, 4, 5, 6, 7]


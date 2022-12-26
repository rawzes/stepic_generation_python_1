numbers = [1, 3, 4, 7, 9]
numbers.append(16)  # add value to the end of the list
numbers.append(48)
print(numbers)

numbers = []  # создаем пустой список

numbers.append(1)
numbers.append(2)
numbers.append(3)

print(numbers)  # [1, 2, 3]

''''

numbers = []  # создаем пустой список
numbers[0] = 1  # IndexError: list assignment index out of range
numbers[1] = 2
numbers[2] = 3

print(numbers)
'''

numbers = [0, 2, 4, 6]
odds = [1, 3, 5]
numbers.extend(odds)  # extend list by another list
print(numbers)

words1 = ['iq option', 'stepik', 'beegeek']
words2 = ['iq option', 'stepik', 'beegeek']

words1.append('python')
words2.extend('python')  # string as list splits on characters

print(words1)
print(words2)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[5]    # удаляем элемент имеющий индекс 5
print(numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[2:7]    # удаляем элементы с 2 по 6 включительно
print(numbers)  # [1, 2, 8, 9]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[::2]
print(numbers)  # [2, 4, 6, 8]

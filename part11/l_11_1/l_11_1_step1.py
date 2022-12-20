numbers = [2, 4, 6, 8]
languages = ['Python', 'C#', 'C++', 'Java']
print(languages[0])
print(numbers[0])

info = ['Roma', 1992, 98.9]
print(info)


# empty lists
my_list1 = []
my_list2 = list()

numbers = list(range(5))
print(type(numbers))  # <class 'list'>
print(type(range(6)))  # <class 'range'>


even_numbers = list(range(0, 10, 2))  # список содержит четные числа 0, 2, 4, 6, 8
odd_numbers = list(range(1, 10, 2))   # список содержит нечетные числа 1, 3, 5, 7, 9


s = 'test string'
chars = list(s)
print(chars)

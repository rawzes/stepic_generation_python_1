n = int(input())
list_values = []
for i in range(n):
    list_values.append(int(input()))

result = []
for item in list_values:
    if item != min(list_values) and item != max(list_values):
        result.append(item)
print(*result, sep='\n')


'''
1) del имя_списка[имя_списка.index(max(имя_списка))] - находим максимум, находим его индекс, удаляме по индексу.

2) имя_списка.remove(max(имя_списка)) - здесь проще, находим максимум и его удаляем, передавая как аргумент.
'''
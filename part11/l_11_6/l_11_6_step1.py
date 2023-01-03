'''
list.append(x)Добавляет элемент в конец списка

list.extend(L)Расширяет список list, добавляя в конец все элементы списка L

list.insert(i, x)Вставляет на i-ый элемент значение x

list.remove(x) Удаляет первый элемент в списке, имеющий значение x. ValueError, если такого элемента не существует

list.pop([i])Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент

list.index(x, [start [, end]])Возвращает положение первого элемента со значением x (при этом поиск ведется от start до end)

list.count(x)Возвращает количество элементов со значением x

list.sort([key=функция])Сортирует список на основе функции

list.reverse()Разворачивает список

list.copy()Поверхностная копия списка

list.deepcopy(x) - возвращает полную копию x.

list.clear()Очищает список

'''

names = ['Gvido', 'Roman', 'Timur']
names.insert(45645, 'TEst')
print(names)  # ['Gvido', 'Roman', 'Timur', 'TEst']
names.insert(-9999, 'D')
print(names)  # ['D', 'Gvido', 'Roman', 'Timur', 'TEst']
names.insert(-2, 'D')
print(names)  # ['D', 'Gvido', 'Roman', 'D', 'Timur', 'TEst']

names = ['Gvido', 'Roman', 'Timur']
position = names.index('Timur')
print(position)  # 2

'''
ValueError: 'Timu2r' is not in list
position = names.index('Timu2r')  
'''

names = ['Gvido', 'Roman' , 'Timur']
if 'Anders' in names:
    position = names.index('Anders')
    print(position)
else:
    print('Такого значения нет в списке')

names = ['Gvido', 'Roman', 'Timur']

'''
ValueError: list.remove(x): x not in list
names.remove('sfsdf')
print(names)
'''
'''
remove() удаляет только перый элемент, для удаления всех, можно использовать remove() + while + in
'''
names.remove('Roman')
print(names)

names = ['Gvido', 'Roman', 'Timur']
# item = names.pop(-9)  IndexError: pop index out of range
item = names.pop()  # selects last value in list
print(item)
print(names)

names = ['Timur', 'Gvido', 'Roman', 'Timur', 'Anders', 'Timur']
cnt1 = names.count('Timur')
cnt2 = names.count('Gvido')
cnt3 = names.count('Josef')

print(cnt1)
print(cnt2)
print(cnt3)
names.reverse()
print(names)
'''
Существует большая разница между вызовом метода names.reverse() и использованием среза names[::-1].
 Метод reverse() меняет порядок элементов на обратный в текущем списке, а срез создает копию списка, 
 в котором элементы следуют в обратном порядке.
'''

names.clear()
print(names)

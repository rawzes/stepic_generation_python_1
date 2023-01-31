
def print_texas():
    global birds
    birds = 5000
    print('В Техасе обитает', birds, 'птиц.')


def print_california():
    print('В Калифорнии обитает', birds, 'птиц.')


print_texas()
print_california()

'''
def print_texas():
    global birds
    birds = 5001
    print('В Техасе обитает', birds, 'птиц.')
def print_california():
    print('В Калифорнии обитает', birds, 'птиц.')

birds = 100

print_texas()
birds = 200  # добавили здесь новое значение переменной
print_california()
print(birds)
И результат:

В Техасе обитает 5001 птиц.
В Калифорнии обитает 200 птиц.
200
'''

x = 5


def add():
    x = 3
    x = x + 5
    print(x)


add()
print(x)

# объявление функции
def print_fio(name, surname, patronymic):
    print(surname[:1].upper() + name[:1].upper() + patronymic[:1].upper())
    # variant 2
    print((surname[0] + name[0] + patronymic[0]).upper())

# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)

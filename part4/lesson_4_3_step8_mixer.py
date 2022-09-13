color1 = input()
color2 = input()

if color1 == 'красный':
    if color2 == 'красный':
        print('красный')
    elif color2 == 'синий':
        print('фиолетовый')
    elif color2 == 'желтый':
        print('оранжевый')
    else:
        print('ошибка цвета')
elif color1 == 'синий':
    if color2 == 'синий':
        print('синий')
    elif color2 == 'желтый':
        print('зеленый')
    elif color2 == 'красный':
        print('фиолетовый')
    else:
        print('ошибка цвета')
elif color1 == 'желтый':
    if color2 == 'желтый':
        print('желтый')
    elif color2 == 'красный':
        print('оранжевый')
    elif color2 == 'синий':
        print('зеленый')
    else:
        print('ошибка цвета')
else:
    print('ошибка цвета')





#
# if color1 == 'красный' and color2 == 'синий' or color2 == 'красный' and color1 == 'синий':
#     print('фиолетовый')
# elif color1 == 'красный' and color2 == 'желтый' or color2 == 'красный' and color1 == 'желтый':
#     print('оранжевый')
# elif color1 == 'синий' and color2 == 'желтый' or color2 == 'синий' and color1 == 'желтый':
#     print('зеленый')
# elif color1 == color2 == 'красный':
#     print('красный')
# elif color1 == color2 == 'синий':
#     print('синий')
# elif color1 == color2 == 'синий':
#     print('синий')
# elif color1 == color2 == 'желтый':
#     print('желтый')
# else:
#     print('ошибка цвета')

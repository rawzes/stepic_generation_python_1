color1 = input()
color2 = input()

if color1 == 'красный' and color2 == 'синий' or color2 == 'красный' and color1 == 'синий':
    print('фиолетовый')
elif color1 == 'красный' and color2 == 'желтый' or color2 == 'красный' and color1 == 'желтый':
    print('оранжевый')
elif color1 == 'синий' and color2 == 'желтый' or color2 == 'синий' and color1 == 'желтый':
    print('зеленый')
elif color1 == color2 == 'красный':
    print('красный')
elif color1 == color2 == 'синий':
    print('синий')
elif color1 == color2 == 'синий':
    print('синий')
elif color1 == color2 == 'желтый':
    print('желтый')
else:
    print('ошибка цвета')

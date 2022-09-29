import math


a, b, c = float(input()), float(input()), float(input())

d = math.pow(b, 2) - 4 * a * c
if d > 0:
    result1 = (-b + math.sqrt(d)) / (2 * a)
    result2 = (-b - math.sqrt(d)) / (2 * a)
    if result1 < result2:
        print(result1, result2, sep='\n')
    else:
        print(result2, result1, sep='\n')
elif d == 0:
    print(-b / (2 * a))
else:
    print('Нет корней')


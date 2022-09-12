
a, b, c, d = int(input()), int(input()), int(input()), int(input())

if (a == c and b != d):
    print('YES')
elif (a == c and b == d):
    print('YES')
elif (a != c and b == d):
    print('YES')
else:
    print('NO')

# более красивое решение
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if a == c or b == d:
#     print('YES')
# else:
#     print('NO')

# # Год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400.
#
# year = int(input())
#
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print('YES')
# else:
#     print('NO')


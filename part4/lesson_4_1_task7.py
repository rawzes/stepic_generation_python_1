a = int(input())
b = int(input())
c = int(input())
d = int(input())

min_1 = a
min_2 = c

if a < b:
    min_1 = a
else:
    min_1 = b

if c < d:
    min_2 = c
else:
    min_2 = d

if min_1 < min_2:
    print(min_1)
else:
    print(min_2)

# a = int(input())
# b = int(input())
#
# if a < b:
#     print(a)
# else:
#     print(b)

# a = int(input())
# b = int(input())
# c = int(input())
#
# if b - a == c - b:
#     print('YES')
# else:
#     print('NO')
#

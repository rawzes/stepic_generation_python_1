
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

if a1 < a2:
    left_border = a2
else:
    left_border = a1

if b1 < b2:
    right_border = b1
else:
    right_border = b2

if left_border > right_border:
    print('пустое множество')
elif left_border == right_border:
    print(left_border)
else:
    print(left_border, right_border)

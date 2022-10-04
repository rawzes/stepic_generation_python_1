
is_oven = False
for i in range(10):
    num = int(input())
    if num % 2 == 0:
        is_oven = True
    else:
        is_oven = False
        break

if is_oven:
    print('YES')
else:
    print('NO')


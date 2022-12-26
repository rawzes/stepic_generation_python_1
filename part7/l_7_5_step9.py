n = int(input())

flag = True
last = n % 10
while n != 0:
    if last != n % 10:
        flag = False
    last = n % 10
    n = n // 10

if flag:
    print('YES')
else:
    print('NO')

n = int(input())

flag = True
last_digit = n % 10

while n != 0:
    digit = n % 10
    if last_digit > digit:
        flag = False
    last_digit = digit
    n = n // 10

if flag:
    print('YES')
else:
    print('NO')

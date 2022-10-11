n = int(input())

while n != 0:
    last_number = n % 10
    print(last_number, end='')
    n = n // 10

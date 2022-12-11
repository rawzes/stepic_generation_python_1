n = int(input())

while n > 99:
    last_digit = n % 10
    n = n // 10
    if n < 99:
        print(last_digit)

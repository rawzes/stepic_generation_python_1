n = int(input())

c = n % 10
b = n // 10 % 10
a = n // 100
avg = a + b + c - max(a, b, c) - min(a, b, c)
if max(a, b, c) - min(a, b, c) == avg:
    print('Число интересное')
else:
    print('Число неинтересное')

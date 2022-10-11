n = int(input())
max = min = n % 10
while n != 0:
    last = n % 10
    if last >= max:
        max = last
    if last <= min:
        min = last
    n = n // 10

print('Максимальная цифра равна', max)
print('Минимальная цифра равна', min)

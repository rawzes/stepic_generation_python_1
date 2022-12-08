n = int(input())
value = 1
for i in range(n):
    for j in range(0, i + 1, 1):
        print(value, end=' ')
        value += 1
    print()

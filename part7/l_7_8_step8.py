n = int(input())

for i in range(1, n + 1):
    for j in range(i):
        if i + j > n:
            break
        print('*', end='')
    print()

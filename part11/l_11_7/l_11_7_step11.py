print(*[int(v) ** 2 for v in input().split() if int(v) ** 2 % 2 == 0 and int(v) ** 2 % 10 != 4])


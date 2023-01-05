# [print(c, end='') for c in input() if c.isdigit()]

print(*[c for c in input() if c.isdigit()], sep='')

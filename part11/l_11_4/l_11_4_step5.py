n = int(input())
values = []
for i in range(n):
    value = input()
    if value not in values:
        values.append(value)

print(*values, sep='\n')

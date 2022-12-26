n = int(input())
values = []
for i in range(n):
    values.append(int(input()))

del values[1::2]

# results = [i for i in values[::2]]
print(values)

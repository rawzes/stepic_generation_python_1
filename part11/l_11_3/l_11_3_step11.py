n = int(input())
values = []
results = []
for i in range(n):
    values.append(int(input()))

for i in range(1, n):
    results.append(values[i-1] + values[i])

print(results)

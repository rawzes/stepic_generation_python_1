n = int(input())

results = []
for i in range(1, n + 1):
    if n % i == 0:
        results.append(i)

print(results)

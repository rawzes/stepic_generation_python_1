import math
n = int(input())
result = 0

for i in range(1, n + 1):
    result += 1 / i

print(result - math.log(n))

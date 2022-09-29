import math

n, a = float(input()), float(input())

s = (n * math.pow(a, 2))/(4 * math.tan(math.pi / n))
print(s)

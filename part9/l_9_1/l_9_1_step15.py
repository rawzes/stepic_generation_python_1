
a = [x*2 for x in range(1,n)]
print(a)
while n > 0:
    s = str(n % 2) + s
    n = n // 2
print(s)

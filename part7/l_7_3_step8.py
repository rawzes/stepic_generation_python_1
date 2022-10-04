n = int(input())
sum = 0
for i in range(1, n + 1):
    if i*i % 10 == 2 or i*i % 10 == 5 or i*i % 10 == 8:
        sum += i
print(sum)

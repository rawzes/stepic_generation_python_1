a, b = int(input()), int(input())
count = 0
for i in range(a, b + 1):
    if (i * i * i) % 10 == 4 or (i * i * i) % 10 == 9:
        count += 1
print(count)

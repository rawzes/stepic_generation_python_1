a, b = int(input()), int(input())
summ_count = 0
max_x = 0

for x in range(a, b + 1):
    count = 0
    for i in range(1, x + 1):
        if x % i == 0:
            count += i
        if count >= summ_count:
            summ_count = count
            max_x = x
print(max_x, summ_count)

max_negative = -1000000
sum_negative = 0
for _ in range(10):
    x = int(input())
    if x < 0:
        sum_negative += x
        if x >= max_negative:
            max_negative = x

if sum_negative < 0:
    print(sum_negative)
    print(max_negative)
else:
    print('NO')

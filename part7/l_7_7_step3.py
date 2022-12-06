count = 0
multiple = 1
for _ in range(0, 10):
    x = int(input())
    if x >= 0:
        multiple *= x
        count += 1
if count > 0:
    print(count)
    print(multiple)
else:
    print('NO')


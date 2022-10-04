n = int(input())

max1, max2 = -1, -1
for i in range(n):
    num = int(input())
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        max2 = num

print(max1, max2, sep='\n')

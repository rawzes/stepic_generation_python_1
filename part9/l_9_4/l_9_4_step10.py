n = int(input())
count = 0
for i in range(n):
    num = input().count('11')
    if num >= 3:
        count += 1

print(count)

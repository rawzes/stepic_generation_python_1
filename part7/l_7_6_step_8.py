'''
чисел от 5 до 9 включительно;
чисел от 17 до 37 включительно;
чисел от 78 до 87 включительно.
'''

n = int(input())

for i in range(1, n + 1):
    if 5 <= i <= 9:
        continue
    if 17 <= i <= 37:
        continue
    if 78 <= i <= 87:
        continue
    print(i)


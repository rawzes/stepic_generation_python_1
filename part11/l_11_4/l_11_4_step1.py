numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    print(num, end=' ')
print()
print(*numbers)  # 0 1 2 3 4 5 6 7 8 9 10

print(*numbers, sep='\n')

s = 'Python'
print(*s)
print(*s, sep='\n')

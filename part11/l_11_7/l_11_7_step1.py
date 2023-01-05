zeros = []
for i in range(10):
    zeros.append(0)

print(*zeros)
zeros = [1] * 10
print(*zeros)

numbers = []
for i in range(10):
    numbers.append(i)
print(*numbers)

# variant 2 - list comprehension
# [выражение for переменная in последовательность]
numbers = [i for i in range(10)]
print(*numbers)

numbers = [0 for i in range(10)]
print(*numbers)
squares = [i ** 2 for i in range(10)]
cubes = [i ** 3 for i in range(10, 21)]
print(*squares)
print(*cubes)

chars = [c for c in 'abcdfg']
print(chars)

evens = [i for i in range(10) if i % 2 == 0]
print(*evens)  # 0 2 4 6 8


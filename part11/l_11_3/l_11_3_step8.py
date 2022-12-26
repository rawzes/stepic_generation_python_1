# ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
list_values = []
for i in range(1, 27):
    list_values.append(chr(ord('a') + i - 1) * i)

print(list_values)

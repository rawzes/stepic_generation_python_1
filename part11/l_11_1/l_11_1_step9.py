n = int(input())
list2 = list(range(97, 97 + n))
result = []
for i in list2:
    result.append(chr(i))

print(result)


# variant 2

s = ''
for i in range(n):
    s += chr(97 + i)
print(s)
print(list(s))


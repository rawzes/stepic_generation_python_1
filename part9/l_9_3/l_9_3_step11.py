s = input()

count = 0
for i in range(len(s)):
    if s[i] in 'abcdefghijklmnopqrstuvwxyz':
        count += 1
print(count)


# variant2

count = 0
for c in s:
    if c == c.lower():
        count += 1
print(count)

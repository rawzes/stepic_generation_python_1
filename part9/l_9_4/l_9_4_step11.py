s = input()
count = 0
for c in range(len(s)):
    if s[c] in '0123456789':
        count += 1
print(count)

# variant 2
count = 0
for i in range(10):
    count += s.count(str(i))
print(count)


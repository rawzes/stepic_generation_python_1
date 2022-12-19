s = input()

count = 0
char = ''

for c in s:
    if s.count(str(c)) >= count:
        count = s.count(str(c))
        char = c
print(char)

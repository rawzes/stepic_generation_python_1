s = 'Python'
# get first character
print(s[0])
print(s[-6])
print(s[-len(s)])

# get last character
print(s[len(s) - 1])
print(s[-1])

# print(s[17]) IndexError: string index out of range

# examples of iteration

s = 'dfg54g45'
for i in range(len(s)):
    print(s[i])

for c in s:
    print(c)

s = input().split()
for i in range(len(s)):
    s[i] = int(s[i])

s1 = s.copy()
s2 = s.copy()
s1.sort()
s2.sort(reverse=True)
print(*s1)
print(*s2)


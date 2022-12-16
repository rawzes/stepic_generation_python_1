s = input()

l1 = len(s) // 2 + len(s) % 2
l2 = len(s) // 2
print(s[l1:] + s[:l1])

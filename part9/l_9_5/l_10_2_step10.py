s = input()

if s.count('f') == 0:
    print(-2)
elif s.count('f') == 1:
    print(-1)
else:
    index1 = s.index('f')
    print(s.index('f', index1 + 1))

s1, s2, s3 = input(), input(), input()

l1, l2, l3 = len(s1), len(s2), len(s3)
# или через формулу прогрессии (2b-c-a)(2c-b-a)(2a-b-c) = 0
a1 = min(l1, l2, l3)
a3 = max(l1, l2, l3)
a2 = (l1 + l2 + l3) - a1 - a3

if abs(a1 - a2) == abs(a3 - a2):
    print('YES')
else:
    print('NO')

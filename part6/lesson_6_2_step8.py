t1 = input()
t2 = input()
t3 = input()

l1 = len(t1)
l2 = len(t2)
l3 = len(t3)

max = max(l1, l2, l3)
min = min(l1, l2, l3)

if min == l1:
    print(t1)
elif min == l2:
    print(t2)
else:
    print(t3)

if max == l1:
    print(t1)
elif max == l2:
    print(t2)
else:
    print(t3)


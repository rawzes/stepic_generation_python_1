l = [int(i) for i in input().split()]
m = [int(i) for i in input().split()]

result = [l[i] + m[i] for i in range(len(l))]
print(*result, end=' ')

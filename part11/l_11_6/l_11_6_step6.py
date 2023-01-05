s = input()
list_values = s.split()
for i in range(len(list_values)):
    list_values[i] = int(list_values[i])

max_value = max(list_values)
min_value = min(list_values)

max_index = list_values.index(max_value)
min_index = list_values.index(min_value)

list_values[max_index] = min_value
list_values[min_index] = max_value

print(*list_values, end=' ')

'''
variant 2

l = [int(i) for i in input().split()]
x = l.index(min(l))
y = l.index(max(l))
l[x], l[y] = max(l), min(l)
print(*l)

'''
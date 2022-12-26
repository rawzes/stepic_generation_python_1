n = int(input())
list_strings = []
for i in range(n):
    list_strings.append(input())
k = int(input())

for item in list_strings:
    print(item[k-1:k], end='')


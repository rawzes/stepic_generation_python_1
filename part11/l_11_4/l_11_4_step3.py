n = int(input())
list_input = []
list_values = []
for i in range(n):
    list_input.append(int(input()))

for item in list_input:
    list_values.append(item ** 2 + 2 * item + 1)

print(*list_input, sep='\n')
print()
print(*list_values, sep='\n')


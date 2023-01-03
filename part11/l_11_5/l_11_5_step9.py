s = input()

list_values = s.split()
count = 0
for i in range(0, len(list_values)):
    for j in range(i + 1, len(list_values)):
        if list_values[i] == list_values[j]:
            count += 1

print(count)

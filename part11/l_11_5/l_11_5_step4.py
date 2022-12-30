s = input()

list_values = s.split()
for item in list_values:
    print('.'.join(item[0]), end='.')

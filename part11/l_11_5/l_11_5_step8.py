s = input()
separator = input()
print(separator.join(s))

#  variant 2

print(*s, sep=separator)

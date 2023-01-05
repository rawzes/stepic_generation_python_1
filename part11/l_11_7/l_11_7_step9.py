s = input().split()
for w in s:
    print(w)

# variant 2

print(*input().split(), sep='\n')

# variant 3
print(input().replace(" ", "\n"))

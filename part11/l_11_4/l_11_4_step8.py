n = int(input())
positive = []
zero = []
negative = []

for i in range(n):
    value = int(input())
    if value < 0:
        negative.append(value)
    elif value == 0:
        zero.append(value)
    else:
        positive.append(value)

print(*negative, sep='\n')
print(*zero, sep='\n')
print(*positive, sep='\n')

a = int(input())
b = int(input())
c = int(input())

print(max(a, b, c), a+b+c - max(a, b, c) - min(a, b, c), min(a, b, c), sep='\n')


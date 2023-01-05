values = input().split()
values = [int(i) for i in values]

result = [i*i*i for i in values]
for i in result:
    print(i, end=' ')


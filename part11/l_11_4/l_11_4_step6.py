n = int(input())
values = []
for i in range(n):
    values.append(input())

r = input()
for item in values:
    if r.lower() in item.lower():
        print(item)

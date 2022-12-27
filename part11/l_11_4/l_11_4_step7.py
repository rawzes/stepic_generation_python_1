n = int(input())

values = []
for i in range(n):
    values.append(input())

k = int(input())
req = []
for i in range(k):
    req.append(input())

for i in values:
    for j in req:
        if j.lower() not in i.lower():
            break
    else:
        print(i)


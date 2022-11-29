n = 10
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n, end='*')

for i in range(10):
    print(i, end='*')
    if i > 6:
        break

num = int(input())
flag = True
for i in range(2, num):
    print('iteration ' + str(i))
    if num % i == 0:
        flag = False
        break
if flag:
    print('Число простое')
else:
    print('Число не простое')


result = 0
for i in range(10):
    num = int(input())
    if num < 0:
        break
    result += num
print(result)


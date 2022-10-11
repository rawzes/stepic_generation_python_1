n = int(input())

num_count = 0
sum = 0
avg = 0
first = 0
last = n % 10
mult = 1

while n != 0:
    digit = n % 10

    num_count += 1
    sum += digit
    mult *= digit

    n = n // 10

print(sum)
print(num_count)
print(mult)
print(sum / num_count)
print(n)
print(n + last)
'''
сумму его цифр;
количество цифр в нем;
произведение его цифр;
среднее арифметическое его цифр;
его первую цифру;
сумму его первой и последней цифры.
'''

n = int(input())
count_three = 0
count_last = 0
count_odd = 0
sum_numbers_more_5 = 0
mult_more_7 = 1
count_0_and_5 = 0
last = n % 10
while n > 0:
    last_digit = n % 10
    if last_digit == 3:
        count_three += 1
    if last_digit == last:
        count_last += 1
    if last_digit % 2 == 0:
        count_odd += 1
    if last_digit > 5:
        sum_numbers_more_5 += last_digit
    if last_digit > 7:
        mult_more_7 *= last_digit
    if last_digit == 0 or last_digit == 5:
        count_0_and_5 += 1
    n = n // 10

print(count_three)
print(count_last)
print(count_odd)
print(sum_numbers_more_5)
print(mult_more_7)
print(count_0_and_5)

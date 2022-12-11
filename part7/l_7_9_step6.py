n = int(input())
result_sum = 0
for i in range(1, n + 1):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    result_sum += factorial
print(result_sum)

n = int(input())
product = n % 10
while n > 10:
    n //= 10
    digit = n % 10
    product *= digit

print(product)


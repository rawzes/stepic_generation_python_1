s = input()
numbers = s.split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])


for i in range(len(numbers)):
    print('+' * int(numbers[i]))


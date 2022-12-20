n = int(input())
message = input()
for c in message:
    number = ord(c) - n
    if number < 97:
        number += 26
    print(chr(number), end='')

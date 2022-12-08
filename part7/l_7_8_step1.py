for seconds in range(60):
    print(seconds)

for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours, ':', minutes, ':', seconds)


for i in range(8):
    for j in range(6):
        print('*', end='')
    print()


for i in range(0, 10, 2):
    for j in range(i + 1):
        print('*', end='')
    print()

iteration = 0
size = 151
for a in range(1, size):
    a5 = a ** 5
    for b in range(a, size):
        b5 = a5 + b ** 5
        for c in range(b, size):
            c5 = b5 + c ** 5
            for d in range(c, size):
                e5 = c5 + d ** 5
                if round(e5 ** 0.2) ** 5 == e5:
                    print(a + b + c + d + round(e5 ** 0.2))


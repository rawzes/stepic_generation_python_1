for a in range(1, 33):
    for b in range(1, 33):
        for c in range(1, 33):
            for d in range(1, 33):
                if a**3 + b**3 == c**3 + d**3:
                    if a != c and a != d and b != c and b != d:
                        print(a**3 + b**3)

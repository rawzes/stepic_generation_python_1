age = int(input())

if age <= 14:
    print('детство')
elif 14 < age <= 24:
    print('молодость')
elif 25 <= age <= 59:
    print('зрелость')
else:
    print('старость')

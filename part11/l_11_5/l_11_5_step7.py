s = input()

values = s.split('.')
is_IP = False
for item in values:
    if 0 <= int(item) < 256:
        is_IP = True
    else:
        is_IP = False
        break

if is_IP:
    print('ДА')
else:
    print('НЕТ')

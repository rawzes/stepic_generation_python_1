import math

s = input()

base = 16
result = 0
count = 0

# def prepare(s, base):
#
#     return  tmp
#
# s = prepare(s, base)
# for c in s[::-1]:
#     if base == 16:
#         tmp = ''
#         if base == 16:
#             tmp = s.replace('A', '10')
#             tmp = s.replace('F', '15')
#     result += int(c) * math.pow(base, count)
#     count += 1

print(int(s, base))


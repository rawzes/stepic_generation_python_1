m, n = int(input()), int(input())
for i in range(m % 2 - 1 + m, n - 1, -2):
    print(i)

# m, n = int(input()), int(input())
#
# for i in range(m, n - 1, -1):
#     if i % 2 == 1:
#         print(i)

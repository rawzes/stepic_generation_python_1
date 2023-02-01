def quick_merge(list):
    result = []
    for sublist in list:
        result += sublist
    result.sort()
    return result


# считываем данные
n = int(input())
sources = []
for i in range(n):
    tmp = [int(c) for c in input().split()]
    sources.append(tmp)

# вызываем функцию
print(*quick_merge(sources), sep=' ')


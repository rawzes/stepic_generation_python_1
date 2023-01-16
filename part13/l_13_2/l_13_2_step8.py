def draw_triangle(fill, base):
    for i in range(base // 2 + 2):
        print(fill * i)
    for i in range(base // 2 , 0, -1):
        print(fill * i)

fill = input()
base = int(input())
draw_triangle(fill, base)


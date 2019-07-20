ipt = input("請輸入 a, b, c，並以空白分開：").split(' ')
a, b, c = float(ipt[0]), float(ipt[1]), float(ipt[2])

d = b ** 2 - 4 * a * c

if d < 0:
    print('無實數解')
elif d == 0:
    x = (-b) / (2 * a)
    print('重根，x =', x)
else:
    x1 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    x2 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    print('有相異解，x =', (x1, x2))
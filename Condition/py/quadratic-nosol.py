a = 1
b = -4
c = 6.25

x1 = (-b - (b ** 2 - 4 * a * c) ** 0.5)/ (2 * a)
x2 = (-b + (b ** 2 - 4 * a * c) ** 0.5)/ (2 * a)

print("x1 =", x1)
print("x2 =", x2)
print(type(x1), x1)

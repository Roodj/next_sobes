a, b, c = int(input("Введите a: ")), int(input("Введите b: ")), int(input("Введите c: "))

discr = b ** 2 - 4 * a * c

if discr > 0:
    x1 = (-b + discr ** 0.5) / (2 * a)
    x2 = (-b - discr ** 0.5) / (2 * a)
    print((x1, x2))
elif discr == 0:
    x = (-b / (2 * a))
    print(x)
else:
    print("null")

print("Введите число от 1 до 9")
x = int(input())
if 1 <= x <= 3:
    print("Введите строку")
    s = input()
    print("Введите число повторений строки")
    n = int(input())
    for i in range(n):
        print("Строка = ", s)
        print("N = ", i)
elif 4 <= x <= 6:
    print("Введите степень числа")
    m = int(input())
    print(pow(x, m))
elif 7 <= x <= 9:
    for i in range(10):
        x += 1
        print("x = ", x)
else:
    print("Ошибка ввода")





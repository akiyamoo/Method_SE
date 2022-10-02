def first_condition(x):
    if x >= 1 and x <= 3:
        s = input("Введите строку: ")
        n = int(input("Введите число повторов: "))
        for i in range(0, n, 1):
            print(s)
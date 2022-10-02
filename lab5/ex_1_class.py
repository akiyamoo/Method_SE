class Exercise:
    x = None
    s = None
    n = None
    m = None

    def __init__(self, x):
        self.x = x
        if 1 <= x <= 3:
            self.condition_1()
        elif 4 <= x <= 6:
            self.condition_2()
        elif 7 <= x <= 9:
            self.condition_3()
        else:
            print("Ошибка ввода")

    def condition_1(self):
        print("Введите строку")
        self.s = input()
        print("Введите число повторений строки")
        self.n = int(input())
        for i in range(self.n):
            print("Строка = ", self.s)
            print("N = ", i)

    def condition_2(self):
        print("Введите степень числа")
        self.m = int(input())
        print(pow(self.x, self.m))

    def condition_3(self):
        for i in range(10):
            self.x += 1
            print("x = ", self.x)

def third_condition(x):
    if x >= 7 and x <= 9:
        for i in range(0, 10, 1):
            x = x + 1
            print(i + 1, "итерация - x =", x)
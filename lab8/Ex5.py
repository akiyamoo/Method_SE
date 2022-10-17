from calendar import monthrange
n = int(input("Введите число: "))

month=1
flag=1

while month<13 and flag:
    days = monthrange(2021, month)[1]
    n -= int(days)
    if n<=0:
        print("Месяц: ", month)
        print("День месяца: ", n+days)
        flag=0
    month+=1


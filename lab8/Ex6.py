from datetime import datetime, date
from calendar import monthrange
print("Текущая дата: ", date.today())

day = int(date.today().day)
month = int(date.today().month)
month -= 1
while month > 0:
    days = monthrange(date.today().year, month)[1]
    day += int(days)
    month -= 1
print("Номер дня в году: ", day)
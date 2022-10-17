from datetime import datetime, date, time, timedelta

now = datetime.today()

n1 = date(2002, 9, 26)
print(n1, "\n")

n2 = date(2022, 10, 17)

print(n2.year, "year")
print(n2.month, "month")
print(n2.day, "day","\n")


n3 = datetime.strptime('2022-10-03', "%Y-%m-%d")
print(n3, "\n")

date1 = date.today()
date2 = date1.replace(month=date1.month - 1)
date3 = date2.replace(year=date1.year + 1)

date4 = date(date3.year, 1, 1)
timedelta = date3 - date4

print("сегоднящняя дата - месяц + год: ",date3)
print("День от ",date3.year, "года: ",timedelta)




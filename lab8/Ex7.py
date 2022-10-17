from datetime import datetime, date
from calendar import monthrange

data=str(input("Введите дату в формате dd.mm.yyyy: "))

a=datetime.strptime(data,"%d.%m.%Y")
b=a.strftime("%B %d, %y")
print(b)


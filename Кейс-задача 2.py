import datetime
from art import *

d = int(input ("Введите день вашего рождения: "))
m = int(input ("Введите месяц вашего рождения: "))
y = int(input ("Введите год вашего рождения: "))
print ('Дата вашего рождения: ')
print (d, m, y, sep = '.' )
date = datetime.datetime(y, m, d)
dayweek = date.weekday()
if dayweek == 0:
    print('День вашего рождения: понедельник')
elif dayweek == 1:
    print('День вашего рождения: вторник')
elif dayweek == 2:
    print('День вашего рождения: среда')
elif dayweek == 3:
    print('День вашего рождения: четверг')
elif dayweek == 4:
    print('День вашего рождения: пятница')
elif dayweek == 5:
    print('День вашего рождения: суббота')
else:
    print('День вашего рождения: воскресенье')

if (y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0):
    print('Ваш год является високосным')
else:
    print('Ваш год не високосный')
today = datetime.date.today()
print(f'Вам {today.year - y - ((today.month, today.day) < (m, d))} лет')
dd = f"{d:02d}"
mm = f"{m:02d}"
yy = f"{y:04d}"
date_str = f"{dd} {mm} {yy}"
print(text2art(date_str))
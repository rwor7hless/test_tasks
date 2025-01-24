from datetime import datetime, timedelta
import locale
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')  # установка локали для вывода месяца


date_str = input("Введите дату (ДД.ММ.ГГГГ): ")
date = datetime.strptime(date_str, "%d.%m.%Y")

first_day = date.replace(day=1) # получаем первый день месяца
next_month = date.replace(day=28) + timedelta(days=4) # получаем следующий месяц
last_day = next_month - timedelta(days=next_month.day) # получаем последний день месяца

print(f"Первый день: {first_day.strftime('%d.%m.%Y')}")
print(f"Последний день: {last_day.strftime('%d.%m.%Y')}")
print(f"Месяц:", date.strftime("%B"))
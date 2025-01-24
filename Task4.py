from datetime import datetime

def get_datetime():
    s = input("Введите дату и время (ДД.ММ.ГГГГ ЧЧ:ММ): ")
    return datetime.strptime(s, "%d.%m.%Y %H:%M")

dt1 = get_datetime()
dt2 = get_datetime()

delta = abs(dt2 - dt1)
seconds = delta.total_seconds()
minutes = seconds // 60
hours = minutes // 60
days = hours // 24

print(f"Разница: {int(days)} дней, {int(hours)} часов, {int(minutes)} минут, {int(seconds)} секунд")
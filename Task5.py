from datetime import datetime

def get_datetime():
    s = input("Введите дату и время (ДД.ММ.ГГГГ ЧЧ:ММ): ")
    return datetime.strptime(s, "%d.%m.%Y %H:%M")

start = get_datetime()
end = get_datetime()
target = get_datetime()

if start <= end:
    is_between = start <= target <= end
else:
    is_between = end <= target <= start

print("Дата в интервале" if is_between else "Дата вне интервала")
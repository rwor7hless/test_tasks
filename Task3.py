from datetime import datetime

datetime_str = input("Введите дату и время (ДД.ММ.ГГГГ ЧЧ:ММ): ") 
dt = datetime.strptime(datetime_str, "%d.%m.%Y %H:%M")
dt = dt.replace(second=0, hour=10) 
print(dt.strftime("%d.%m.%Y %H:%M"))
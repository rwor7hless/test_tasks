from datetime import datetime

def strong_decorator(func):
    def wrapper(self):
        return f"<strong>{func(self)}</strong>"
    return wrapper

class Person:
    def __init__(self, last_name, first_name, birth_year):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_year = birth_year

    def get_full_name(self):
        return f"{self.last_name} {self.first_name}"

    def get_age(self):
        return datetime.now().year - self.birth_year


# Класс наследник с измененным методом вычисления даты
class PersonDays(Person):
    def get_age(self):
        today = datetime.now()
        birth_date = datetime(self.birth_year, 1, 1)
        delta = today - birth_date
        return delta.days
    

    @strong_decorator
    def get_full_name(self):
        return super().get_full_name() # Возьмем функцию юзера из базового класса и передадим ее в декоратор

person = Person("Бобрышев", "Роман1", 2002)
print(person.get_age())  # Возраст в годах

person_days = PersonDays("Бобрышев", "Роман2", 2002)
print(person_days.get_age())  # Возраст в днях
 
print(person.get_full_name())  # Вывод юзера в формате без декоратора 
print(person_days.get_full_name()) # Вывод юзера в формате с декоратором

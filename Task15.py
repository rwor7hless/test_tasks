from datetime import datetime

def get_checker():
    current_date = datetime.now()
    day_parity = current_date.day % 2  # 0 - четный день, 1 - нечетный

    def check_good(weight):
        if day_parity == 0:
            return 1000 <= weight <= 1100  # Контроллер 1
        else:
            return 950 <= weight <= 1050   # Контроллер 2

    return check_good

products = [950, 1000, 1050, 1100]
check_good = get_checker()
filtered_products = [weight for weight in products if check_good(weight)]

print("Пропущенны товары с весами:", filtered_products)
orders = [["Товар1", 1, 500], ["Товар3", 7, 1000], ["Товар2", 6, 900], ["Товар3", 6, 900], ["Товар3", 6, 900], ["Товар4", 6, 900]]

# Разделяем список на две части
half = len(orders) // 2
part1 = orders[:half]
part2 = orders[half:]

# Создаем списки уникальных товаров
list1 = list(set(item[0] for item in part1))
list2 = list(set(item[0] for item in part2))

print("Список 1:", list1)
print("Список 2:", list2)
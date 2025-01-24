orders = [["Товар1", 1, 500], ["Товар3", 7, 1000], ["Товар2", 6, 900], ["Товар3", 6, 900], ["Товар3", 6, 900], ["Товар4", 6, 900], ["Товар2",10, 120]]

# Сортировка по товару
sorted_by_name = sorted(orders, key=lambda x: x[0])
# Сортировка по сумме
sorted_by_total = sorted(orders, key=lambda x: x[1] * x[2])

print("Сортировка по товару:")
for item in sorted_by_name:
    print(item)

print("\nСортировка по сумме:")
for item in sorted_by_total:
    print(item, "Total cost: ", item[1] * item[2])
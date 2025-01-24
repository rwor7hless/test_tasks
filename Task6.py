orders = [["Товар1", 1, 500], ["Товар2", 7, 1000], ["Товар1", 6, 900]]

total = {}
for item in orders:
    name, qty, price = item
    total[name] = total.get(name, 0) + qty * price

print(total)
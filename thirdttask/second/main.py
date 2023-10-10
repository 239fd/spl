filename = "prices.txt"

total_cost = 0

with open(filename, "r") as file:
    for line in file:
        parts = line.strip().split()

        if len(parts) == 3:
            try:
                quantity = int(parts[1])
                unit_price = float(parts[2])

                line_cost = quantity * unit_price

                total_cost += line_cost
            except ValueError:
                print("Ошибка при обработке строки:", line)
        else:
            print("Некорректный формат строки:", line)

print(f"Общая стоимость заказа: {total_cost}")

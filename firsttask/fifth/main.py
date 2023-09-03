def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False
def is_not_text(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
def menu():
    print(
        "******************\nЮвелирный магазин\n1.Описание\n2.Цена\n3.Количество\n4.Всю информацию\n5.Покупка\n6.До свидания\n******************")
def second_menu():
    print(
        "******************\nЮвелирный магазин\n1.Кольцо\n2.Колье\n3.Браслет\n4.Серьги\n5.Цепь\n6.Назад\n******************")
list_ring = ["Золото", "1000", "50"]
list_necklace = ["Золото", "2000", "40"]
list_wirstband = ["Серебро", "500", "10"]
list_earrings = ["Золото", "750", "70"]
list_chains = ["Платина", "5000", "5"]
dictionary = {
        "Кольцо": list_ring,
        "Колье": list_necklace,
        "Браслет": list_wirstband,
        "Серьги": list_earrings,
        "Цепь": list_chains
}
while True:
    menu()
    choice = input("Выберите пункт меню: ")
    while not is_int(choice) or int(choice) > 6 or int(choice) < 1:
        choice = input("Некорректный ввод, попробуйте снова: ")
    match choice:
        case "1":
            second_menu()
            number = input("Выберите пункт меню: ")
            while not is_int(number) or int(number) > 6 or int(number) < 1:
                number = input("Некорректный ввод, попробуйте снова: ")
            match number:
                case "1":
                    print(f"Материал изделия: {list_ring[0]}")
                case "2":
                    print(f"Материал изделия: {list_necklace[0]}")
                case "3":
                    print(f"Материал изделия: {list_wirstband[0]}")
                case "4":
                    print(f"Материал изделия: {list_earrings[0]}")
                case "5":
                    print(f"Материал изделия: {list_chains[0]}")
                case "6":
                    print("Возращаемся...")
        case "2":
            second_menu()
            number = input("Выберите пункт меню: ")
            while not is_int(number) or int(number) > 6 or int(number) < 1:
                number = input("Некорректный ввод, попробуйте снова: ")
            match number:
                case "1":
                    print(f"Цена изделия: {list_ring[1]}")
                case "2":
                    print(f"Цена изделия: {list_necklace[1]}")
                case "3":
                    print(f"Цена изделия: {list_wirstband[1]}")
                case "4":
                    print(f"Цена изделия: {list_earrings[1]}")
                case "5":
                    print(f"Цена изделия: {list_chains[1]}")
                case "6":
                    print("Возращаемся...")
        case "3":
            second_menu()
            number = input("Выберите пункт меню: ")
            while not is_int(number) or int(number) > 6 or int(number) < 1:
                number = input("Некорректный ввод, попробуйте снова: ")
            match number:
                case "1":
                    print(f"Количество изделия: {list_ring[2]} шт.")
                case "2":
                    print(f"Количество изделия: {list_necklace[2]} шт.")
                case "3":
                    print(f"Количество изделия: {list_wirstband[2]} шт.")
                case "4":
                    print(f"Количество изделия: {list_earrings[2]} шт.")
                case "5":
                    print(f"Количество изделия: {list_chains[2]} шт.")
                case "6":
                    print("Возращаемся...")
        case "4":
            second_menu()
            number = input("Выберите пункт меню: ")
            while not is_int(number) or int(number) > 6 or int(number) < 1:
                number = input("Некорректный ввод, попробуйте снова: ")
            match number:
                case "1":
                    print(f"Материал изделия: {list_ring[0]}, цена изделия: {list_ring[1]}, количетсво изделия: {list_ring[2]} шт.")
                case "2":
                    print(f"Материал изделия: {list_necklace[0]}, цена изделия: {list_necklace[1]}, количетсво изделия: {list_necklace[2]} шт.")
                case "3":
                    print(f"Материал изделия: {list_wirstband[0]}, цена изделия: {list_wirstband[1]}, количетсво изделия: {list_wirstband[2]} шт.")
                case "4":
                    print(f"Материал изделия: {list_earrings[0]}, цена изделия: {list_earrings[1]}, количетсво изделия: {list_earrings[2]} шт.")
                case "5":
                    print(f"Материал изделия: {list_chains[0]}, цена изделия: {list_chains[1]}, количетсво изделия: {list_chains[2]} шт.")
                case "6":
                    print("Возращаемся...")
        case "5":
            cost = 0
            second_menu()
            name = input("Введите название пункта меню: ")
            while is_not_text(name) or len(name) == 0 or not name.isalpha() or not name == "Кольцо" or not name == "Колье" or not name == "Браслет" or not name == "Серьги" or not name == "Цепь":
                name = input("Некорректный ввод, попробуйте снова: ")
            match name:
                case "Кольцо":
                    amount = input("Введите количество: ")
                    while not is_int(amount) or int(amount) > int(list_ring[2]):
                        amount = input("Некорректный ввод, попробуйте снова: ")
                    result = str(int(list_ring[2]) - int(amount))
                    list_ring.insert(2,result)
                    cost += int(amount) * int(list_ring[1])
                    print(f"В вашу корзину добавлены кольца на стоимость: {cost}")
                case "Колье":
                    amount = input("Введите количество: ")
                    while not is_int(amount) or amount > int(list_necklace[2]):
                        amount = input("Некорректный ввод, попробуйте снова: ")
                    result = str(int(list_necklace[2]) - int(amount))
                    list_necklace.insert(2, result)
                    cost += int(amount) * int(list_necklace[1])
                    print(f"В вашу корзину добавлено колье на стоимость: {cost}")
                case "Браслет":
                    amount = input("Введите количество: ")
                    while not is_int(amount) or amount > int(list_wirstband[2]):
                        amount = input("Некорректный ввод, попробуйте снова: ")
                    result = str(int(list_wirstband[2]) - int(amount))
                    list_wirstband.insert(2, result)
                    cost += int(amount) * int(list_wirstband[1])
                    print(f"В вашу корзину добавлены браслеты на стоимость: {cost}")
                case "Серьги":
                    amount = input("Введите количество: ")
                    while not is_int(amount) or amount > int(list_earrings[2]):
                        amount = input("Некорректный ввод, попробуйте снова: ")
                    result = str(int(list_earrings[2]) - int(amount))
                    list_earrings.insert(2, result)
                    cost += int(amount) * int(list_earrings[1])
                    print(f"В вашу корзину добавлены серьги на стоимость: {cost}")
                case "Цепь":
                    amount = input("Введите количество: ")
                    while not is_int(amount) or amount > int(list_chains[2]):
                        amount = input("Некорректный ввод, попробуйте снова: ")
                    result = str(int(list_chains[2]) - int(amount))
                    list_chains.insert(2, result)
                    cost += int(amount) * int(list_chains[1])
                    print(f"В вашу корзину добавлены цепи на стоимость: {cost}")
                case "n":
                    print("Выходим...")
                    break
        case "6":
            print("До свидания")
            break

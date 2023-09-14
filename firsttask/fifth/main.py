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
        "******************\nJewelry\n1.Description\n2.Price\n3.Quantity\n4.All information\n5.Purchase\n6.Bye\n******************")
def second_menu():
    print(
        "******************\nJewelry\n1.Ring\n2.Necklace\n3.Wirstband\n4.Earrings\n5.Chain\n6.Back\n******************")
list_ring = ["Gold", "1000", "50"]
list_necklace = ["Gold", "2000", "40"]
list_wirstband = ["Silver", "500", "10"]
list_earrings = ["Gold", "750", "70"]
list_chains = ["Platinum", "5000", "5"]
dictionary = {
        "Ring": list_ring,
        "Necklace": list_necklace,
        "Wirstband": list_wirstband,
        "Earrings": list_earrings,
        "Chain": list_chains
}
list_cart = []
while True:
    menu()
    choice = input("Choose: ")
    while not is_int(choice) or int(choice) > 6 or int(choice) < 1:
        choice = input("Invalid input, try again: ")
    match choice:
        case "1":
            second_menu()
            number = input("Choose: ")
            while not is_int(number) or int(number) > 6 or int(number) < 1:
                number = input("Invalid input, try again: ")
            match number:
                case "1":
                    print(f"Product material: {list_ring[0]}")
                case "2":
                    print(f"Product material: {list_necklace[0]}")
                case "3":
                    print(f"Product material: {list_wirstband[0]}")
                case "4":
                    print(f"Product material: {list_earrings[0]}")
                case "5":
                    print(f"Product material: {list_chains[0]}")
                case "6":
                    print("Back...")
        case "2":
            second_menu()
            number = input("Choose: ")
            while not is_int(number) or int(number) > 6 or int(number) < 1:
                number = input("Invalid input, try again: ")
            match number:
                case "1":
                    print(f"Product price: {list_ring[1]}")
                case "2":
                    print(f"Product price: {list_necklace[1]}")
                case "3":
                    print(f"Product price: {list_wirstband[1]}")
                case "4":
                    print(f"Product price: {list_earrings[1]}")
                case "5":
                    print(f"Product price: {list_chains[1]}")
                case "6":
                    print("Back...")
        case "3":
            second_menu()
            number = input("Choose: ")
            while not is_int(number) or int(number) > 6 or int(number) < 1:
                number = input("Invalid input, try again: ")
            match number:
                case "1":
                    print(f"{list_ring[2]} pieces of rings")
                case "2":
                    print(f"{list_necklace[2]} pieces of rings")
                case "3":
                    print(f"{list_wirstband[2]} pieces of wirstbands")
                case "4":
                    print(f"{list_earrings[2]} pieces of earrings")
                case "5":
                    print(f"{list_chains[2]} pieces of chains")
                case "6":
                    print("Back...")
        case "4":
            second_menu()
            number = input("Choose: ")
            while not is_int(number) or int(number) > 6 or int(number) < 1:
                number = input("Invalid input, try again: ")
            match number:
                case "1":
                    print(f"Product material: {list_ring[0]}, product price: {list_ring[1]}, {list_ring[2]} pieces of rings")
                case "2":
                    print(f"Product material: {list_necklace[0]}, product price: {list_necklace[1]}, {list_necklace[2]} pieces of rings")
                case "3":
                    print(f"Product material: {list_wirstband[0]}, product price: {list_wirstband[1]}, {list_wirstband[2]} pieces of rings")
                case "4":
                    print(f"Product material: {list_earrings[0]}, product price: {list_earrings[1]}, {list_earrings[2]} pieces of rings")
                case "5":
                    print(f"Product material: {list_chains[0]}, product price: {list_chains[1]}, {list_chains[2]} pieces of rings")
                case "6":
                    print("Back...")
        case "5":
            second_menu()
            name = input("Choose: ")
            set = 'Ring Necklace Wirstband Earrings Chain'
            while name not in set:
                name = input("Invalid input, try again: ")
            match name:
                case "Ring":
                    cost = 0
                    amount = input("Input quantity: ")
                    while not is_int(amount) or int(amount) > int(list_ring[2]):
                        amount = input("Invalid input, try again: ")
                    result = str(int(list_ring[2]) - int(amount))
                    list_ring.insert(2,result)
                    cost += int(amount) * int(list_ring[1])
                    list_cart += "Ring", amount, cost
                case "Necklace":
                    cost = 0
                    amount = input("Input quantity: ")
                    while not is_int(amount) or int(amount) > int(list_necklace[2]):
                        amount = input("Invalid input, try again: ")
                    result = str(int(list_necklace[2]) - int(amount))
                    list_necklace.insert(2, result)
                    cost += int(amount) * int(list_necklace[1])
                    list_cart += "Necklace", amount, cost
                case "Wirstband":
                    cost = 0
                    amount = input("Input quantity: ")
                    while not is_int(amount) or int(amount) > int(list_wirstband[2]):
                        amount = input("Invalid input, try again: ")
                    result = str(int(list_wirstband[2]) - int(amount))
                    list_wirstband.insert(2, result)
                    cost += int(amount) * int(list_wirstband[1])
                    list_cart += "Wirstband", amount, cost
                case "Earrings":
                    cost = 0
                    amount = input("Input quantity: ")
                    while not is_int(amount) or int(amount) > int(list_earrings[2]):
                        amount = input("Invalid input, try again: ")
                    result = str(int(list_earrings[2]) - int(amount))
                    list_earrings.insert(2, result)
                    cost += int(amount) * int(list_earrings[1])
                    list_cart += "Earrings", amount, cost
                case "Chain":
                    cost = 0
                    amount = input("Input quantity: ")
                    while not is_int(amount) or int(amount) > int(list_chains[2]):
                        amount = input("Invalid input, try again: ")
                    result = str(int(list_chains[2]) - int(amount))
                    list_chains.insert(2, result)
                    cost += int(amount) * int(list_chains[1])
                    list_cart += "Chain", amount, cost
                case "n":
                    if(len(list_cart) == 0):
                        print("Your cart is empty")
                        break
                    else:
                        total = 0;
                        print("Your cart:")
                        for i in range(0,len(list_cart),3):
                            print(f"Product: {list_cart[i]}, amount: {list_cart[i+1]}, price: {list_cart[i+2]}")
                        for i in range(2,len(list_cart), 3):
                            total+=list_cart[i]
                        print(f"Total price {total}")
                        print("Back...")
                    break
        case "6":
            print("Bye")
            break

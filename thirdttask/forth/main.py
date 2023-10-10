import json

filename = "firms.txt"

firms_list = []

total_profit = 0
num_profitable_firms = 0

with open(filename, "r") as file:
    for line in file:
        parts = line.strip().split()

        if len(parts) == 4:
            firm_name, ownership_form, revenue, expenses = parts
            revenue = int(revenue)
            expenses = int(expenses)

            profit = revenue - expenses

            firm_data = {firm_name: profit}
            firms_list.append(firm_data)

            if profit > 0:
                total_profit += profit
                num_profitable_firms += 1

average_profit = total_profit / num_profitable_firms if num_profitable_firms > 0 else 0

average_profit_dict = {"average_profit": average_profit}

firms_list.append(average_profit_dict)

with open("firms.json", "w") as json_file:
    json.dump(firms_list, json_file, ensure_ascii=False, indent=4)

print(firms_list)

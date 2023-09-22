def process_input(input_data):
    if isinstance(input_data, set):
        result = 1
        for num in input_data:
            if isinstance(num, (int, float)):
                result *= num
        return result

    elif isinstance(input_data, list):
        input_data = [x for x in input_data if x != 0]

        positive_count = 0
        result = 1
        for num in input_data:
            if isinstance(num, (int, float)) and num > 0:
                positive_count += 1
                if positive_count == 1:
                    first_positive = num
                elif positive_count == 2:
                    result = first_positive * num
                    break
        return result

    elif isinstance(input_data, int):
        return len(str(abs(input_data)))

    elif isinstance(input_data, str):
        num_count = 0
        current_num = ''
        for char in input_data:
            if char.isdigit():
                current_num += char
            elif current_num:
                num_count += 1
                current_num = ''
        if current_num:
            num_count += 1
        return num_count

    else:
        return "Не поддерживаемый тип данных"

print(process_input({2, 3, 4}))
print(process_input([1, 0, 3, 5, 2, -4, 7]))
print(process_input(12345))
print(process_input("abc123def456gh7"))
print(process_input(True))

with open("F1.txt", "w") as f1:
    line_count = 0
    max_vowels_count = 0
    line_number_with_max_vowels = None

    while True:
        line = input("Введите строку (пустая строка для завершения): ")

        if not line:
            break

        f1.write(line + "\n")

        vowels_count = sum(1 for char in line.lower() if char in "aeiouаеёиоуыэюя")

        if vowels_count > max_vowels_count:
            max_vowels_count = vowels_count
            line_number_with_max_vowels = line_count

        line_count += 1

with open("F1.txt", "r") as f1, open("F2.txt", "w") as f2:
    line_number = 0
    for line in f1:
        if line_number != line_number_with_max_vowels:
            f2.write(line)
        line_number += 1

print(f"Номер строки с максимальным количеством гласных: {line_number_with_max_vowels + 1}")

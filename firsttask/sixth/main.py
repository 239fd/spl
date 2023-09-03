def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False
Amount = int(input('Количество элементов множеств? '))
while not is_int(Amount):
    input("Неккоректный ввод, повторите снова: ")
firstSet = set()
print("Введите элементы первого множества: ")
for i in range(Amount):
    number = input()
    while not is_int(number):
        input("Неккоректный ввод, повторите снова: ")
    firstSet.add(number)
secondSet = set()
print("Введите элементы второго множества: ")
for i in range(Amount):
    number = input()
    while not is_int(number):
        input("Неккоректный ввод, повторите снова: ")
    secondSet.add(number)
diff_set = firstSet.difference(secondSet)
print(diff_set)

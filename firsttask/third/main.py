def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

s = input('Введите список: ')
list = s.split()
counter = 0
if(len(s) == 0 or s.isalpha() or not is_number(''.join(list))):
    print("Ошибка")
else:
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] == list[j]:
                counter += 1
    print(counter)

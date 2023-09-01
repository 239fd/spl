s = input('Введите список: ')
list = s.split()
counter = 0
if(len(s) == 0 or s.isalpha()):
    print("Ошибка")
elif('1'.join(list).isdigit()):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] == list[j]:
                counter += 1
    print(counter)
else:
    for i in range(len(list)):
        if (list[i].isalpha()):
            print("Ошибка")

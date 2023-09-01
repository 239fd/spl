while True:
    str = input("Введите строку: ")
    if(str.isdigit() or len(str) == 0):
        print("Ошибка")
        break
    else:
        newstr = str.split(" ")
        count = 0;
        for i in range(len(newstr)):
            if(len(newstr[i]) % 2 != 0):
                count += 1
    print(*[f'{x} - {str.count(x)}' for x in set(str) if x.isalpha()], sep='\n')
    print(f'Количесвто нечетных слов: {count}')

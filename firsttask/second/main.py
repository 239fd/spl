string = input("Введите строку: ")
list = string.split()
count = 0;
def is_text(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
if(is_text(''.join(list)) or len(string) == 0 or not ''.join(list).isalpha()):
    print("Ошибка")
else:
    newstr = string.split(" ")
    for i in range(len(newstr)):
        if(len(newstr[i]) % 2 != 0):
            count += 1
    print(*[f'{x} - {string.count(x)}' for x in set(string) if x.isalpha()], sep='\n')
    print(f'Количесвто нечетных слов: {count}')

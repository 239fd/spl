years = ['Обезьяна', 'Петух', 'Собака', 'Свинья', 'Мышь', 'Бык', 'Тигр', 'Кролик', 'Дракон','Змея', 'Лошадь', 'Овца']
def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

year = input("Введите год: " )
if(not is_int(year) or year < "0"):
    print("Ошибка")
elif(year == "0"):
    print("Конец")
else:
    newyear = int(year)
    for i in range(0, 12):
        if newyear % 12 == i:
            print(years[i])

years = ['Обезьяна', 'Петух', 'Собака', 'Свинья', 'Мышь', 'Бык', 'Тигр', 'Кролик', 'Дракон','Змея', 'Лошадь', 'Овца']

while True:
    year = input("Введите год: " )
    if(year.isalpha() or len(year) == 0 or year < "0"):
        print("Ошибка")
        break
    elif(year == "0"):
        print("Конец")
        break
    else:
        newyear = int(year)
        for i in range(0, 12):
            if newyear % 12 == i:
                print(years[i])

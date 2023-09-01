years = ['Обезьяна', 'Петух', 'Собака', 'Свинья', 'Мышь', 'Бык', 'Тигр', 'Кролик', 'Дракон','Змея', 'Лошадь', 'Овца']

while True:
    year = str(input("Введите год: " ))
    if(year.isalpha()):
        print("Mistake")
        break
    elif(year == "0"):
        print("Конец")
        break
    elif(year < "0"):
        print("Mistake")
        break2
    else:
        newyear = int(year)
        for i in range(0, 12):
            if newyear % 12 == i:
                print(years[i])

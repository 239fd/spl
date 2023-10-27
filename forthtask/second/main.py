class Employee:
    def __init__(self, full_name, experience, hourly_rate, hours_worked):
        self.full_name = full_name
        self.experience = experience
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.base_salary = hourly_rate * hours_worked
        self.bonus = self.calculate_bonus()

    def calculate_bonus(self):
        if self.experience < 1:
            return 0.01 * self.base_salary
        elif self.experience < 3:
            return 0.05 * self.base_salary
        elif self.experience < 5:
            return 0.08 * self.base_salary
        else:
            return 0.15 * self.base_salary

    def calculate_total_salary(self):
        return self.base_salary + self.bonus

    def display_info(self):
        print(f"Имя: {self.full_name}")
        print(f"Стаж: {self.experience} года(лет)")
        print(f"Почасовая ставка: {self.hourly_rate}")
        print(f"Отработанные часы: {self.hours_worked}")
        print(f"Оклад: {self.base_salary}")
        print(f"Премия: {self.bonus}")
        print(f"Заработная плата: {self.calculate_total_salary()}")


employees = []

n = int(input("Введите количество сотрудников: "))
for i in range(n):
    full_name = input("Введите ФИО сотрудника: ")
    experience = int(input("Введите стаж сотрудника (в годах): "))
    hourly_rate = float(input("Введите почасовую заработную плату: "))
    hours_worked = float(input("Введите количество отработанных часов: "))
    employees.append(Employee(full_name, experience, hourly_rate, hours_worked))

for employee in employees:
    employee.display_info()

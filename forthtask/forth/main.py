class BankAccount:
    interest_rate = 0.03  

    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Счет {self.account_number}: Внесено {amount} рублей. Новый баланс: {self.balance} рублей."
        else:
            return "Сумма для внесения должна быть положительной."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Счет {self.account_number}: Снято {amount} рублей. Новый баланс: {self.balance} рублей."
        else:
            return "Недостаточно средств на счете или сумма для снятия недопустима."

    @staticmethod
    def is_valid_account_number(account_number):
        return len(account_number) == 10 
    
    @classmethod
    def calculate_interest(cls, balance):
        return cls.interest_rate * balance


account1 = BankAccount("1234567890", "Иванов Иван Иванович", 1000)
account2 = BankAccount("9876543210", "Петров Петр Петрович", 500)

print(account1.deposit(500))
print(account1.withdraw(300))
print(account2.deposit(300))
print(account2.withdraw(700))

print(f"Проценты по счету 1: {BankAccount.calculate_interest(account1.balance)} рублей")
print(f"Проценты по счету 2: {account2.calculate_interest(account2.balance)} рублей")

print(f"Счет 1 - допустимый номер счета? {BankAccount.is_valid_account_number(account1.account_number)}")
print(f"Счет 2 - допустимый номер счета? {BankAccount.is_valid_account_number(account2.account_number)}")

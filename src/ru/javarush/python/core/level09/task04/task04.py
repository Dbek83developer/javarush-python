# Банкир.

# Создайте класс BankAccount с конструктором, который принимает параметры account_number и initial_balance.
# Добавьте метод deposit(amount), который пополняет счет, и метод withdraw(amount), который снимает средства со счета.
# Создайте объект этого класса и выполните несколько операций пополнения и снятия средств.

# Напишите тут ваш код
class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.initial_balance = initial_balance

    def deposit(self, amount):
        self.initial_balance += amount

    def withdraw(self, amount):
        if self.initial_balance >= amount:
            self.initial_balance -= amount


xisob = BankAccount(12313123123132, 2000)
xisob.deposit(1000)
xisob.deposit(350)
xisob.withdraw(800)
print(xisob.initial_balance)

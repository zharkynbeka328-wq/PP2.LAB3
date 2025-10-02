class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} добавлено. Баланс: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств!")
        else:
            self.balance -= amount
            print(f"{amount} снято. Баланс: {self.balance}")


acc = Account("Akmaral", 100)
acc.deposit(50)    # Баланс = 150
acc.withdraw(70)   # Баланс = 80
acc.withdraw(100)  # Недостаточно средств!

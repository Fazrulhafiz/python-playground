class Account:
    def __init__(self, name, balance):
        self.id = id(name)
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("\n", amount, " deposited.")

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print("\n", amount, " withdrew.")
        else:
            print("Account balance insufficient")

    def __str__(self):
        return f"{self.name}'s account. Balance: {self.balance}"

A1 = Account("Fazrul", 100)
A1.deposit(4000)
A1.withdraw(245)
record = (A1)
print(A1)
print(record)
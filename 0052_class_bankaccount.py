class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        '''TU JEST coś co sprawdza, cyz pieniądze są prawdziwe'''
        self.balance += amount
    def try_withdraw(self, amount):
        if (self.balance > amount):
            self.balnace -= amount
            return True
        return False

    def __str__(self):
        return (str(self.balance))

class MinimumBalanceAccount:
    def __init__(self, balance=0, minimumBalance = 1000):
        self.balance = balance
        self.minimumBlanace = minimumBalance

konto = BankAccount()
konto.deposit(500)
if konto.try_withdraw(500):
    print("tak, wypłacono kasę")
else:
    print("Za mało kasy!")
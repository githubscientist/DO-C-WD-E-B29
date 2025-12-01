class Account:
    def __init__(self, number, type, balance):
        self.number = number
        self.type = type
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print("Balance is very low")

    def deposit(self, amount):
        self.balance = self.balance + amount

    def getBalance(self):
        print('Balance amount in account:',
              self.number, 'is ', self.balance)

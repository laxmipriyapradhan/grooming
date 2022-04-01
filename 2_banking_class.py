# BankAccount Class
class BankAccount:
    # Class Variable
    interest_rate = 0.04
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transactions = []
        self.transactions.append(f'******** Inital Amount Deposit ************ {balance}')

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f'Amount deposited: {amount}')

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(f'Amount withdrawn: {amount}')
    def transfer(self, to_account, amount):
        if self.balance >= amount:
            to_account.deposit(amount)
            self.balance -= amount
            self.transactions.append(f'NEFT to BankAccount {to_account}')
    def statement(self):
        for item in self.transactions:
            print(item)
        print(f'************ Total Account Balance ********** {self.balance}')
    def roi(self):
        int_amount = self.__class__.interest_rate * self.balance
        self.balance = self.balance + int_amount
        self.transactions.append(f'Interest Amount Credited {int_amount}')

b1 = BankAccount("steve", 1000)
b2 = BankAccount("bill", 2000)

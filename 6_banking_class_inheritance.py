from datetime import datetime

# Custom Exceptions for Bank Transactions!!
class TransactionDeclined(Exception):
    pass


class InsufficientBalance(Exception):
    pass


class MaxWithdrawLimtExceeded(Exception):
    pass


class BankAccount:
    interest_rate = 4.0

    def __init__(self, fname, lname, amount):
        self.fname = fname
        self.lname = lname
        self.balance = float(amount)
        self._transactions = []
        self._transactions.append(f"{datetime.now()} ***Initial Deposit*** {self.amount}")

    def deposit(self, amount):
        self.balance += float(amount)
        self._transactions.append(f'{datetime.now()} Deposited Amount: {amount}')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self._transactions.append(f'{datetime.now()} Withdrawn Amount: {amount}')
        else:
            raise InsufficientBalance()

    def statement(self):
        for line in self._transactions:
            print(line)
        print(f"Total Account Balance: {self.balance}")

    def roi(self):
        self.balance = self.balance + self.balance * (self.interest_rate / 100)


class SavingsAccount(BankAccount):
    interest_rate = 4.0

    def withdraw(self, amount):
        if amount > 10000:
            raise MaxWithdrawLimtExceeded('Can not withdrawn more than 10000 per day')
        super().withdraw(amount)


class SalaryAccount(BankAccount):
    def __init__(self, fname, lname):
        self.isFirstTime = True
        self._draft_amount = 0.00
        super().__init__(fname, lname, 0.00)

    def deposit(self, amount):  # Add A/C opening Bonus of 1000rs
        if self.isFirstTime:
            self.balance += 1000
            self.isFirstTime = False
        super().deposit(amount)

    def overdraft(self, amount):
        if self._draft_amount <= 10000:
            self.balance += amount
            self._draft_amount += amount
            self._transactions.append(f'{datetime.now()} ***Overdraft Amount Credited*** {amount}')
        else:
            raise Exception


class SeniorCitizenAccount(BankAccount):
    interest_rate = 5.5

    def withdraw(self, amount):
        if amount > 20000:
            raise MaxWithdrawLimtExceeded('Can not withdraw more than 20000 per day')
        super().withdraw(amount)


class SukanyaSamrudhiAccount(BankAccount):
    interest_rate = 9.5

    def deposit(self, amount):
        if amount < 1000:
            raise ValueError('Min Amount Should be 1000rs')
        super().deposit(amount)

    # Completely overriding the parent class method "withdraw"
    def withdraw(self, amount):
        raise TransactionDeclined("Can not withdraw")


class PenaltyAccount:
    def withdraw(self, amount):
        self.balance -= 200  # Penalty for withdrawing from PensionAccount
        super().withdraw(amount)


class RetirementAccount(PenaltyAccount, BankAccount):
    pass
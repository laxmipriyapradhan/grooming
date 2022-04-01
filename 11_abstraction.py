from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    def deposit(self, amount):
        print(f'Depositing amount {amount}')

    def withdraw(self, amount):
        print(f'Withdrawing amount {amount}')

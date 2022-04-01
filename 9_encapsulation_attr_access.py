class A:
    def __init__(self):
        self._internal = 0  # An internal/private attribute
        self.public = 1   # A Public attribute

    def public_method(self):
        print('Public method')
        return self._internal

    def _private_method(self):
        print('Internal Method')

class Spam:
    def __init__(self, text):
        self.text = text

    def _clean_up(self, text):
        return text.strip()

    def split_text(self):
        temp = self._clean_up(self.text)
        return temp.split()

    def get_len(self):
        temp = self._clean_up(self.text)
        return len(temp)
# ====================================================================================
# Setters and Getters
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if not isinstance(value, int):
            raise TypeError()
        self._radius = value
    
    def circumference(self):
        return self._radius * 3.14 * 2
    
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # By setting self.first_name , the set operation uses the setter method to set the
    # first_name attribute as opposed to bypassing it by accessing self._first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('First Name must be String')
        if len(value) > 12:
            raise ValueError('First Name must be less than 13 characters')
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")


p1 = Person('Steve', 'Jobs', 30)

print(p1.first_name)
p1.first_name = 'Bill'
print(p1.first_name)
# del p1.first_name


class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    @property
    def pay(self):
        return self._pay

    @pay.setter
    def pay(self, value):
        if not isinstance(value, int):
            raise TypeError('Pay Must be an Integer')
        self._pay = value

    def pay_raise(self, percent):
        hike = self.pay * percent
        self.pay += hike

e = Employee('Steve', 'Jobs', 9000)

# ====================================================================================
class BankAccount:
    __interest = 4.0

    def deposit(self, amount):
        print('Depositing Amount:', amount)

    def withdraw(self, amount):
        print('Withdrawing Amount:', amount)

    def roi(self):
        print("ROI is:", self.__class__.__interest)


class SavingsAccount(BankAccount):
    __interest = 4.5        # Does Not Override __interest of Parent Class


s = SavingsAccount()
# __interest in SavingsAccount will not override __interest of BankAccount
s.roi()     # Prints 4.0.

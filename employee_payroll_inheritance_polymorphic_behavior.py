# Calculating Payroll of different Employees
class Employee:
    def __init__(self, _id, name):
        self._id = _id
        self.name = name


class WeeklyEmployee(Employee):
    def __init__(self, _id, name, weekly_salary, weeks_worked):
        self.weekly_salary = weekly_salary
        super().__init__(_id, name)

    def calculate_pay(self):
        return self.weekly_salary * self.weeks_worked


class HourlyEmployee(Employee):
    def __init__(self, _id, name, hours_worked, hourly_rate):
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        super().__init__(_id, name)

    def calculate_pay(self):
        return self.hours_worked * self.hourly_rate


class CommisionedEmployee(WeeklyEmployee):
    def __init__(self, _id, name, weekly_salary, weeks_worked, commision):
        self.commision = commision
        super().__init__(_id, name, weekly_salary)

    def calculate_pay(self):
        fixed_pay = super().calculate_pay()
        return fixed_pay + self.commision


# Function that calculates the pay of all Employees
def calculate_payroll(employess):
    print('Calculating Payroll')
    for employee in employess:
        print(f'Pay for {employee._id}, {employee.name} = {employee.calculate_pay()}')


e1 = HourlyEmployee('1', 'steve', 40, 20)
e2 = WeeklyEmployee('2', 'Bill', 1250)
e3 = CommisionedEmployee('3', 'John', 1250, 100)
calculate_payroll([e1, e2, e3])

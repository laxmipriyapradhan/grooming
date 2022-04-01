class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    @classmethod
    def from_string(cls, string):
        temp = string.split("-")
        return cls(temp[0], temp[1], temp[2])

    def email(self):
        return f'{self.fname}.{self.lname}@company.com'

class Company:
    def __init__(self):
        self._records = []

    @classmethod
    def from_csv(cls):
        import csv
        c = cls()       # Company()
        with open('employees.csv') as f:
            rows = csv.DictRecder(f)
            for row in rows:
                c._records.append(row)
        return c

c = Company.from_csv()
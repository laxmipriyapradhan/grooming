import csv

# Representing each row of employee data as instance of class
class Employee:
    def __init__(self, name, gender, team, pay):
        self.name = name
        self.gender = gender
        self.team = team
        self.pay = pay

def read_csv():
    with open('employees.csv') as f:
        records = []
        rows = csv.Dictreader(f)
        for row in rows:
            records.append(row['name'], row['gender'], row['team'], row['pay'])
    return records

# Representing covid data as instance of class
class Covid:
    def __init__(self, country, date, cases):
        self.country = country
        self.date = date
        self.cases = int(cases)

# Company Class.
class Company:
    def __init__(self):
        self._team = []

    def add_emp(self, name, gender, team, pay):
        self._team.append((name, gender, team, pay))

    # Total Cost
    def total_cost(self):
        total = 0.00
        for emp in self._team:
            total += float(emp[3])
        return total

    # Total Number of male and female employees
    def emp_count_by_gender(self):
        from collections import defaultdict
        _count = defaultdict(int)
        for emp in self._team:
            _count[emp[1]] += 1
        return _count

    # Count of Employees in each department
    def emp_count_by_department(self):
        from collections import defaultdict
        _count = defaultdict(int)
        for emp in self._team:
            _count[emp[2]] += 1
        return _count

# Analysis of employees.csv file
with open('employees.csv') as f:
    c = Company()
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        c.add_emp(row[0], row[1], row[2], row[3])

print(c.total_cost())
print(c.emp_count_by_gender())
print(c.emp_count_by_department())

class Covid:
    def __init__(self):
        self.records = []

    def add_case(self, country, _date, cases):
        self.records.append({"country": country, "_date": _date, "cases": int(cases)})

    def total_cases(self):
        return sum([record['cases'] for record in self.records])

    def cases_by_country(self):
        from collections import defaultdict
        d = defaultdict(int)
        for record in self.records:
            d[record['country']] += record['cases']
        return d

    def countries(self):
        return {record['country'] for record in self.records}

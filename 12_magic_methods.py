import csv
# ========================================================================================
# Container Protocol
# ========================================================================================
"""
1. __contains__(self, obj)
2. __len__(self)
3. __getitem__(self, index)
4. __setitem__(self, index, value)
5. __delitem__(self, name)
"""
names = ['apple', 'google', 'yahoo']

names.__contains__("apple")     # Same as "apple" in names

names.__len__()     # Sames as len(names)

names.__getitem__(0)    # Same as names[0]

names.__setitem__(1, 'facebook')    # Same as names[1] = "facebook"

# Making Only Positive List Object
class PositiveList(list):
    # Overriding __setitem__ method of object list
    def __setitem__(self, index, value):
        if value < 0:
            raise ValueError("Only Positive Values are allowed in the list")
        return super().__setitem__(index, value)
    
    # Overriding the append method of built-in list class
    def append(self, value):
        if value < 0:
            raise ValueError("Only Positive Values are allowed in the list")
        return super().append(value)

# Making a positive dictionary
class PositiveDict(dict):
    def __setitem__(self, name, value):
        if value < 0:
            raise ValueError("Cannot set value less than Zero")
        super().__setitem__(name, value)

# Making an immutable dictionary
class ImmutableDict(dict):
    def __setitem__(self, name, value):
        raise KeyError(f"Cannot set value to Key {name}")
    
    def __delitem__(self, name):
        raise AttributeError(f"Cannot delete key {name}")

# Making PositiveCounter class by inheriting from builtin Counter class    
from collections import Counter
class PositiveCounter(Counter):
    def __setitem__(self, name, value):
        if value <= 0:
            raise AttributeError("No No No")
        super().__setitem__(name, value)

names = ['apple', 'google', 'apple', 'apple', 'google', 'yahoo']
c = PositiveCounter(names)
# This is not allowed
c['apple'] = -1

# Making ReadOnlyCounter
class ReadOnlyCounter:
    def __init__(self, obj):
        self._obj = obj

    def __setitem__(self, name, value):
        raise AttributeError("No... You cannot set item")
    
    def __getitem__(self, name):
        return self._obj[name]

names = ['apple', 'google', 'apple', 'apple', 'google', 'yahoo']
c = PositiveCounter(names)
# Wrap PositiveCounter object inside ReadOnlyCounter class
r = ReadOnlyCounter(c)
r['apple'] = 10 # Raises an exception

# ========================================================================================
# Attribute Protocol
# ========================================================================================
"""
1. __getattribute__(self, name)
2. __getattr__(self, name)
3. __setattr__(self, name, value)
4. __delattr__(self, name)
"""

"""
1. Whenever an attribute is accessed, the __getattribute__() method is invoked.
2. If the attribute is located, its value is returned. Otherwise, the __getattr__() method is invoked. 
3. The default behavior of __getattr__() is to raise an AttributeError exception. (we can override this method)
4. The __setattr__() method is always invoked when setting an attribute. 
and the __delattr__() method is always invoked when deleting an attribute.
"""

names.__getattribute__("append")        # Same as names.append

# Making an Immutable Class
class Point:
    def __init__(self, x, y):
        super().__setattr__("x", x)
        super().__setattr__("y", y)

    def __setattr__(self, name, value):
        print('Calling __setattr__')
        raise AttributeError("Cannot set attribute value")

    def __delattr__(self, name):
        print("Calling __delattr__")
        raise AttributeError("Cannot delete an attribute")

# Alternate method of making class Readonly
class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
class ReadOnly:
    def __init__(self, obj_point):
        super().__setattr__("point", obj_point)
    
    def __setattr__(self, name, value):
        raise AttributeError()
        
    def __getattr__(self, name):
        return getattr(self.point, name)   

    def __delattr__(self, name):
        raise AttributeError("No.. You cannot delete")

# Restricting users from adding new attribute to the class
class Point:
    # you will not be able to add new attribute, but you can change the value of 'x' and 'y'
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        (self.x, self.y) = (x, y)

# Alternate Method
class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
    
    def __setattr__(self, name, value):
        if name not in {"x", "y"}:
            raise AttributeError(f"Cannot add new attribute {name}")
        super().__setattr__(name, value)

# User defined datatype
class Employee:
    def __init__(self, name, pay, languages):
        self.name = name
        self.pay = pay
        self.languages = languages

    # Overriding __setattr__ method present in object class
    def __setattr__(self, name, value):
        print("Calling __setattr__")
        if name not in {"name", "pay", "languages"}:
            raise AttributeError(f'Cannot set attribute {name}')
        if name == "pay" and value < 0:
            raise ValueError(f"Cannot set {name} to a negative value")
        if name == "name" and len(value) > 5:
            raise ValueError(f"{name} attribute cannot have more than 5 characters")
        super().__setattr__(name, value)

    # Overriding __delattr__ method of parent or object class
    def __delattr__(self, name):
        raise AttributeError(f'Cannot delete attribute {name}')

e1 = Employee("Steve", 1000, ['C', 'Python'])
e2 = Employee("Bill", 2000, ['C++', 'Python', 'Java'])

# Function Protocol
"""
1. __call__
"""
# Iterator Protocol
"""
1. __iter__
2. __next__
"""
# Comparison Protocol

# ========================================================================================
# Number Protocol
# ========================================================================================
x = 10

x.__add__(10)

x.__mul__(10)

x.__sub__(10)
# ========================================================================================

# Descriptor Protocol
"""
1. __get__
2. __set__
3. __del__
"""
# Context Manager Protocol
"""
1. __enter__
2. __exit__
"""

# User defined datatype
class Employee:
    def __init__(self, name, pay, languages):
        self.name = name
        self.pay = pay
        self.languages = languages

    # Overriding __setattr__ method present in object class
    def __setattr__(self, name, value):
        print("Calling __setattr__")
        if name not in {"name", "pay", "languages"}:
            raise AttributeError(f'Cannot set attribute {name}')
        if name == "pay" and value < 0:
            raise ValueError(f"Cannot set {name} to a negative value")
        if name == "name" and len(value) > 5:
            raise ValueError(f"{name} attribute cannot have more than 5 characters")
        super().__setattr__(name, value)

    # Overriding __delattr__ method of parent or object class
    def __delattr__(self, name):
        raise AttributeError(f'Cannot delete attribute {name}')

    def __gt__(self, other):
        print('calling __gt__')
        return self.pay > other.pay

    def __lt__(self, other):
        print('calling __lt__')
        return self.pay < other.pay

    def __add__(self, other):
        return self.pay + other.pay

    def __sub__(self, other):
        return self.pay - other.pay

    def __iter__(self):
        return iter(self.languages)

    # overriding __str__ method of object class
    # __str__ method is used to give nice string representation of an object.
    # __str__ method should return a string.
    def __str__(self):
        return f"Employee({self.name}, {self.pay}, {self.languages})"

    def __contains__(self, item):
        return item in self.languages

    def __len__(self):
        return len(self.languages)

    def __getitem__(self, item):
        return self.__dict__[item]      # self.__dict__['pay']

    def __getitem__(self, item):
        return self.languages[item]


e1 = Employee("Steve", 1000, ['C', 'Python'])
e2 = Employee("Bill", 2000, ['C++', 'Python', 'Java'])
# ========================================================================
# Restricting users from adding new attribute to the class
class Point:
    # you will not be able to add new attribute, but you can change the value of 'x' and 'y'
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        (self.x, self.y) = (x, y)
# ========================================================================
# Alternate Method
class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
    
    def __setattr__(self, name, value):
        if name not in {"x", "y"}:
            raise AttributeError(f"Cannot add new attribute {name}")
        super().__setattr__(name, value)
# ========================================================================
# Implementing magic methods on Company class
class Company:
    def __init__(self):
        self._team = []

    def __iter__(self):
        return iter(self._team)

    def __len__(self):
        return len(self._team)

    def __getitem__(self, index):
        return self._team[index]

    @classmethod
    def from_csv(cls):
        c = cls()
        with open('data/employees.csv') as f:
            rows = csv.reader(f)
            next(rows)
            for row in rows:
                c._team.append((row[0], row[1], row[2], row[3]))
        return c

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

# What is the difference between __str__ and __repr__in Python?
from datetime import date
today = date.today()
print(str(today))
'2020-10-31'
print(repr(today))
'datetime.date(2020, 10, 31)'

# __str__ is used for printing o/p which is understandable by users
# __repr__ is used for printing o/p which is understandable by developers

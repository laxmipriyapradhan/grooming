# =======================================================================================
# DESCRIPTORS..
# =======================================================================================
# A descriptor is any object that defines __get__(), __set__(), or __delete__().

class Number:
    def __get__(self, obj, cls):
        print(obj, cls)
        print("Getting")
        return 26

class Point:
    d = Number()      # "d" is a descriptor Instance
    def __init__(self, a, b):
        self.a = a
        self.b = b

p = Point(1, 2)     # "p" is an instance of Point class

print(p.a)      # Normal Attribute lookup (Instance attributes)
print(p.b)      # Normal Attribute lookup (Instance attributes)

print(p.d)      # Descriptor Lookup

# The dot operator finds a descriptor instance and calls the method __get__ which returns 26

# Note that the value 26 is not stored in either the class dictionary or the instance dictionary of Point class. 
# Instead, the value 26 is computed on demand.

class Upper:
    def __get__(self, obj, cls):
        print("-------- Getting ------")
        return obj.name.upper()

class Employee:
    u = Upper()     # Descriptor Instance
    def __init__(self, name):
        self.name = name        # Regular Instance attribute

e1 = Employee("Steve")
e2 = Employee('Bill')

# "self" is the instance of Upper class which is "u"
# "obj" is the instance of Employee class. In the above case it is either "e1" or "e2"
# cls is the class reference, in the above case "Employee"

# Descriptors are uesd for managing access to instance data.

# The descriptor is assigned to a public attribute in the class dictionary while the actual data is stored as a private attribute in the instance dictionary.

# The descriptor’s __get__() and __set__() methods are triggered when the public attribute is accessed.

class Logging:
    def __get__(self, obj, cls):
        print(f'Accessing private attribute')
        return obj._age
    
    def __set__(self, obj, value):
        print(f'Setting/Updating private attribute to {value}')
        obj._age = value

class Employee:
    age = Logging()
    def __init__(self, name, age):
        self.name = name    # Regular instance attribute
        self.age = age      # Calls __set__()
    
    def birthday(self):
        self.age += 1       # Calls both __get__() and __set__()

e1 = Employee("Steve", 26)
e2 = Employee("Bill", 30)

# One major issue with this example is that the private name "_age" is hardwired in the Logging class.
# All the instances of Logging class will have same name to the private attribute which is "_age"
# For e.g. if we want to add one more private attribute named "_pay", we cannot do it since "_age" is hard-coded in Logging class.

# When a class uses descriptors, it can inform each descriptor about which variable name was used to create descriptor instance.
# Descriptors only work when used as class variables. When put in instances, they have no effect.

# Optionally, descriptors can have a __set_name__() method. 
# This is only used in cases where a descriptor needs to know either the class where it was created or the name of class variable it was assigned to. 
# (This method, if present, is called even if the class is not a descriptor.)

# PRACTICAL EXAMPLE
from abc import ABC

# 1. Name Should be Min=4 and Max=14
# 2. age should be integer and Max=60
# 3. pay should be floating point number

# Make a descriptor class (Abstract Base class)
class Validate(ABC):
    def __set_name__(self, cls, name):
        self.private_name = "_"+name

    def __get__(self, obj, cls):
        return obj.__dict__[self.private_name]
    
    def __set__(self, obj, value):
        obj.__dict__[self.private_name] = value


class Name(Validate):
    def __init__(self, min_len=4, max_len=14):
        self.min_len = min_len
        self.max_len = max_len

    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError("Name Should be a String")
        if not len(value) >= self.min_len or not len(value) <= self.max_len:
            raise ValueError(f"Minumum Length of name should be {self.min_len} and Maximum length shoould be {self.max_len}")
        super().__set__(obj, value)

class Age(Validate):
    def __init__(self, min_age=22, max_age=60):
        self.min_age = min_age
        self.max_age = max_age
    
    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        if value < self.min_age or value > self.max_age:
            raise ValueError(f"Minimum age must be {self.min_age} and Maximum age must be {self.max_age}")
        super().__set__(obj, value)
    
class Pay(Validate):
    def __init__(self, min_pay= 1000):
        self.min_pay = min_pay
    
    def __set__(self, obj, value):
        if not isinstance(value, (float, int)):
            raise TypeError("Pay Must be either float or int")
        if value < self.min_pay:
            raise ValueError(f"Minimum pay must be {self.min_pay}")
        super().__set__(obj, value)

class Employee:
    name = Name()
    age = Age()
    pay = Pay()

    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay

e = Employee("Steve", 26, 1000)

# Attribute Look-up chain on an object

# First, you’ll get the result returned from the __get__ method of the data descriptor named after the attribute you’re looking for.

# If that fails, then you’ll get the value of your object’s __dict__ for the key named after the attribute you’re looking for.

# If that fails, then you’ll get the result returned from the __get__ method of the non-data descriptor named after the attribute you’re looking for.

# If that fails, then you’ll get the value of your object type’s __dict__ for the key named after the attribute you’re looking for.

# If that fails, then you’ll get the value of your object parent type’s __dict__ for the key named after the attribute you’re looking for.

# If that fails, then the previous step is repeated for all the parent’s types in the method resolution order of your object.

# If everything else has failed, then you’ll get an AttributeError exception.

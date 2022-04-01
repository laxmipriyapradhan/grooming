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

# Under the Covers, property descreptors works as below.
p = e.__class__.__dict__['pay']     # Dictionary Look up happens

hasattr(p, '__get__')   # Checks if the Property object has an attribute '__get__'

p.__get__(e)    # If hasattr returns True, then python will fire __get__ method on the Property Object

hasattr(p, '__set__')   # Checks if the Property object has an attribute '__set__'

p.__set__(e, 9500)     # If hasattr returns True, then python will fire __set__ method on the Property Object

# So Basically Descreptors are Objects that impletements __get__, __set__ and __del__ methods.
# The DOT operator is Mapped to __get__ and __set__ methods


class Integer:
    def __init__(self, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError
        instance.__dict__[self.name] = value


class Employee:
    pay = Integer('pay')

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay


class Point:
    a = Integer('a')
    b = Integer('b')

    def __init__(self, a, b):
        self.a = a
        self.b = b


# Imlementation of properties Using Descriptors
class Descriptor:
    def __init__(self, value):
        self.value = value

    def __set__(self, instance, newvalue):
        instance.__dict__[self.value] = newvalue


class TypeCheck(Descriptor):
    expected_type = None

    def __set__(self, instance, newvalue):
        if not isinstance(newvalue, self.expected_type):
            raise TypeError(f'Expected Type should be {self.expected_type}')
        super().__set__(instance, newvalue)


class Integer(TypeCheck):
    expected_type = int


class String(TypeCheck):
    expected_type = str


class Float(TypeCheck):
    expected_type = float


class Positive(Descriptor):
    def __set__(self, instance, newvalue):
        if newvalue < 0:
            raise ValueError('Cant be Negative')
        super().__set__(instance, newvalue)


class Sized(Descriptor):
    def __init__(self, value, *, maxlen, **kwargs):
        self.maxlen = maxlen
        super().__init__(value, **kwargs)

    def __set__(self, instance, value):
        if len(value) > self.maxlen:
            raise ValueError('Can not be more than 10 chars')
        super().__set__(instance, value)


class Regx(Descriptor):
    def __init__(self, value, *, pat):
        self.pat = pat
        super().__init__(value)

    def __set__(self, instance, value):
        import re
        matches = re.compile(self.pat)
        print(matches)
        super().__set__(instance, value)


class PositiveInteger(Integer, Positive):
    pass


class PositiveFloat(Float, Positive):
    pass


class SizedString(String, Sized):
    pass


class SizedRegxString(SizedString, Regx):
    pass


class Employee(object):
    firstname = SizedRegxString("firstname", maxlen=10, pat='[A-Z]+')
    lastname = SizedRegxString("lastname", maxlen=10, pat='[A-Z]+')
    age = PositiveInteger('age')

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


e1 = Employee('Steve', 'Jobs', 40)
e2 = Employee('Bill', 'Gates', 41)


class Descriptor:
    def __init__(self, name, exp_type):
        self.name = name
        self.exp_type = exp_type

    def __get__(self, instance, value):
        if not isinstance(value, self.exp_type):
            raise TypeError
        instance.__dict__[self.name] = value


def TypeCheck(**kwargs):
    def decorate(cls):
        for name, exp_type in kwargs.items():
            setattr(cls, name, Descriptor(name, exp_type))
        return cls
    return decorate


# Decorated Class
@TypeCheck(fname=str, lname=str, pay=int)
class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
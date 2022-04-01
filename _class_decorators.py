# Normal function decorator.
def log(func):
    def wrapper(*args, **kwargs):
        print('Calling decorator')
        return func(*args, **kwargs)
    return wrapper

# Class decorators should take class as an argument and modified that class and returns the modified class
def logging(cls):
    for key, value in cls.__dict__.items():
        if callable(value):
            setattr(cls, key, log(value))
    return cls

# All the methods inside the class will be applied with the logging decorator
@logging
class Arithmetic:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def mul(self):
        return self.a * self.b  
# ==================================================================================================================  

# Attaching a class attribute using class decorator
def prices(cls):
    print('attaching class attribute')
    # creates a class attribute by name "apple" on the class ShoppingCart
    cls.apple = {"iphone": 900, "ipad": 2800, "imac": 4500}
    return cls

@prices
class ShoppingCart:
    def demo(self):
        print(self.apple)

# ==================================================================================================================

# Attaching an instance method to the class using class decorator
def attach_init(cls):
    def wrapper(self, a, b):
        self.a = a
        self.b = b
    cls.__init__ = wrapper
    return cls

@attach_init
class Arithmetic:
    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def mul(self):
        return self.a * self.b        

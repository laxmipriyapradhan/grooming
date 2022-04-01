class Greeting:
    def __init__(self, name="world"):
        self.name = name
    
    def __call__(self):
        return f"hello {self.name}"
    
class Greeting:
    def __call__(self, name):
        print(f'Hello {name}')

class Spam:
    def __init__(self, a):
        self.a = a

    def __call__(self):
        print('Executing __call__ ',self.a)

class Squares:
    def __call__(self, numbers):
        squares = []
        for number in numbers:
            squares.append(number ** 2)
        return squares

class Evens:
    def __call__(self, number):
        if number % 2 == 0:
            return True
        else:
            return False

# Class Decorators
class Log:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("You called {self.func.__name__}")
        return self.func(*args, **kwargs)

class Time:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        import time
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        print(f'Execution Time: {end-start}')
        return result

class Record:
    def __init__(self, func):
        self.func = func
        self._count = 0

    def __call__(self, *args, **kwargs):
        self._count += 1
        return self.func(*args, **kwargs)

# Using callable classes in sorted() function
# Sorting the list based on the last character of the list item
class LastChar:
    def __call__(self, item):
        return item[-1]

items = ['bv', 'aw', 'dt', 'cu']
last = LastChar()
s = sorted(items, key=last)

# Sorting based on temperatures
class Temperature:
    def __call__(self, item):
        return item[-1]

temperatures = [('Bangalore', 25), ('Delhi', 35), ('Chennai', 37), ('Mumbai', 32)]
temperature = Temperature()
sorted(temperatures, key=temperature)


portfolio = [
                {'name': 'IBM', 'shares': 100, 'price': 91.1},
                {'name': 'AAPL', 'shares': 50, 'price': 543.22},
                {'name': 'FB', 'shares': 200, 'price': 21.09},
                {'name': 'HPQ', 'shares': 35, 'price': 31.75},
                {'name': 'YHOO', 'shares': 45, 'price': 16.35},
                {'name': 'ACME', 'shares': 75, 'price': 115.65}
            ]

class By:
    def __init__(self, key):
        self.key = key

    def __call__(self, item):
        if self.key == "name":
            return item['name']
        elif self.key == "shares":
            return item['shares']
        else:
            return item['price']

# Sorting Based on name
sorted(portfolio, key=By("name"))

# Sorting Based on Shares
sorted(portfolio, key=By("shares"))

# Sorting Based on Price
sorted(portfolio, key=By("price"))

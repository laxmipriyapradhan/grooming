import csv

# Handling Bad records in csv file.
total = 0.00
with open('portfolio.csv', 'r') as f:
    next(f)     # Skip the header
    rows = csv.reader(f)
    for lineno, row in enumerate(rows):
        try:
            total += float(row[2])
        except ValueError as err:
            print('Line:', lineno, ':', err)
            continue

print('Total value of stock is :', total)
#-----------------------------------------------------
# Handling key error.
names = ["apple", "google", "yahoo", "yahoo", "gmail", "apple", "apple", "apple"]
_counts = {}
for name in names:
    try:
        _counts[name] = _counts[name] + 1
    except KeyError:
        _counts[name] = 1
#-----------------------------------------------------
# Handling Divide by Zero exception.
def func(n1, n2):
    try:
        result = n1 / n2
    except ZeroDivisionError:
        print("Bad Record:",(n1, n2))
    else:
        print(result)
    finally:
        print('Executing Finally')

numbers = [(1, 0), (3, 4), (4, 5), (1, 0), (3, 4), (3, 0)]

for number in numbers:
    n1, n2 = number
    func(n1, n2)
#-----------------------------------------------------
# Handling Multiple Exceptions
def div(n1, n2):
    try:
        result = n1 / n2
    except ZeroDivisionError:
        print(f'Bad Record: ({n1},{n2})')
    except TypeError:
        print('Numbers must not be strings')
    else:
        return result

def div(n1, n2):
   try:
      result = n1 / n2
   except (ZeroDivisionError, TypeError):
      print(f'Bad Record: ({n1},{n2})')
   else:
      return result
#-----------------------------------------------------
from requests import request
import json

def validate_url(ifsc_code):
    url = f"https://ifsc.razorpay.com/{ifsc_code}"
    response = request("GET", url)
    json_response = json.loads(response.text)
    try:
        return json_response['BRANCH']
    except TypeError:
        return "Invalid IFSC Code"
 
with open('./bank_codes.csv') as f:
    rows = csv.DictReader(f)
    for row in rows:
        print(validate_code(row['codes']))
#-----------------------------------------------------    
# Raising exceptions
def factorial(n):
    if isinstance(n, str):
        raise TypeError('No String value accepted')
    if n < 0:
        raise ValueError('Value should be greater than or equal to Zero')
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# ---------------------------------------------------------
# finally block
def func():
    try:
        print('Executing Try Block')
    except:
        print("Executing Except Block")
    # else block gets executed only when there is no exception in try block.
    else:
        print('Executing Else Block')
    # finally gets executed no matter what happens in try, except and else blocks.
    finally:
        print('Executing Finally Block')

# ---------------------------------------------------------
# returning values from try, except and else block's
def func():
    try:
       return 1
    except:
        return 2
    else:
        return 3
    finally:
        print('Finaly')

def func():
    try:
       return 1
    except:
        return 2
    else:
        return 3
    finally:
        return 4

# ---------------------------------------------------------------------------------
# Defining Custom Exceptions
class InsufficientFunds(Exception):
    pass

class AuthError(Exception):
    pass

class NetworkError(Exception):
    pass

def withdraw(amount):
    if amount > 5000:
        raise InsufficientFunds

def login(username, password):
    if username == 'admin' and password == 'admin123':
        print('Login Success')
    else:
        raise AuthError
# ---------------------------------------------------------------------------------
# Chained exceptions (Errors in different function)
# ---------------------------------------------------------------------------------
# Any exceptions related to the functions which is passed to "delay" would be reported 
# as "CallbackError"
class CallbackError(Exception):
    pass

def add(a, b):
    return a + b  # Raises TypeError if one of the value is of type string

def div(a, b):
    return a/b      # Raises ZeroDivisionError if the value of b is Zero

def spam(name):
    return name[10]     # Raises IndexError if the length of the iterable is less than 11

def delay(func, seconds, *args, **kwargs):
    from time import sleep
    sleep(seconds)
    try:
        return func(*args, **kwargs)
    # Catches any Exception while executing the function "func"
    except Exception as e:
        # raises CallbackError if there is any Exception from "func"
        raise CallbackError from e

# ---------------------------------------------------------------------------------        
# excluding except and else block (not mandatory)
def func(n1, n2):
    try:
        n1 / n2
    finally:
        return 1
# ---------------------------------------------------------------------------------

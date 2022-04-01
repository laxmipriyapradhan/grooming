"""
1. A sequence is an object which can be indexed.
2. All Sequences are Iterables. But all iterables are not sequences.
"""

point = (4, 5)  # Unpacking Tuple
x, y = point
print(x)
print(y)

data = ['IBM', 50, 91.1, (2019, 7, 17)]
name, shares, price, date = data    # Unpacking list of items
print(name)
print(shares)
print(price)
print(date)

y, m, d = date  # Unpacking Date

print(y)
print(m)
print(d)

s = 'Hello'
a, b, c, d, e = s   # Unpacking String
print(a)
print(b)
print(c)
print(d)
print(e)

# enumerate function
names = ['apple', 'google', 'gmail', 'yahoo', 'yahoo']

# Tuple unpacking
for item in enumerate(name):
    index, name = item
    print(index, name)

# Tuple unpacking (in for loop)
for index, name in enumerate(name):
    print(index, name)

# zip function
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

# Tuple unpacking
for item in zip(a, b):
    first_number, second_number = item
    print(first_number, second_number)

# Tuple unpacking (unpcking in for loop)
for first_number, second_number in zip(a, b):
    print(first_number, second_number)

# Unpacking a dictionary (method-1)
d = {'one': 1, 'two':2, 'three': 3}
for item in d.items():
    k, v = item
    print(k, v)

# Unpacking a dictionary (method-2)
for k, v in d.items():
    print(k, v)

# Normal unpacking
temperatures = {"Bangalore": (26, 32), "Chennai": (29, 35), "Delhi": (31, 36)}
for city, temperatures in temperatures.items():
    print(city, temperatures)

# Deep Unpacking
for city, (_min, _max) in temperatures.items():
    print(city, _min, _max)

# Unpacking Elements from iterables of Arbitary length
# * is used to grab excess arguments/items
# * is called unpacking operator
least, *rest, maximum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(least)    # Prints first item in the list
print(maximum)  # Prints last item in the list
print(rest)     # Prints all the item in between 1st and last item of the list
print(max(rest))
print(min(rest))

*trailing, current = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(trailing)
print(current)

a, b, *c = range(1, 10)

# Ignoring certain values while unpacking
# _ is called throwaway variable in python
data = ['IBM', 50, 91.1, (2019, 7, 17)]
name, *_, (year, *_) = data

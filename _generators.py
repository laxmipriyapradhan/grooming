from itertools import count
import time

'''
1. A Generator is a function that returns an iterator. It generates values using the 'yield' keyword.
2. They don't take memory of a list. They are LAZY Iterables. Generators are used for saving memory.
3. when called on next() function a raises StopIteration exception when there are no more values to generate.
4. 'yield' keyword suspends or pauses the execution of the function. But 'return' statement ends the function.
'''
# A function (Code which is after first return statement will be ignored by python)
def func():
    return 1
    return 2
    return 3

# Simple Generator
def func():
    print('Hello')
    yield "Hi"
    print('World')
    yield "Bye"

# Countdown Generator
def countdown(start):
    print('Starting countdown from ', start)
    while start > 0:
        yield start
        start -= 1
    print('Done!')

# Generates a range of floating point numbers
def frange(start, stop, step):
    while start <= stop:
        yield start
        start += step

# Generator produces even numbers
def evens(iterable):
    print('Genertor Wakes up!!')
    for item in iterable:
        if item % 2 == 0:
            yield item
            print("Runing After Yield")

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
e = evens(a)
c = count()     # Create a count object
i = evens(c)    # passing an infinite iterable to evens func

# Generator Expression
evens = (item for item in a if item % 2 == 0)

names = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex', 'ive']
# Generator function which yields the name starting from vowel
def vowels():
    for name in names:
        if name[0] in 'aeiou':
            yield name

# Generator Expression!
g_vowels = (name for name in names if name[0] in 'aeiou')

# Build a list of tuples with string and its length pair
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
g_pairs = ((name, len(name)) for name in names)

# Reverse the item of a list if the item is of odd length string
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
g_reverse_odd_length = (name[::-1] for name in names if len(name) % 2 != 0)

# Generator Expression!
loglines = (line for line in open('sample.log'))
events = (line for line in loglines if 'TRACE' in line)

# Analysing COVID data
# Without using Generators!
def read_csv(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append({'country': row[1], 'date': row[3], 'cases': row[5]})
    return records

import csv
# Using Generators
def g_read_csv(filename):
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            yield {'country': row[2], 'date': row[3], 'cases': int(row[5])}

# Total Cases
def total_cases():
    total = 0.00
    for row in g_read_csv('covid_data.csv'):
        total += row['cases']
    return total

# Cases By Country
def cases_by_country():
    from collections import defaultdict
    d = defaultdict(int)
    for row in g_read_csv('covid_data.csv'):
        d[row['country']] += row['cases']
    return d

# Cases by date and Country
def cases_by_date_country(country, _date):
    for row in g_read_csv('covid_data.csv'):
        if row['country'] == country and row['date'] == _date:
            return row

# Countries which has less than 10K cases
def cases_less_10K():
    total_cases = cases_by_country()
    return {country: cases for country, cases in total_cases.items() if int(cases) < 10000}

# List of all the countries affected by COVID. (Set Comprehension)
countries = { row['country']  for row in g_read_csv("covid_data.csv")}

# Generator that produces one line when asked for it
def g_read_log():
    with open('errors.log') as f:
        for line in f:
            yield line

# Generator that searches for a partucular pattern
def _grep(pattern, line):
    if pattern in line:
        yield line

for line in g_read_log():
    for match in _grep('WARN', line):
        print(line)
        time.sleep(1)

# Monitering live log file using generators
def _tail():
    with open('/var/log/system.log') as log:
        log.seek(0, 2)   # Goes to End of File
        while True:
            line = log.readline()
            if not line.strip():
                time.sleep(0.1)
                continue
            yield line
# =========================================================================
# Sending Values to the Generator
def spam():
    while True:
        value = yield
        if value == 26:
            print('Got: ',value)
            break

# Generator that yields a line from a file
def loglines(filename):
    with open(filename) as f:
        for line in f:
            yield line

def loglines(filename):
    with open(filename) as f:
        for line in f:
            yield line

def get_event_lines(event_type):
    print('Running Gen')
    while True:
      line = yield
      if event_type in line:
         print(line)

g = get_event_lines('TRACE')
next(g)

for line in loglines('sample.log'):
    g.send(line)
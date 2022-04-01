import itertools

# COUNT
counter = itertools.count()

for _ in range(10):
    print(next(counter))    # Prints numbers from 0 through 9

my_counter = itertools.count(start=5, step=5)   # It can take negative value for step argument

for _ in range(10):
    print(next(my_counter))

names = ['apple', 'microsoft', 'google', 'yahoo']

name_id = zip(itertools.count(), names)

for item in name_id:
    print(item)

# ================================================================
# CYCLE
states = ['ON', 'OFF']

cc = itertools.cycle(states)

for _ in range(5):
    print(next(cc))

colours = ['Red', 'Green', 'Yellow']
lights = itertools.cycle(colours)
print(next(lights))
print(next(lights))
print(next(lights))
print(next(lights))
print(next(lights))
print(next(lights))
# ================================================================
# REPEAT
r_2 = itertools.repeat(2)

# Prints 2 infinitely
for item in r_2:
    print(item)

r_2 = itertools.repeat(2, times=5)

# Prints 2, 5 times
for item in r_2:
    print(item)

# Prints string 'hello' 10 times
r_hello = itertools.repeat('hello', times=10)
for item in r_hello:
    print(item)

# ================================================================
# COMBINATION
letters = ['a', 'b', 'c']
my_comb = itertools.combinations(letters, 2)

for item in my_comb:
    print(item)

vowel_comb = itertools.combinations("aeiou", 2)

for item in vowel_comb:
    print(item)

# ================================================================
# PERMUTATION
my_permutation = itertools.permutations(letters)
# The above code Prints
# ('a', 'b', 'c')
# ('a', 'c', 'b')
# ('b', 'a', 'c')
# ('b', 'c', 'a')
# ('c', 'a', 'b')
# ('c', 'b', 'a')

my_permutation = itertools.permutations(letters, 2)

# The above code prints
# ('a', 'b')
# ('a', 'c')
# ('b', 'a')
# ('b', 'c')
# ('c', 'a')
# ('c', 'b')

for item in my_permutation:
    print(item)

# ================================================================
# iSlice

names = ['apple', 'google', 'yahoo', 'flikpart', 'netflix', 'gmail']

my_slice = itertools.islice(names, 2, 5)

for item in my_slice:
    print(item)

for item in itertools.islice(names, 2, None):
    print(item)
# None is used to indicate everything beyond index 2 (item[2:])

for item in itertools.islice(names, None, 3):
    print(item)
# start upto index 3 but not including index 3 (item[:3])

# Reading first 5 lines of the file
with open('read.txt', 'r') as f:
    lines = itertools.islice(f, 5, None)
    for line in lines:
        print(line, end='')
# ================================================================

# ================================================================
# chain
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

# Merges all 3 list's and returns an iterator object
d = itertools.chain(a, b, c)


# GroupBy
# ================================================================
students = [
    {"name": "alex", "level": 10, "grade": "A"},
    {"name": "ive", "level": 8, "grade": "B"},
    {"name": "steve", "level": 8, "grade": "A"},
    {"name": "jobs", "level": 10, "grade": "B"},
    {"name": "martin", "level": 8, "grade": "A"},
    {"name": "laura", "level": 10, "grade": "A"},
    {"name": "turner", "level": 10, "grade": "A"},
    {"name": "doug", "level": 10, "grade": "C"},
    {"name": "joe", "level": 8, "grade": "C"},
    {"name": "eric", "level": 8, "grade": "A"},
    {"name": "tim", "level": 10, "grade": "C"},
    {"name": "cook", "level": 8, "grade": "C"},
    {"name": "gates", "level": 10, "grade": "A"},
    {"name": "jeff", "level": 10, "grade": "B"}
]

from itertools import groupby
# Grouping students by "grade"
students.sort(key=lambda item: item['grade'])
by_grade = groupby(students, key=lambda item: item['grade'])

for _grade, items in by_grade:
    print(_grade)
    print('-----------')
    for item in items:
        print(item)

# Grouping students by "level"
students.sort(key=lambda item: item['level'])
by_level = groupby(students, key=lambda item: item['level'])
for _level, items in by_level:
    print(_level)
    print('-----------')
    for item in items:
        print(item)

# zip_longest
# =======================================================================
a = [1, 2, 3]
b = [4, 5, 6, 7, 8]

z = itertools.zip_longest(a, b)

print(list(z))  # Prints [(1, 4), (2, 5), (3, 6), (None, 7), (None, 8)]

z = itertools.zip_longest(a, b, fillvalue="NA")
print(list(z))  # Prints [(1, 4), (2, 5), (3, 6), (NA, 7), (NA, 8)]

# takewhile
# =======================================================================
t = itertools.takewhile(lambda item: item in 'aeiou', 'ear')
print(list(t))  # ['e', 'a']

# Iterating through varying records
prices = [
    ['GOOG', 490.1, 485.25, 487.5],
    ['IBM', 91.5],
    ['HPE', 13.75, 12.1, 13.25, 14.2, 13.5],
    ['GE', 52.5, 51.2]
]

for name, *values in prices:
    print(name, values)

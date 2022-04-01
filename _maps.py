"""
1. map() function is a built-in function that allows you to process and transform all the items in an iterable without
using an explicit for loop, a technique commonly known as mapping.

2. map() maps a function with an iterable. The functions transforms the each item of the iterable/iterator and returns a new map object
which is an iterator.

3. General Syntax of map() function. map(function, iterable[, iterable1, iterable2,..., iterableN])

4. map() applies the function to each item in the iterable in the loop and returns a new iterator, which you can feed it to next() function.

5. The first argument to the map function is a callable. This includes built-in functions, classes, methods, lambda expressions/functions.

6. The advantage of map function is that, it returns an iterator object and not a list. So the memory consumption is less. Each item inside the map
object can be obtained on-demand.
"""

# Square Numbers in the list. Using map function
def squares(item):
    return item ** 2

nums = [1, 2, 3, 4, 5]

# Using "for" loop
squared_numbers = [ squares(number) for number in nums]

# Using "map" function
squared_numbers = map(squares, nums) # map returns a map object

# Using lambda function
squared_numbers = map(lambda item: item ** 2, nums)

# Iterator over the map object
for number in squared_numbers:
    print(number)

# Build a list of tuples with string and its length pair
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']

# Using "for" loop
pairs = [(name, len(name) for name in names)]

# Using "map" function
def len_item_pair(item):
    return (item, len(item))

pairs = map(len_item_pair, names)

print(list(pairs))

# Type Conversion
str_nums = ["1", "2", "3", "4", "5"]

# Using "for" loop
int_nums = [ int(item) for item in str_nums]

# Using "map" function
int_items = map(int, str_nums)
print(list(int_items))

# inbuilt abs func
numbers = [-1, -2, 4, 5, -6]

# Using "for" loop
abs_values = [abs(number) for number in numbers]

# Using "map" function
abs_values = map(abs, numbers)

# Different precesions of pi values using map func
from math import pi

# Using "for" loop
pi_values = [round(pi, i) for i in range(1, 5)]

# Using "map" function
pi_values = map(round, [pi, pi, pi, pi], range(1, 5))
print(list(pi_values))

# passing two arguments to an user defined function.
exp = map(lambda x, y: 2*x + 3*y, [1, 2, 3, 4], [5, 6, 7, 8])
print(list(exp))

"""
NOTE: If we pass two iterables with different length's, the iteration
stops at the shortest length
"""

# Convert to upper case
sentence = "This is bunch of words"
ucase = map(str.upper, sentence.split())

# Using strip function.
words = ['This ', ' is', ' Python', ' Programming  ', ' Language ']
stripped = map(str.strip, words)
print(list(stripped))

# Factorial of a numbers
from math import factorial
f = map(factorial, [1, 2, 3, 4])
print(list(f))

# Passing a class which is callable to map function
class Squares:
    def __call__(self, item):
        return item ** 2

s = Squares()
m = map(s, [1, 2, 3, 4, 5])
print(list(m))

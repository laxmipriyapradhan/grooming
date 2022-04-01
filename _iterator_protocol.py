# Iterable:

"""
1. Anything that can be iterated or looped over is called iterable in Python.
2. All iterables have a special method call __iter__
3. String's, List's, Tuple's, Set's, Dictionary's, file objects and generator's are iterables.
4. All iterables can be passed to the built-in iter() function to get an iterator from them.
5. An iterator is an object that implements __next__,
which is expected to return the next element of the iterable object that returned it,
and raise a StopIteration exception when no more elements are available.
Any iterator can be passed to next() function to get the next item.
6. Iterators does not have length. They do not know how long they are.
7. Iterators do not have length can not be indexed. You can only call next() method to get the next item.
8. Generators are iterators, enumerate objects are iterators, zip function is an iterator file objects are iterators,
9. * Generators.
   * Generator Expressions.
   * enumerate
   * map
   * filter
   * zip
   * reversed
   * csv.reader()  functions returns an iterator object
"""

# Iterators are Lazy Iterables. i.e. they dont determine what their next item is until you ask them for it

# Iterator Protocol
# Let's Consider a for Statement

# for item in obj:
    # Statements

# What happens under the Covers?
#     _iter = obj.__iter__()  # Get iterator object
#     while True:
#         try:
#             x = _iter.__next__()  # Get next item
#         except StopIteration:  # No more items
#             break
        # statements ...

# All the objects that work with the for-loop implement this low-level iteration protocol.
x = [1, 2, 3]
it = x.__iter__()
print(it.__next__())    # Manually Iterate over

class SpamIterator:
    def __init__(self):
        self.index = 0

    def __next__(self):
        if self.index > 5:
            raise StopIteration
        item = self.index
        self.index += 1
        return item

# Spam object is now an iterable
class Spam:
    # __iter__ method should return a object ref to the
    # class which implements __next__ method
    def __iter__(self):
        return SpamIterator()


# Below Spam object is both iterable and Iterator
class Spam:
    def __init__(self):
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 5:
            raise StopIteration
        item = self.index
        self.index += 1
        return item

# Generator Function. (All generators are iterators)
def g_spam():
  index = 0
    while index <= 5:
       yield index
       index += 1
g = g_spam()

# ====================================================================
# Custom Iterator Class
class _range:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start > self.end:
            raise StopIteration()
        value = self.start
        self.start += self.step
        return value

# Generator Function.
def g_range(start, end, step):
    while start < end:
        yield start
        start = start + step
# ====================================================================
class Countdown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        value = self.start
        self.start -= 1
        return value

# Generator (All Generators are iterators)
def g_countdown(start):
    while start >= 0:
        yield start
        start -= 1
# ==================================================================== 
class Squares:
    def __init__(self, limit):
        self.limit = limit
        self.number = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.number > self.limit:
            raise StopIteration
        value = self.number ** 2
        self.number += 1
        return value

def g_squares(limit):
    number = 1
    while number <= limit:
        yield number ** 2
        number += 1
# ==================================================================== 

# Reverse Iterator
class ReverseItreator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = len(numbers) - 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        print('__next__ calling')
        if self.index < 0:
            raise StopIteration
        value = self.numbers[self.index]
        self.index -= 1
        return value

r = ReverseItreator([1, 2, 3, 4, 5])

# Prints each item of the list in reversed order
for item in r:
  print(item)

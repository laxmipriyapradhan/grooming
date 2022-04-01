def evens(item):
    if item % 2 == 0:
        return item

f = filter(evens, range(1, 10))
print(list(f))  # [2, 4, 6, 8]

# Build a list with only even with even length string using filter func
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']

# Returns the string if the string has even number of characters.
def even_len(item):
    if item % 2 == 0:
        return item

f = filter(even_len, names)
print(list(f))  # ['google', 'facebook', 'yelp', 'flipkart']


names = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex', 'ive']
# Returns the string if the string is starting from vowel character
def get_vowels(name):
    if name[0] in 'aeiou':
        return name

vowels = filter(get_vowels, names)
print(list(vowels))

# Get only those lines which has TRACE.
def logmessages(line):
    if 'TRACE' in line:
        return line

f = open('sample.log')
trace_lines = filter(logmessages, f)
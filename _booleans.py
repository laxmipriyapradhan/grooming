# Python evaluates below conditions to False

"""
1. Any Empty String in Python always evaluates to Boolean False.
A non-empty string or a string with atleast one character evaluates to boolean True

2. Any Empty list in python always evaluates to Boolean False.
A Non-Empty list or a list with atleast one item evaluates to Boolean True

3. An Integer Zero in python evaluates to Boolean False
and any number other than zero, it evaluates to Bool True.

4. An Empty Dictionary evaluates to Bool False
and a Dictionary with atleat one key:value pair evaluates to Bool True.

5. An Empty Tuple evaluates to Bool False
and a Tuple with atleast one element evaluates to Bool True.

6. An Empty set() evaluates to Bool False
and a set() with atleast one element evaluates to Bool True

7. None evalutes to Bool False.

8. Bool True evaluates to True and False evaluates to False
"""
# Lists
words = ['apple', 'google', 'yahoo', 'gmail']

# Iterate over the list only if the list has atleast 1 item.
if len(words) > 0:
    for word in words:
        print(word)
else:
    print('List is Empty')


if words:
    for word in words:
        print(word)
else:
    print('List is Empty')

# Strings
line = "           "
if len(line.strip()) > 0:
    print(line[0])
else:
    print('Got Empty String')

if line.strip():
    print(line[0])
else:
    print('Got Empty String')

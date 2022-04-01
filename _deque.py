from collections import deque

""" list-like container with fast appends and pops on either end """

# Make a new deque object with a string
d = deque("hello")  # deque(['h', 'e', 'l', 'l', 'o'])

# add a new entry to the right side
d.append('w')   # deque(['h', 'e', 'l', 'l', 'o', 'w'])

# add a new entry to the left side
d.appendleft('P')   # deque(['P', 'h', 'e', 'l', 'l', 'o', 'w'])

# return and remove the rightmost item
d.pop()     # deque(['P', 'h', 'e', 'l', 'l', 'o'])

# return and remove the leftmost item
d.popleft()     # deque(['h', 'e', 'l', 'l', 'o'])

sentence = "python is a programming language"
words = sentence.split()
d = deque(words)
d.rotate(2)
rotated_sentence = ' '.join(d)

# Rotating words of a string
def _rotate(sentence, n):
    words = sentence.split()
    for _ in range(n):
        last_item = words.pop()
        words.insert(0, last_item)
    return ' '.join(words)

# Rotating characters of a string
def _rotate_c(string, n):
    chrs = list(string)
    for _ in range(n):
        last_chr = chrs.pop()
        chrs.insert(0, last_chr)
    return ''.join(chrs)

def last_n_lines(n):
    with open('words.txt') as f:
        d = deque(f, maxlen=n)
    return list(d)

import re
# ============ Characters ===================
# . - Matches any character except new line
# \. - Mathes a dot.
# \\ - Matches backslash
# \* - Matches astrick

# ============ Character set ===================
# [abcd] - any character which matches either 'a' or 'b' or 'c' or 'd'
# [^abcd] - any character but not 'a' or 'b' or 'c' or 'd'
# [a-z] - any character between 'a' through 'z'

# =========== Special Sequences ================
# \w - Word character. Same as [a-zA-Z0-9_]. Matches alphanumeric and underscore.
# \W - Non-Word Character. Same as [^a-zA-Z0-9_]. Matches anything but word characters.
# \d - Matches a digit. Same as [0-9]
# \D - Matches a Non-Digit. Same as [^0-9]
# \s - Matches only whitespace.
# \S - Matches only Non-Whitespace.

# ========== Anchors ======================
# ^ - Start of String
# $ - End of String
# \b - Word boudary
# \B - Not a word Boundry
# [] - Matches characters in square brackets
# [^ ] - Matches characters Not in square brackets

# Meta Characters that needs to be Escaped (But need not be escaped when inside square brackets)
# . ^ $ * + ? { } [ ] \ | ( )

# Quantifiers
# * - Match expression 0 or more times
# + - Match expression 1 or more times
# ? - Match expression 0 or 1 times
# {3} - Matches expression exactly 3 times
# {3,4} - Matches expression 3 to 4 times
# {3, } - Match expression 3 or more times
# {, 3} - Match expression 0 to 3 times

# =========== Grouping ====================
# ("A"| "B" | "C") - Either "A" or "B" or "C"

# re.findall()   # returns a list of all the matches
# re.sub()  # replaces one pattern with other
# re.finditer()  # returns an iterator object
# re.search()  # stops at the first match

def search_pattern(_search_pattern, _search_string):
    _matches = re.findall(_search_pattern, _search_string)
    return _matches


greeting = "Hello world welcome to regular expressions in python"
matches = re.findall("python", greeting)

re.findall(r'hello', "hello world")

re.findall('hello', 'hello world, hello world hello')

re.findall('hello', "Hello world", re.IGNORECASE)

re.findall(r'.', "hello world")

re.findall(r'h.', "hello")

re.findall(r'h.', "hello world hi how how are you")

re.findall(r'a.b', "acb")

re.findall(r'a.b', "a b")

re.findall(r'a.b', "ab")

re.findall(r'a.b', "a*b a?b")

re.findall(r'a.b', "abcde")

re.findall(r"^hello", "hello world")

re.findall(r"^hello", "world hello")

re.findall(r"hello$", "world hello")

re.findall(r"hello$", "hello world")

re.findall(r'hello$', 'hello world welcome to python')

re.findall(r'^hello', 'hello world welcome to python')

re.findall(r'a.a', "ana")

re.findall(r'a..a', "anna")

re.findall(r'a..a', "an*a")

re.findall(r'a.*a', "annnnnna")

re.findall(r'a.*a', 'aa')

re.findall(r"^a.*a$", "anna")

re.findall(r"^a.*a$", "hello anna")

re.findall(r"an*a", "hello ana")

re.findall(r"an*a", "hello aa")

re.findall(r"an*a", "hello annna")

re.findall(r"an*a", "amma")

re.findall(r'a.*a', 'abcad')

re.findall(r'a.*a$', 'abcad')

re.findall(r'a.*a$', 'abcada')

re.findall(r'a.+a', 'ana')

re.findall(r'an+a', 'annnnnnnnnnna')

re.findall(r'a.+a', 'aa')

re.findall(r'an?a', "ana")

re.findall(r'an?a', "anna")

re.findall(r'colou?r', "colour")

re.findall(r'colou?r', "what color do you like")

re.findall(r'https?://', 'https://www.google.com')

re.findall(r'https?://', 'http://www.google.com')

re.findall(r"[aeiou]", "hello")

re.findall(r'[aeiou]', 'hello how are you doing anna')

re.findall(r'aeiou', 'hello how are you doing anna')

re.findall(r'aeiou', 'hello how are you doing anna, aeiou')

re.findall(r'[0-9]', 'The cost of the book is Rs.100')

re.findall(r'[0-9]+', 'The cost of the book is Rs.100')

re.findall(r"\d", 'The cost of the book is Rs.100')

re.findall(r"\d+", 'The cost of the book is Rs.100')

re.findall(r'[abcd]', 'hello world')

re.findall(r'[abcd]', 'abcdefghijk')

re.findall(r'[abcd]+', 'abcdefghijkab')

re.findall(r'[^0-9]', 'Rs.100')

re.findall(r'[^abcd]', 'axbyczdp')

re.findall(r'\D', 'Rs.100')

re.findall(r"[a-z]", 'hello HOW ARE YOU')

re.findall(r"[A-Z]", 'hello HOW ARE YOU')

re.findall(r"[a-zA-Z]", 'hello HOW ARE YOU')

re.findall(r"\w", "hello")

re.findall(r"\w+", "hello")

re.findall(r"\W", "hello world welcome to Python")

re.findall(r'\w+', 'hello there')

re.findall(r'\w+', 'hello_there')

re.findall(r"\w+", "my email is sandeep_gs@spam.com")

re.findall(r'\s', 'hello there    Hello')

re.findall(r'\S', 'hello there    Hello')

re.findall(r'\d\d\d\d\d\d', '560001')

re.findall(r"\d\d\d\d\d\d", 'Pincode of Bangalore is 560001 and telephone code is 080')

re.findall(r"\b\d{6}\b", 'Pincode of Bangalore is 560001 and telephone code is 080')

re.findall(r'\w{3,5}', 'hi')

re.findall(r'\w{3,5}', 'hello')

re.findall(r'\w{3,5}', 'helloworld')

re.findall(r'\w{3,5}', 'helloworld')

re.findall(r'\w{3,5}', 'hii hello _world')

re.findall(r'\w{3,}', 'hello')

re.findall(r'\w{3,}', 'hi')

re.findall(r'\w{1,}', 'hi')

re.findall(r'\w{0,}', '')

re.findall(r'^\w{0,1}$', 'hi')

re.findall(r'^\w{0,1}$', 'h')

# Regular expression which matches words that starts with "h"
matches = re.findall(r"\bh\w+", 'hello world hi hello universe how are you happy birthday')

# Regular expression which matches words that ends with "y"
matches = re.findall(r"\w+y\b", 'hello world hi hello universe how are you happy birthday feeling very sleepy flying')

# Sum all the numbers in the below string.
s = "Sony12India567Pvt2ltd" # 1 + 2 + 5 + 6 + 7 + 2
total = 0
numbers = re.findall(r'\d', s)
for number in numbers:
    total += int(number)

# Adding 12 + 567 + 2
s = "Sony12India567Pvt2ltd" # 1 + 2 + 5 + 6 + 7 + 2
total = 0
numbers = re.findall(r'\d+', s)
for number in numbers:
    total += int(number)
 
# Write a program to count the number of white spaces in a given string
sentence = "Hello world welcome to Python Hi  How are you. Hi how are you"
spaces = re.findall(r'\s', sentence)
print(len(spaces))

# Count the number of whitespaces in a file
white_spaces = 0
with open('sample.txt') as f:
    for line in f:
        match = re.findall(r'\s', line)
        if match:
            white_spaces += len(match)
print(white_spaces)

# Write a program count the occurrence of a particular word in the file
def count_words(word):
    _count = 0
    with open('sample.txt') as f:
        for line in f:
            _count +=  len(re.findall(word, line))
    return _count

# Write a program to count the number of occurrences of non-special characters in a given string.
sentence = 'hello@world! welcome!!! Python$ hi how are you & where are you?'
chrs = re.findall(r'\w', sentence)
d = {chr: chrs.count(chr) for chr in chrs}

# Filter only those characters except digits
word = '@hello12world34welcome!123'
matches = re.findall(r'\D', word)
print(''.join(matches))

# Count the characters in each word. Ignore special characters
sentence = "Hi there! How are you:) How are you doing today!"
words = re.findall(r'\w+', sentence)
word_len = { word: len(word) for word in words}

# Total Number of Upper case and Lower case letters
sentence = "Hello World Welcome To Python"
upper_case = re.findall(r'[A-Z]', sentence)
lower_case = re.findall(r'[a-z]', sentence)

print(f'Total No of upper case letters {len(upper_case)}')
print(f'Total No of lower case letters {len(lower_case)}')

# ===================================================
# Regular Expression - File names and extensions
# ===================================================
download_messages = """
Downloading file archive.zip to downloads folder...
Downloading file image.jpeg to downloads folder...
Downloading file index.xhtml to downloads folder... 
Downloading file python.py to downloads folder...
"""
re.findall(r'[a-z]+\.[a-z]+', download_messages)
# o/p ['.zip', '.jpeg', '.xhtml', '.py']

# Regular Expression- File Abbrevation
# ===================================================
match_abbreviation = r'[A-Z]'
file_formats = ['Graphics Interchange Format',
                'Advanced Audio Coding',
                'Cascading Style Sheets',
                'HyperText Markup Language',
                'Joint Photographic Experts Group',
                'Content Management System',
                'Tagged Image File Format',
                'Windows Media Audio',
                'Comma Seperated Values',
                'JavaScript Object Notation'
                ]

# ===================================================
# Regular Expression - Phone Number pattern
phone_numbers = ['123-345-0987', '456-9832-098', '800-987-4756', '080-1029384725', '123-345-12', '900-938-0987']
match_phone_numbers = r'\d{3}[-]\d{3}[-]\d{4}'
# ===================================================

# matching only 800 and 900 numbers
pat = r"^[89]00-\d{3}-\d{4}"
for number in phone_numbers:
    match = re.findall(pat, number)
    if match:
        print(match)
# ===================================================
# Regular Expression - YYYY-MM-DD date format
# ===================================================
_dates = ['2019-01-02', '2019-13-02', '2019-12-26', '26-08-2019', '20-19-20', '2019-12-31', '2019-12-32']
match_date_format = r'\d{4}-(?:0[1-9]|[12][0-9]|3[01])-(?:0[1-9]|[12][0-9]|3[01])'
# ===================================================
# Regular Expression - 24hr time format
_formats = ['00:00:00', '23:59:59', '24:00:00', '1:59:20', '12:9:10', '10:20:8']
for _format in _formats:
    match = search_pattern(r"(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d", _format)
    print(match)
# ===================================================
# Regular Expression - IP Addresses
# ===================================================
id_address_format = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
ips = ['10.1.2.3', '127.0.0.0', '199.99.9.9', '199.9.9999.9', '127-0-0-0']

# Regular Expression - Email format
# ===================================================
email_pattern = r'[\w-]+\.?[\w-]@[\w]+\.(com|edu|in|gov)'
emails = ['test.user@company.com',
          'test.user2@company.com',
          'test_user@company.com',
          'testing@company.com',
          'test-T.user@company.com',
          'testing@company',
          'testingcompany.com'
          ]
# ===================================================

# Regular Expression - URL Pattern
# ===================================================
url_pattern = r'https?://[\w.]+'
urls = ['http://www.youtube.com',
        'https://www.google.com',
        'http://www.amazon.in',
        'https://www.mail.yahoo.com',
        'ftp://test.com'
        'https://www.facebook.com/'
        ]
# ===================================================
# Regular Expression - PAN Number
sentence = "my pan number is ABCDE1234X and my friends pancard number is XYZTR3104J"
re.findall(r'\b[A-Z]{5}[0-9]{4}[A-Z]\b', sentence)
# ===================================================
# print only those words starting with vowel character
sentence = "hello hi american engieers and indian writers officers united states"
words = re.findall(r"\b[aeiou]\w+\b", sentence)
# =================================================== 
# Regular expression for matching only 3 letter words in the given string
sentence = "hello hi how are you what is your name he is older than me how old are you"
re.findall(r'\b\w{3}\b', sentence)
o/p ['how', 'are', 'you', 'how', 'old', 'are', 'you']
# ===================================================
# Replacing patterns
# Replace whitespaces with newline character in the below string
sentence = "Hello world welcome to python"
words = re.sub(r'\s', '\n', sentence)
print(words)

# Replace all vowels with "*"
sentence = "hello world welcome to python"
words = re.sub(r'[aeiou]', '*', sentence)
print(words)

# Replace all occurances of digits with "*"
sentence = 'hello123world welcome456to python012'
words = re.sub(r'\d', '*', sentence)

# Replace all occurances of special characters with "*"
sentence = 'hello#$%world welcome@!#$%to python*&^%'
words = re.sub(r'[^a-zA-Z\s]', "*", sentence)

# Replace all occurances of "Java" with "Python" in a file
with open('java.txt', 'r') as jf:
    with open('python.txt', 'a') as pf:
        for line in jf:
            new_line = re.sub('Java', 'Python', line)
            pf.write(new_line)

#=================================================================================
# re.finditer()
matches = re.finditer(r"hello", 'hello world welcome to python hello world')
for match in matches:
    print(match.group())

# Write a program to find the index of nth occurrence of a sub-string in a string
sentence = "hello world welcome to python hello hi how are you hello there"
matches = re.finditer(r'hello', sentence)
positions = [ (match.start(), match.end()) for match in matches]

# re.search()
match = re.search(r"hello", 'hello world hello world')
print(match.group())

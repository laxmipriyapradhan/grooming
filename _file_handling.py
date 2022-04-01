from collections import Counter
from collections import defaultdict
# File Objects

# r ---> Read Only, w ---> Write Only, a ---> Append, r+ ---> Read and Write

# Reading file without using Context manager
f = open('read.txt', 'r')
f_contents = f.read()
print(f_contents)
f.close()

# Reading file Using Context Manager (No need to close the file explicitly when file is opened using contex manager)
with open('read.txt') as f:
    f_contents = f.readlines()   # Returns a List
    for line in f_contents:
        print(line, end='')
    print('Number of lines in the file ', len(f_contents))  # Prints total number of lines in the file

with open('read.txt') as f:
    f_contents = f.read()    # Reads the entire contents of the file into a variable as string
    print(f_contents, end='')

with open('read.txt') as f:
    print(f.readline(), end='')  # Reads one line at a time
    print(f.readline(), end='')
    print(f.readline(), end='')

with open('read.txt') as f:
    line = f.readline()
    while line:
        print(line, end='')
        line = f.readline()

with open('read.txt') as f:
    for line in f:           # Loads only one line at a time and prints the line
        print(line, end='')

# Reading 10 characters at a time
size_to_read = 10
with open('read.txt') as f:
    f_contents = f.read(size_to_read)
    print(f_contents, end='')
    f_contents = f.read(size_to_read)
    print(f_contents, end='')


# Printing the line's with line numbers
with open('sample.txt') as f:
    for linenumber, line in enumerate(f, start=1):
        print(linenumber, line, end='')

# Reading the file in reversed order
with open('read.txt') as f:
    for line in reversed(list(f)):
        print(line, end='')

# Finding the length of each line in the text file
with open('read.txt') as f:
    for line in f:
        print(len(line))

# Exercises:
# 1. Extracting IP addresses from log file
with open('access-log.txt') as f:
    ip = []
    for line in f:
        line = line.strip()
        if line:
            parts = line.split()
            ip.append(parts[0])

# Getting unique ip's from the list
unique_ip = set(ip)

# Using set
with open('access-log.txt') as f:
    ip = set()
    for line in f:
        if line.strip():
            parts = line.split()
            ip.add(parts[0])

# Using List Comprehension
ip = [line.split()[0] for line in open('access-log.txt') if line.strip()]

# Using Set Comprehension
unique_ip = {line.split()[0] for line in open('access-log.txt', 'r') if line.strip()}

out_file = open('ip_list.txt', 'w')
for item in unique_ip:
    out_file.write(item)
out_file.close()

# Counting number of occurances of ip adresses in the log file.
# Normal Dict
d = {}
for item in ip:
    if item in d:
        d[item] += 1
    else:
        d[item] = 1

# Using defaultdict
d = defaultdict(int)

for item in ip:
    d[item] += 1

# Using Counter Object
d = Counter(ip)

# Sotring dictionary based on occurances of ip addresses.
sorted_ip = sorted(d.items(), key=lambda item: item[-1])

# Extracting Messages from sample.log
with open('sample.log') as log:
    for line in log:
        line = line.strip()
        if line:
            parts = line.split()
            print(parts[2])

# Getting Unique Messages (Set comprehension)
unique_messages = {line.split()[2] for line in open("sample.log") if line.strip()}

# Counting Number of INFO, WARN, TRACE Messages.
messages = defaultdict(int)
with open('sample.log') as log:
    for line in log:
        line = line.strip()
        if line:
            parts = line.split()
            messages[parts[2]] += 1

# Using Counter object
message_list = [line.strip().split()[2] for line in open('sample.log') if line.strip()]
c = Counter(message_list)
print(c)

# Reading Countries from football.txt
with open('football.txt') as log:
    countries = []
    headers = next(log)     # Skipping Header
    for line in log:
        if line.strip():
            parts = line.split("\t")
            countries.append(parts[1])

# Using List Comprehension
countries = [line.strip().split()[1] for line in open("football.txt") if line.strip()]
print(len(countries))

# Using set
with open('football.txt') as f:
    unique_countries = set()
    headers = next(log)  # Skipping Header
    for line in f:
        if line.strip("\t"):
            parts = line.split()
            unique_countries.add(parts[1])

# Getting Unique Countries using Set Comprehension
set_countries = {line.strip().split()[1] for line in open("football.txt") if line.strip()}

# Using defaultdict
word_count = defaultdict(int)
f = open('sample.txt')
for line in f:
    if line.strip():
        words = line.split()
        for word in words:
            word_count[word] += 1
print(word_count)

# Least and Most occurances of the word
least, *rest, maximum = sorted(d.items(), key=lambda name: name[-1])
print(least)    # Prints the word with least occurance
print(maximum)  # Prints the word with maximum occurance
print(rest)     # Prints all elements between 1st and last element

# Counting total number of words present in a file
words_count = 0
with open('sample.txt') as f:
    for line in f:
        if line.strip():
            words = line.split()
            print(words)
            words_count += len(words)

# Finding the line no of a perticular word in a file.
with open('sample.txt') as f:
    for lineno, line in enumerate(f, start=1):
        if line.strip():
            if "Ruby" in line:
                print(lineno, line)

# list of Dicts from data
def make_dict(line):
    data = line.strip().split('\t')
    return {"brand": data[0], "color": data[1], "size": data[2]}

s = [make_dict(line) for line in open('data.txt')]

# Writing to file
with open('write.txt', 'a') as f:
    f.write('Hello world')
    f.write('\n')

# # Preventing files from being overwritten
# with open('sample.txt', 'x') as f:
#     f.write('hello world')
#     f.write('hello world') # Throws an exception. Cannot overwrite a file

# Opening two files in parallel
# Comparing the two files line by line
with open('file1.txt') as f1, open('file2.txt') as f2:
    for f1_line, f2_line in zip(f1, f2):
        print(f1_line.strip(), f2_line.strip())

# Copying Contents of one file to another file
with open('sample.txt') as rf, open('sample2.txt', 'w') as wf:
    for line in rf:     # Iterate through each line in sample.txt
        wf.write(line)  # Write each line to sample2.txt

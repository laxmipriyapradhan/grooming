# Conditional statement
_month = 'January'

if _month == 'January':
    print('You are in Jan')
elif _month == 'March':
    print('You are in Mar')
elif _month == 'July':
    print('You are in Jul')
else:
    print('Unknown month')
    
# Good and Bad Emotions
good_emotions = ['good', 'great', 'happy', 'awesome']
bad_emotions = ['sad', 'angry', 'upset', 'tired']

user_feeling = input('How are you today?').lower()

if user_feeling in good_emotions:
    print(f'I am glad you are feeling {user_feeling} today')
elif user_feeling in bad_emotions:
    print(f'I am sorry you are feeling {user_feeling} today')
else:
    print('I dont know how you are feeling today')

# Inline If statement
ios_latest_version = '12.2.1'
ios_current_version = '12.1.1'

msg = 'Update Available' if ios_latest_version.split('.') > ios_current_version.split('.') else 'Software is upto date'
print(msg)

# Below code is same as the above inline if statement
if ios_latest_version.split('.') > ios_current_version.split('.'):
    print('Update Available')
else:
    print('Software is upto date')

# =================================================
# Looping
fruits = ['apple', 'orange', 'banana', 'strawberry']

# Traditional way of Looping..
for index in range(len(fruits)):
    print(fruits[index])

# Looping to get both the index and item
for index in range(len(fruits)):
    print(index, fruits[index])

# PYTHONIC approach
for fruit in fruits:
    print(fruit)

# To get both index and item (PYTHONIC approach)
for index, fruit in enumerate(fruits):
    print(index, fruit)
# ============================================
for num in range(5):
    print(num)

for x in range(5):
    print('Python is awesome')

for num in range(0, 10, 2):
    print(num)

# Prints numbers from 9 through 0
for num in reversed(range(10)):
    print(num)

months = ['january', 'march', 'may', 'july']
for month in months:
    print(len(month), month)

# Iterates through the list in reversed order
for month in reversed(months):
    print(month)

counter = 0
while counter < 5:
    print('Python is awesome')
    counter += 1

# ===================================================
# Break and Continue statements
my_num = 10
for num in range(100):
    if num == my_num:
        print(num)
        break
    else:
        print(num)

for num in range(51):
    if num % 2 == 0:
        continue
    else:
        print(num)

numbers = [1, 3, 5, 7, 9]
for num in range(10):
    if num in numbers:
        continue
    else:
        print(num)
# ======================================================

import random

print(random.random())  # Prints a random floating point number between 0 and 1. Both excluding. e.g. 0.1, 0.8

print(random.uniform(1, 10))    # Prints random floating point number between the specified range (1 and 10).

print(random.randint(1, 6))     # Prints random integer between 1 and 6. Both inclusive.

print(random.randrange(0, 100, 5))      # Prints random integer between 0 and 100 with step size of 5

names = ['apple', 'google', 'yahoo', 'facebook', 'microsoft', 'instagram', 'watsapp']

print(random.choice(names))     # Prints a random item in the list 'names'

# Creating a combination of first name and last names from the list
fname = ['steve', 'bill', 'mark', 'rob', 'mike', 'laura', 'adams']
lname = ['jobs', 'gates', 'waugh', 'charlie', 'stone', 'turner', 'randolph']

for _ in range(10):
    full_name = f'{random.choice(fname)} {random.choice(lname)}'
    print(full_name)

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(random.sample(values, 3))     # Prints random subset of the list

# Shuffles the list
random.shuffle(values)      # Only Mutable data can be passed to shfulle method
# Shufulle does not return new list, insted it mutates the existing list
print(values)

# Shuffles the list
random.shuffle(values)
print(values)

suits = ['hearts', 'clubs', 'diamonds', 'spades']
random.shuffle(suits)

# Generate 6 digit OTP
def generate_otp():
    otp = []
    for _ in range(6):
        otp.append(str(random.randint(0, 9)))
    return ''.join(otp)


def random_password(*, upper=1, lower=1, digits=1, special=1, length=8):
    UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LOWERCASE = UPPERCASE.lower()
    DIGITS = "0123456789"
    SPECIAL = "!@#$%^&*()"
    ALL = UPPERCASE + LOWERCASE + DIGITS + SPECIAL

    password = []

    for _ in range(upper):
        password.append(random.choice(UPPERCASE))
    for _ in range(lower):
        password.append(random.choice(LOWERCASE))
    for _ in range(digits):
        password.append(random.choice(DIGITS))
    for _ in range(special):
        password.append(random.choice(SPECIAL))
    for _ in range(length - upper - lower - digits - special):
        password.append(random.choice(ALL))

    return ''.join(password)


pwd = random_password(upper=1, lower=3, digits=1, special=1, length=8)


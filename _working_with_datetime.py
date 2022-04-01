import datetime

# Datetime object is Immutable
my_dt = datetime.datetime(2019, 5, 26, 8)

# Below code Throws exception "attribute 'year' of 'datetime.date' objects is not writable"
my_dt.year = 2022

# Traceback (most recent call last):
#   File "<pyshell#74>", line 1, in <module>
#     td.year = 2022
# AttributeError: attribute 'year' of 'datetime.date' objects is not writable

# Converting String to Python DateTime format
dt = '1/1/2014  12:38:00 PM'   # The Data Type of dt is String
m, d, y = dt.split('/')
y = y.split(' ')[0]
d = datetime.date(int(y), int(m), int(d))
print(d)    # The Data Type of d is Datetime
# =================================================

# To Get the Current date
td = datetime.date.today()
print("Today's date is ", td)
print("Today's Year is ", td.year)  # To Get the Current Year
print("Today's Day is ", td.day)  # To Get the Current Day
print("Today's Month is ", td.month)     # To Get the Current Month
print(td.weekday())     # Monday =0 and Sunday = 6
# =================================================

# TIME DELTAS's
# =================================================
# Time Delta's are the difference between two dates and Time
t_delta = datetime.timedelta(days=7)
print(td + t_delta)     # Prints 7 Day's from today
print(td - t_delta)     # Prints Date 7 Day's before from today's date

td_hour = datetime.datetime.today()
t_delta = datetime.timedelta(hours=2)
print(td_hour + t_delta)    # Adds two hours to the current hour

td_days_hour = datetime.timedelta(days=2, hours=4)
print(datetime.datetime.today() + td_days_hour)     # Prints two days and 4hrs from today
# =================================================
# TO know how many days are there for my Birthday
bday = datetime.date(2019, 7, 26)
till_bday = bday - td
print(till_bday)    # Prints the Number of days to go for the Birth day from today
print(type(till_bday))  # The data type is timedelta
print(till_bday.days)   # Prints Days The Data type is integer

# ===================================================
# datetime.time
ts = '9:14:00'   # Data Type is String
h, m, s = ts.split(':')
t = datetime.time(int(h), int(m), int(s))
print(t)      # Date Type is Time
print(t.hour)   # Prints Hour
print(t.minute)     # Prints Minute
print(t.second)     # Prints Seconds
# ====================================================
# datetime.datetime
# ====================================================
dt = datetime.datetime(2019, 7, 26, 11, 46, 36)
print(dt)   # Prints Date and Time
print(dt.date())    # Prints only Date Part
print(dt.time())    # Prints only Time
print(dt.time().minute)     # Prints Minutes
print(dt.time().second)     # Prints Seconds
print(dt.time().hour)       # Prints Hour
print(dt.date().month)      # Prints Month
print(dt.date().year)       # Prints Year
print(dt.date().day)        # Prints Day
print(datetime.datetime.today())    # Prints Current Date and Time
print(datetime.datetime.now())  # Prints Current Date and Time. But we can Pass Time Zone Info
print(datetime.datetime.utcnow())   # Prints Current UTC Date and Time
# ====================================================
td_str = 'July 26, 1983'
print(datetime.datetime.strptime(td_str, '%B %d, %Y').date())  # Prints 1983-07-26
td_str = '26 July, 1983'
print(datetime.datetime.strptime(td_str, '%d %B, %Y').date())  # Prints 1983-07-26
td_str = '1983, July 26'
print(datetime.datetime.strptime(td_str, '%Y, %B %d').date())  # Prints 1983-07-26

td_str = 'Jul 26, 1983'
print(datetime.datetime.strptime(td_str, '%b %d, %Y').date())  # Prints 1983-07-26
td_str = '26 Jul, 1983'
print(datetime.datetime.strptime(td_str, '%d %b, %Y').date())  # Prints 1983-07-26
td_str = '1983, Jul 26'
print(datetime.datetime.strptime(td_str, '%Y, %b %d').date())  # Prints 1983-07-26

print(datetime.date.strftime(td, '%B %d, %Y'))      # Prints January 08, 2019
print(datetime.date.strftime(td, '%d %B, %Y'))      # Prints 08 January, 2019
print(datetime.date.strftime(td, '%Y %B, %d'))      # Prints 2019 January, 08

print(datetime.date.strftime(td, '%b %d, %Y'))      # Prints Jan 08, 2019
print(datetime.date.strftime(td, '%d %b, %Y'))      # Prints 08 Jan, 2019
print(datetime.date.strftime(td, '%Y %b, %d'))      # Prints 2019 Jan, 08

print(datetime.date.strftime(td, '%A %B %d, %Y'))      # Tuesday June 18, 2019

from datetime import date, timedelta

class WeekDay:
    # Class Variables
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

class NextDate:
    def __init__(self, weekday):
        self.weekday = weekday

    def next_date(self):
        td = date.today()
        td_week_day = td.weekday()
        _next_day = self.weekday - td_week_day
        if _next_day <= 0:
            _next_day += 7
        return td + timedelta(_next_day)

# Python Libraries
# example
""" from datetime import date
d = date(2013, 8, 22)
print(d.year)
print(d.month)
print(d.day)
print(d.strftime("%Y %m %d")) """

# current time
""" from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time = ", current_time) """


# Task
""" import datetime

now = datetime.datetime.today()

print(now.year)
print(now.month)
print(now.day)
print(now.date())

myDate = now.date()

for i in range(14, 140, 14):
    print(myDate) """

# Exercise 2
# Ten dates from today, 2 weeks apart
from datetime import datetime, timedelta

# Today's date
dt = datetime.now()

# Prints 10 dates 14 days apart
for x in range(9):
    print(dt.strftime('%Y/ %m/ %d'))
    dt = dt + timedelta(days=7)

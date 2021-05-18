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
""" from datetime import datetime, timedelta

# Today's date
dt = datetime.now()

# Prints 10 dates 14 days apart
for x in range(9):
    print(dt.strftime('%Y/ %m/ %d'))
    dt = dt + timedelta(days=7) """

# Calculating Age
from datetime import datetime
year_born = int(input("Enter year born: "))
month_born = int(input("Enter your month born: "))
day_born = int(input("Enter your day born: "))

current_year = int(datetime.today().strftime("%Y"))
current_month = int(datetime.today().strftime("%m"))
current_day = int(datetime.today().strftime("%d"))

age = current_year - year_born - 1

if month_born < current_month:
    age += 1
elif current_month == month_born:
    if current_day >= day_born:
        age += 1

print(age)

# Python Libraries
# example
""" from datetime import date
d = date(2013, 8, 22)
print(d.year)
print(d.month)
print(d.day)
print(d.strftime("%Y %m %d")) """

# current time
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time = ", current_time)

from datetime import datetime, timedelta

#uses iso8601 format
d = datetime.now()
print(d)

#construct date and time to the seconds
d2 = datetime(2020,12,6,14,34,34)
print(d2)

#tuple for dates, create a date time by expanding a tuple
t = (2007, 8 ,6, 17, 20, 13)
d4 = datetime(*t)
print(d4)

w = d2.weekday()
print(w)

# %A weekday in long form (%a short form)
# %d day of month 
# %m month number
# %b, %B month name in short or long form
# %y, %Y 2 digit or 4 digit format of year
# %j day number of the year
# %H %h 24/12 hours
# %M minute
# %S seconds 
print(d2.strftime("%A %d %B %Y"))


d8 = datetime.now()
print(d8)
d9 = d8 - timedelta(hours=1)
print(d9)

print(d8 - d9)

print((d8 - d9)/ timedelta(minutes=1))

"""import math as m
x=m.ceil(45.6)
print(x)
x=m.ceil(-45.6)
print(x)

#floor
x=m.floor(45.6)
print(x)
x=m.floor(-45.6)
print(x)


#truncate()
x=m.trunc(45.6)
print(x)
x=m.trunc(-45.6)
print(x)

#round
x=round(45.6482,2)
print(x)

#datetime
from datetime import datetime as d
print("Current date and time : ",d.now())"""

#to show only current time/system time
from datetime import datetime as d
x=d.now()  #system dtae and time
#to extract only time hh:mm:ss
#inbuilt method strftime ("%H:%M:%S")
t=x.strftime ("%H:%M:%S")
print("Current time : ",t)

print("system date and time : ",x)
#to extract year of current date and time
y=x.year  #year inbuilt attribute
print("Year of system date : ",y)

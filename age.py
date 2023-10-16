from datetime import date as y1
yr=int(input("Enter Year :"))
mn=int(input("Enter Month :"))
day=int(input("Enter Date :"))
dob=y1.date(yr,mn,day)
print(type(dob))

#extract year from system date
y1=date.tody().year
#find the age
age=y1-yr
print("Age : ",age)

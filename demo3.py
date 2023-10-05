a=int(input("enter student roll no :"))
b=(input("enter student name :"))
c=int(input("enter student age :"))
sub1=float(input("enter marks of 1 subject :"))
sub2=float(input("enter marks of 2 subject :"))
sub3=float(input("enter marks of 3 subject :"))
sub4=float(input("enter marks of 4 subject :"))
sub5=float(input("enter marks of 5 subject :"))

total=sub1+sub2+sub3+sub4+sub5
print("Total Marks :",total)

per=total*100/500
print("Percentage :",per)

if (per>=85):
    grade="A+"
elif(per<85 and per>=70):
    grade="A"
elif(per<70 and per>=60):
    grade="B"
else:
    grade="C"
print("Grade:",grade)    
    
    
            

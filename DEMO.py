# wap to finf simple interest and amount  when given principl,rate of interest and time

p=float(input("Enter princle :"))
r=float(input("Enter rate of interest:"))
t=float(input("Enter time period:"))
SI=p*r*t/100
amt=p+SI
print("simpe interest :",SI,"\nAmount :",amt)

print("simple interest .{}\n Amount .{}".format(SI,amt))
#\n new line : inbuilt command of py

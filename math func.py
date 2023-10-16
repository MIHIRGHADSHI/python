
import math as m
#m is a alias name of math library
p=float(input(" enter principal amount :"))
r=float(input(" enter rate of interest :"))
t=int(input(" enter how many year :"))
x=(1+(r/100))
amt=p*m.pow(x,t)
ci=amt-p
print("Amount : ",amt)
print("Compount Interest : ",ci)
        

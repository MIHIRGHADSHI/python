def interest (x,y,z):
    s=x*y*z/100
    return s
p=float(input("Enter principle amount :"))
r=float(input("Enter rate of interest :"))
t=float(input("Enter how many year :"))
si=interest(p,r,t)
print("Simple interest :",si)
amt=p+si
print("Amount :",amt)

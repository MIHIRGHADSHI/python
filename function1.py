def interest (x,y,z):
    s=x*y*z/100
    return s
def amount(x,y):
    return x+y
p=float(input("Enter principle amount :"))
r=float(input("Enter rate of interest :"))
t=float(input("Enter how many year :"))
si=interest(p,r,t)
print("Simple interest :",si)
amt=amount(p,si)
print("Amount :",amt)

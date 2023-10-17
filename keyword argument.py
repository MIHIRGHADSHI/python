def interest (x,y,z):
    s=x*y*z/100
    a=s+x
    return s,a

p=float(input("Enter principle amount :"))
r=float(input("Enter rate of interest :"))
t=float(input("Enter how many year :"))
si,amt=interest(y=r,x=p,z=t)
print("Simple interest :",si)
print("Amount :",amt)

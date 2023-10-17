def addition_2(a,b):
    return a+b

def addition_3(a,b,c):
    return a+b+c

def addition_4(a,b,c,d):
    return a+b+c+d


print("1. sum of 2 nos. ")
print("2. sum of 3 nos. ")
print("3. sum of 4 nos. ")
ch=int(input("Enter your choice :"))
if ch==1:
    a=float(input("Enter First Number :"))
    b=float(input("Enter Second Number :"))
    result=addition_2(a,b)
    print("Sum of 2 nos is :",result)

elif ch==2:
    a=float(input("Enter First Number :"))
    b=float(input("Enter Second Number :"))
    c=float(input("Enter Third Number :"))
    result=addition_3(a,b,c)
    print("Sum of 3 nos is :",result)

elif ch==3:
    a=float(input("Enter First Number :"))
    b=float(input("Enter Second Number :"))
    c=float(input("Enter Third Number :"))
    d=float(input("Enter Fourth Number :"))
    result=addition_4(a,b,c,d)
    print("Sum of 4 nos is :",result)

else :
    print("Invalid Choice :")
    
    

   

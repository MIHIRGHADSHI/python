#eaxple of Recursion
#recursion is used in user defined function
#and in place of loop
#WAP to find the factorial of given number

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

#main program
n=int(input("Enter number to finf the factorial :"))
ans=fact(n) #call function
print("Factorial :",ans)      
      

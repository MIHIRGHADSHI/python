#wap to find the factorial of given number

n=int(input("Enter Number :"))
ans=1
while n>0:
    ans=ans*n
    n=n-1
print("Factorial :",ans)    

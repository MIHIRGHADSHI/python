#example for dwefault arguments
def addition(a=0,b=0,c=0,d=0):
    return a+b+c+d

#main program
#callfunction

result=addition(10,20)
print("Sum of 2 nos. :",result)

#callfunction

result=addition(10,20,30)
print("Sum of 2 nos. :",result)

result=addition(b=50,d=40) #keyword argument
print("Sum of 2 nos. :",result)

#example for global variable

a=50 #global variable
def show():#show() user defined function (np passing argument and no return value)
    global a #editing possible in variable a
    print ("Value of a :",a)
    #modify the value of global variable a
    a=a+40
    print("After editing value of a :",a)

#main program
#call function
show()
print ("Value of a :",a)

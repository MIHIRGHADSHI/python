"""mobile=input("Enter Mobile N0. ")
if(mobile.isdigit()):
    print("type of mobile : ",type(mobile))
    mobile=int(mobile)
    print("type of mobile : ",type(mobile))
else:
    print("Please enter integer value")


#isdigit() : return answer true/false
#isdigit()inbuilt string function ,it is used to check given input is digit
#or not (0-9)"""


mobile=input("Enter Mobile N0. ")
if(mobile.isdigit()):
    x=len(mobile)
    if x==10:
        print("Valid mobile no. ",mobile)
    else:
            print("type of mobile : ",type(mobile))
    
else:
     print("Please enter integer value")

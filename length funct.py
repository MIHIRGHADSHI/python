mobile=int(input("Enter Mobile no."))
print("type of mobile : ",type(mobile))
x=len(str(mobile))
#str() inbuilt function . it is used to converts int into strinf data type
if x==10:
    print(mobile)
else:
    print("Invalid mobile no.")
 

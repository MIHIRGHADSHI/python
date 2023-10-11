#isalpha() means only alphabets
#isalnum() both alphabets and number


userid=input("Enter Userid , please enter only alphabets ")
if(userid.isalpha()):
    password=input("Enter Password : ")
    print("Successfully Login")
    print("User ID : ",userid)
    print("password : ",password)
else:
    print("Invalid user id , please enter only alphabets")

pinno=2568
i=0
while i<3:
    pin=int(input("Enter pin no. of your card :"))
    if pin==pinno:

        print("Valid Pin no")
        print("Transaction successfully completed")
        break
    else:
        print("Invalid pin  no. ")
        i=i+1
        print("Attemp No. ",i)

print("Good bye")        

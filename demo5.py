n=int(input("How many student :"))
i=1 #intial first student
while i<=n: #outer loop
    name=input("Enter name of student :")
    print("Name :",name)
    j=1 #initial marks of first subject
    while j<=3 : #inner loop
        marks=int(input("Enter marks of student :"))
        print("Marks of {} subject of {} student {}".format(j,i,marks))
        j=j+1 #increment inner loop
    i=i+1    #increment outer loop

"""i=1 #initial value for line
while i<=5: #outer loop for line
    j=1 #initial value for column
    while j<=i: #inner lool for column
        print("*",end="")
        j=j+1#increment column j by 1
    i=i+1 #increment line i by 1
    print() #go to new line"""


for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()    

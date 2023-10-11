"""#for eg
txt="hello ,india ."
print(txt)
print(txt.capitalize())
print(txt.title())
print(txt.upper())"""

#lstrip() inbuilt string function : left strip
#rstrip () right strip

price1='$78'
price2='$90'

#total=price1+price2 #total='$78'+'$90' ='$78$90'

price1=price1.lstrip('$')
print(price1,type(price1))
price1=int(price1)
price2=price2.lstrip('$')
print(price1,type(price2))
price2=int(price2)
print("Type of price1 : {} and type of price2 : {}" .format(type(price1),type(price2)))

total=price1+price2
print("Total Price : ",total)      

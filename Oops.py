'''
class Person:
    hands=1
    legs=2
    
    def walking(self):
        print("Hi.. I'm Human. I can walk")

    def talking(self):
        print("Hi.. I'm Human. I can talk")

human1=Person()
print(human1.hands)
print(human1.legs)
human1.walking()
human1.talking()
print(type(human1))


class Person:
    def set_attributes(self ,n ,a):
        self.name=n
        self.age=a
    def get_attributes(self):
        print(f"name : {self.name}\nAge : {self.age}")

obj=Person()
obj.set_attributes("Itvedant",4)
obj.get_attributes(


class Person:
    def __init__(self ,n ,a):
        self.name=n
        self.age=a
    def get_attributes(self):
        print(f"name : {self.name}\nAge : {self.age}")

obj=Person("Itvedant",4)
obj.get_attributes()


#__str__ : This method return a string  value which is a more reader friendly
#string  representation of a class object by converting objecy into string

class Person:
    def __init__(self):
        self.name=input("Enter name :")
        self.age=int(input("Enter age : "))
    def __str__(self):
        return f"name : {self.name}\nAge : {self.age}"

obj=Person()
print(obj)


class Person:
    def __init__(self):
        self.name=input("Enter name :")
        self.age=int(input("Enter age : "))
    def __str__(self):
        return f"name : {self.name}\nAge : {self.age}"
    def __del__(self):
        print("Object Destroyed")

obj=Person()
print(obj)
del obj

#static attributes :
# This attributes are defined for entire class and not just for indivisaual objec
# it is declared aoyside any method of class ,if we want to acess this class attributes
# we used class refrence instead of objet refrence , if the value of static attributes
# is changed it will reflect on all the object of the class.

#static mathod :
# This method are bound to the class and not to the object
# by defauly the python interpreter consider the method declare iside the class
# as the object method , so we need to specify the static method by using a decorater
# @staticmethod above the method header.
'''

class student:
    institute="Itvedant" #static attri
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def __str__(self):
        return f"Name : {self.name}\nAge : {self.age}"
    #static method
    @staticmethod
    def display():
        print("Hello World !!")
    @staticmethod
    def add(a,b):
        print(a+b)

obj1=student("Tom",4)
print(obj1)
print(student.institute)
student.display()
student.add(2,3)



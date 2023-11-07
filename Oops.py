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

#Multiple inheritance

class grand_parent:
    def g_p(self):
        print("Grand Parent")
class parent(grand_parent):
    def hello(self):
        print("Hello world")
class child(parent):
    pass

obj=child()
obj.g_p()
obj.hello()

obj1=parent()
obj1.g_p()
obj1.hello()


#one parent many children
#hierarchical inheritance
class shape:
    def shape_(self):
        print("shape class")
class rectangle(shape):
    pass
class square(shape):
    pass
class circle(shape):
    pass

r=rectangle()
r.shape_()

s=square()
s.shape_()

c=circle()
c.shape_()

'''
#Multilevel
'''
class mother:
    def mommy(self):
        print("Mommy")
class father:
    def daddy(self):
        print("Daddy")
class child(mother,father):
    pass

c=child()
c.mommy()
c.daddy()

'''
#Method overriding
#is a process in which the method inherited from a parent class gets a new implementation
#in the child class, so while overriding the method we need to make sure that the method
#name is same as defined in the parent and even the nuber of parameter should also be same
'''
class mother:
    def display(self):
        print("Mommy")
class father:
    def display(self):
        print("Daddy")
class child(father,mother):
    def display(self): #method overriding
        print("child")
        #super().display()
        mother.display(self)
        father.display(self)

c=child()
c.display()
'''
#Polymorphism
'''
class student:
    def __init__(self,n,a,m):
        self.name=n
        self.age=a
        self.marks=m
    def __add__(self,other):
        total=self.marks+other.marks
        print(total)
    def __sub__(self,other):
        print("Hi ! I override subtraction")
s1=student("Tom",4,90)
s2=student("Jerry",2,23)
s1+s2
s1-s2
'''

class customer:
    def __init__(self,n,a,p):
        self.name=n
        self._age=a
        self.__pwd=p
    def display(self):
        print(f"{self.name}\n{self._age}\n{self._pwd}")
        self._displaypwd()
    def _displayage(self):
        print("Protected access.")
    def __displaypwd(self):
        print("Private access")

class seller(customer):
    pass

c=customer("Tom1",4,"Jerry1")
c.display()
c._displayage()
c.__displaypwd()
            
s=seller("Tom",4,"Jerry")
s.display()
s._displayage()
s.__displaypwd()
                
    

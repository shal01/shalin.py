# class Vehicle:
#     def setdetails(self,type,name,catagory):
#         self.name=name
#         self.type=type
#         self.catagory=catagory
#     def printvalue(self):
#         print(self.type,self.company,self.color)
# class Bus(Vehicle):
#     def busdetails(self,company,color,price):
#         self.company = company
#         self.color = color
#         self.price=price
#     def printbus(self):
#         print(self.company,self.color,self.price)
# bus1=Bus()
# bus1.busdetails("Benz","red",4300000)
# bus1.printbus()
# bus1.setdetails("Car","classy","XUV")
# bus1.printvalue()



# class Person:
#         def setvalue(self, name, age, place):
#             self.name = name
#             self.age = age
#             self.place = place
#
#         def printvalue(self):
#             print(self.name, self.age, self.place)
# class Child(Person):
#     def get_child(self,school,stanterd):
#         self.school=school
#         self.std=stanterd
#
#     def print_chld(self):
#         print(self.school,self.std)
# class Parent:
#     def get_parent(self, address, ph_no):
#         self.address = address
#         self.ph_no = ph_no
#
#     def printparent(self):
#         print(self.address, self.ph_no)
# class Employee(Person,Parent):
#     compy_name = "emirald"
#
#     def emp(self, id, salary, desig):
#         self.id = id
#         self.salary = salary
#         self.desig = desig
#
#     def printemploye(self):
#         print(self.name, self.id, self.salary, self.desig, Employee.compy_name)
# class Student(Child):
#     def setstudent(self,rollno,dep):
#         self.rollno=rollno
#         self.dep=dep
#     def printstu(self):
#         print(self.name,"roll_no",self.rollno,self.dep)


# Oddoreven=lambda n:n%2==0
# n=int(input("enter a number"))
# print(Oddoreven(n))

# class Animal:
#     def __init__(self,catagory,name):
#         self.ctgry=catagory
#         self.name=name
#     def printanimal(self):
#         print(self.ctgry,self.name)
# class Dog(Animal):
#     def __init__(self,breed,age,catagory,name):
#         super().__init__(catagory,name)
#         self.breed=breed
#         self.age=age
#     def printdog(self):
#         print(self.breed,self.age)
#         print(self.ctgry,self.name)
# pet=Dog("Canidae",3,"wolf","siberian_husky")
# pet.printanimal()
# pet.printdog()

class Notebook:
    def setdetails(self,type,size,prize):
        self.type=type
        self.size=size
        self.prize=prize
    def printdetails(self):
        print(self.type,self.size,self.prize)
class Book(Notebook):
    def setdetails(self,name,pages,amount):
        self.name=name
        self.pages=pages
        self.amount=amount
    def printdetails(self):
        print(self.name,self.pages,self.amount)
class Secondbook:
    def setdetails(self,brand,prise,line):
        self.brand=brand
        self.prise=prise
        self.line=line
    def printdetail(self):
        print(self.brand,self.prise,self.line)
bk=Secondbook
bk.setdetails("classmate",60,"whiteline")
bk.printdetail()

# class Notebook:
#     def select(self):
#         print("buy blankone")
# class Book(Notebook):
#     def select(self):
#         print("Buy classmate")
# class Anotherchild(Book):
#     def select(self):
#         print("buy lined")
# bk=Anotherchild
# bk.select()

# import re
# x='/d'
#


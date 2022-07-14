# Tostring is used to add values to reference which is related to arguments

# use return function

class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalues(self):
        print(self.name,self.age,self.place)
    def __str__(self):
        return str(self.age)  + self.name
prs=Person("Hilal",22,"Kundannoor")
prs.printvalues()
print(prs)

# Employee company name id
class Employee:
    def __init__(self,name,id,salary,department):
        self.name=name
        self.id=id
        self.salary=salary
        self.dprt=department
    def printvalues(self):
        print(self.name,self.id,self.salary,self.dprt)
    def __str__(self):
        return self.name+str(self.id)
emp=Employee("lalu","099",80000,"csit")

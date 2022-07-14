class student:
    def __init__(self,name,rollno,dprt,mark):
        self.name=name
        self.rollno=rollno
        self.dprt=dprt
        self.mark=mark
    def printvalues(self):
        print(self.name,self.rollno,self.dprt,self.mark)
f=open("student.txt",'r')
for i in f:
    data=i.rstrip("\n").split(",")
    name=data[0]
    rollno=data[1]
    dprt=data[2]
    mark=data[3]
    stud=student(name,rollno,dprt,mark)
    stud.printvalues()


class person:
    def setvalue(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name,self.age,self.place)
obj=person()
obj.setvalue("anu",24,"kochi")
obj.printvalue()

obj1=person()
obj1.setvalue("hritik",24,"thrissur")
obj1.printvalue()
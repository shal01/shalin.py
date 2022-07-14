# Same method name and different no of arguments

# it work depend on how much argument we add

class Sum:
    def findsum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1+self.num2)
class Add(Sum):
    def findsum(self,no1,no2,no3):
        self.no1=no1
        self.no2=no2
        self.no3=no3
        print(self.no1+self.no2+self.no3)
add=Add()
add.findsum(12,30,3)
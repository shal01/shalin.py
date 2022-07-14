class Add:
    def input(self,num1,num2):
        self.num1=num1
        self.num2=num2
        self.sum=self.num1+self.num2
    def print(self):
        print(self.num1)
        print(self.num2)
        print(self.sum)
obj=Add()
obj.input(6,2)
obj.print()
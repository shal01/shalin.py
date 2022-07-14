# self keyword is used to point the current instance.

class Display_numbers:
    def getnumber(self,no1,no2):
        self.no1=no1
        self.num2=no2
    def print_numbers(self):
        print(self.no1)
        print(self.num2)
d1=Display_numbers()
d1.getnumber(6,4)
d1.print_numbers()